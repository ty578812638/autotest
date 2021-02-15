#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_allure.py
# @Author: TangYong
# @Time: 二月 11, 2021

import allure
from func import public

handel_case_file = public.HandelCaseInfoFile()


@allure.story('测试allure场景')
class TestAllure:
    @allure.title('测试allure title怎么展示')
    def test_allure_1(self):
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)
        test_case_info = {
            'sys_name': 'AF',
            'ver_no': '8040',
            'case_name': '用例名称',
            'case_no': 'test2000',
            'case_story': '测试场景',
            'exp_res': '预期结果',
            'act_res': act_res,
            'test_res': test_res,
            'tester': '唐泳',
        }
        handel_case_file.record_test_case_info(test_case_info)


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('测试allure description 怎么展示')
    def test_allure_2(self):

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


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('www.baidu.com',name='百度')
    def test_allure_4(self):
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


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('12345678','TANGYONG')
    def test_allure_4(self):
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

    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_5(self):
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

if __name__ == '__main__':
    import pytest
    pytest.main(['-s'])