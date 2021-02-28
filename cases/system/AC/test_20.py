#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_20.py
# @Author: TangYong
# @Time: 二月 14, 2021

import sys
import allure
import pytest
from func import public

handel_case_file = public.HandelCaseInfoFile()


@pytest.fixture()
def up_teardown():
    '''
    前后置测试
    :return:
    '''
    with allure.step('set_up'):
        allure.attach(body='set_up',name='附件名称')

    yield

    with allure.step('teardown'):
        allure.attach(body='set_up', name='附件名称')



@pytest.fixture()
def up_teardown_ret_val():
    '''
    前后置返回值测试
    :return: 5
    '''
    with allure.step('up_teardown_ret_val'):
        allure.attach(body='set_up',name='附件名称')
        return 5



@pytest.fixture()
def up_teardown_par(request):
    '''
    前后置返回值测试
    :return:val
    '''
    val = request.param
    with allure.step('fixture参数测试'):
        allure.attach(body='参数测试', name='参数名称')
        public.log_record(sys._getframe().f_lineno).info(val)
        return val

@allure.story('测试allure场景')
class TestAllureAC:
    '''
    test
    '''

    @allure.tag('唐泳',500236)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('测试allure报告怎么展示附件')
    def test_allure_10(self):
       act_res = ''
       try:
            assert 5==6
            act_res = 'passed'
       except Exception as e:
            act_res = str(e)
            raise e
       finally:
           test_res = 'Failed'
           test_case_info = {
               'sys_name': 'AD',
               'ver_no': '8040',
               'case_name': '用例名称',
               'case_no': 'test0002',
               'case_story': '测试场景',
               'exp_res': '预期结果',
               'act_res': act_res,
               'test_res': test_res,
               'tester': '唐泳',
           }
           handel_case_file.record_test_case_info(test_case_info)
           with allure.step('日志记录'):
               public.log_record(sys._getframe().f_lineno).info(f'test_allure_1:{test_case_info}')

           with allure.step('请求信息'):
               allure.attach(name="请求接口", body=str('1'))

           with allure.step('响应信息'):
               allure.attach(name="响应信息", body=str(test_case_info))

           with allure.step('日志信息'):
               allure.attach(body=str(test_case_info), name='日志信息')

           with allure.step('图片'):
               allure.attach.file(r'C:\Users\Lenovo\Desktop\bak\1.bmp', '图片')


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('测试allure description 怎么展示')
    def test_allure_20(self):

        with allure.step('test_allure_20'):
            public.log_record(sys._getframe().f_lineno).info(f'test_allure_1:{999}')

        act_res = '实际结果'
        assert 5 == 5

        test_res = 'Failed'
        test_case_info = {
            'sys_name': 'AD',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test0002',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)
        public.log_record(sys._getframe().f_lineno).debug( f'test_allure_1:{test_case_info}')


    @pytest.mark.usefixtures('up_teardown')
    @allure.severity(allure.severity_level.MINOR)
    @allure.link('www.baidu.com')
    @allure.title('前后置测试')
    def test_allure_30(self):
        with allure.step('前后置通过 pytest.mark.usefixtures 调用测试'):
            allure.attach(body='前后置测试', name='前后置测试')


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('前后置测试')
    def test_allure_40(self,up_teardown):
        with allure.step('前后置函数直接调方式测试'):
            allure.attach(body='前后置测试', name='前后置测试')


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('前后置测试返回值测试')
    def test_allure_50(self,up_teardown_ret_val):
        with allure.step('前后置函数直接调方式测试'):
            allure.attach(body='前后置测试', name='前后置测试')
            assert up_teardown_ret_val == 8

    data = [
        {"username": "name1", "pwd": "pwd1"},
        {"username": "name2", "pwd": "pwd2"},
    ]

    @pytest.mark.parametrize('up_teardown_par',data,indirect=True )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_60(self,up_teardown_par):
        val = up_teardown_par
        with allure.step('前后置函数传参测试'):
            allure.attach(body='前后置函数传参测试', name='前后置函数传参测试')
            assert val == 9


    @pytest.mark.parametrize('param',[5,6])
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('单个参数测试')
    def test_allure_70(self,param):
        with allure.step(f'单个参数测试：{param}'):
            allure.attach(body=f'第一个参数值是：{param}', name='单个参数多个值测试')
            assert 5 == param

    @pytest.mark.parametrize('param1,param2', [(3,3),(4,4),(5,5)])
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('多个参数测试')
    def test_allure_80(self, param1,param2):

        with allure.step(f'多参数测试：{param1,param2}'):
            allure.attach(body=f'参数是：{param1,param2}', name='多参数多个值测试')
            assert param1+param2 > 7



if __name__ == '__main__':
    pytest.main(['-v',r'D:\project\autotest\cases\system\AC\test_20.py','--html=./report.html'])