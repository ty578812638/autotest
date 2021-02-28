#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_allure.py
# @Author: TangYong
# @Time: 二月 11, 2021

import allure
import sys
from func import public

handel_case_file = public.HandelCaseInfoFile()


@allure.story('测试allure场景')
class TestAllure:
    @allure.title('测试allure title怎么展示')
    def test_allure_1(self):
        act_res = ''
        try:
            assert 5 == 6
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
    def test_allure_2(self):

        try:
            assert 5 == 6
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'


        try:
            assert 5 == 7
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)
        test_case_info = {
            'sys_name': 'AC',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test1003',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)
        public.logger_record(sys._getframe().f_lineno).info(f'test_allure_1:{test_case_info}')


    @allure.severity(allure.severity_level.MINOR)
    @allure.link('www.baidu.com')
    def test_allure_3(self):

        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)
        test_case_info = {
            'sys_name': 'AC',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test1003',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)
        public.logger_record(sys._getframe().f_lineno).info(f'test_allure_1:{test_case_info}')


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('www.baidu.com',name='百度')
    def test_allure_4(self):
        print('ok3')
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)
        test_case_info = {
            'sys_name': 'AC',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test1003',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)
        public.logger_record(sys._getframe().f_lineno).info(f'test_allure_1:{test_case_info}')


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('12345678','TANGYONG')
    def test_allure_4(self):
        print('ok5')
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)
        test_case_info = {
            'sys_name': 'AC',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test1003',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)
        public.logger_record(sys._getframe().f_lineno).info(f'test_allure_1:{test_case_info}')

    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_5(self):
        print('ok00')
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)
        test_case_info = {
            'sys_name': 'AC',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test1003',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)
        public.logger_record(sys._getframe().f_lineno).info(f'test_allure_1:{test_case_info}')


if __name__ == '__main__':
    import pytest
    pytest.main(['-s'])