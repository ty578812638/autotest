#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_20.py
# @Author: TangYong
# @Time: 二月 14, 2021

import allure
from func import public

handel_case_file = public.HandelCaseInfoFile()

@allure.story('测试allure场景')
class TestAllureAC:
    @allure.title('测试allure title怎么展示')
    def test_allure_1(self):
       try:
           assert  5==5
           test_res = 'Passed'
           act_res = '实际结果'
       except Exception as e:
           test_res = 'Failed'
           act_res = str(e)
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






    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('测试allure description 怎么展示')
    def test_allure_20(self):

        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

        test_case_info = {
            'sys_name':'AD',
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.link('www.baidu.com')
    def test_allure_30(self):
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

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


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('www.baidu.com',name='百度')
    def test_allure_40(self):
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

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


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('12345678','TANGYONG')
    def test_allure_50(self):
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

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

    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_60(self):
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

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