#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_20.py
# @Author: TangYong
# @Time: 二月 14, 2021

import allure
from func import public
from cases.system.AF import case_data

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

       case_data.test_info['case_no'] = 'test0001'
       case_data.test_info['case_name'] = '用例名称1'
       case_data.test_info['case_story'] = '测试场景'
       case_data.test_info['exp_res'] = '预期结果'
       case_data.test_info['act_res'] =act_res
       case_data.test_info['test_res'] = test_res
       public.callback_web_server(case_data.test_info)


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

        case_data.test_info['case_no'] = 'test0002'
        case_data.test_info['case_name'] = '用例名称2'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['exp_res'] = '预期结果'
        case_data.test_info['act_res'] = act_res
        case_data.test_info['test_res'] = test_res
        public.callback_web_server(case_data.test_info)


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

        case_data.test_info['case_no'] = 'test0003'
        case_data.test_info['case_name'] = '用例名称3'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['exp_res'] = '预期结果'
        case_data.test_info['act_res'] = act_res
        case_data.test_info['test_res'] = test_res
        public.callback_web_server(case_data.test_info)


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

        case_data.test_info['case_no'] = 'test0004'
        case_data.test_info['case_name'] = '用例名称4'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['exp_res'] = '预期结果'
        case_data.test_info['act_res'] = act_res
        case_data.test_info['test_res'] = test_res
        public.callback_web_server(case_data.test_info)


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

        case_data.test_info['case_no'] = 'test0005'
        case_data.test_info['case_name'] = '用例名称5'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['exp_res'] = '预期结果'
        case_data.test_info['act_res'] = act_res
        case_data.test_info['test_res'] = test_res
        public.callback_web_server(case_data.test_info)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_60(self):
        try:
            assert 5 == 5
            test_res = 'Passed'
            act_res = '实际结果'
        except Exception as e:
            test_res = 'Failed'
            act_res = str(e)

        case_data.test_info['case_no'] = 'test001'
        case_data.test_info['case_name'] = '用例名称'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['case_story'] = '测试场景'
        case_data.test_info['exp_res'] = '预期结果'
        case_data.test_info['act_res'] = act_res
        case_data.test_info['test_res'] = test_res
        public.callback_web_server(case_data.test_info)
