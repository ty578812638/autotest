#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_skip.py
# @Author: TangYong
# @Time: 二月 11, 2021

import allure
import pytest

import requests
from func import public
from cases.system.AF import case_data
handel_case_file = public.HandelCaseInfoFile()

@allure.title('测试skip')
def test_A():
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
        'case_no': 'test4005',
        'case_story': '测试场景',
        'exp_res': '预期结果',
        'act_res': act_res,
        'test_res': test_res,
        'tester': '唐泳',
    }
    handel_case_file.record_test_case_info(test_case_info)

def test_B():
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
        'case_no': 'test4003',
        'case_story': '测试场景',
        'exp_res': '预期结果',
        'act_res': act_res,
        'test_res': test_res,
        'tester': '唐泳',
    }
    handel_case_file.record_test_case_info(test_case_info)
    return 6



pytest.mark.skipif(test_B() > 5,reason='不执行了')
def test_C():
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
        'case_no': 'test4000',
        'case_story': '测试场景',
        'exp_res': '预期结果',
        'act_res': act_res,
        'test_res': test_res,
        'tester': '唐泳',
    }
    handel_case_file.record_test_case_info(test_case_info)




if __name__ ==  '__main__':
    pass

