#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_b.py
# @Author: TangYong
# @Time: 二月 15, 2021

from func import public
handel_case_file = public.HandelCaseInfoFile()

def test_a1():
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

def test_a2():
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
        'case_no': 'test1004',
        'case_story': '测试场景',
        'exp_res': '预期结果',
        'act_res': act_res,
        'test_res': test_res,
        'tester': '唐泳',
    }
    handel_case_file.record_test_case_info(test_case_info)


def test_a3():
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
        'case_no': 'test1005',
        'case_story': '测试场景',
        'exp_res': '预期结果',
        'act_res': act_res,
        'test_res': test_res,
        'tester': '唐泳',
    }
    handel_case_file.record_test_case_info(test_case_info)