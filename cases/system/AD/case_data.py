#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: case_data.py.py
# @Author: TangYong
# @Time: 二月 12, 2021

"""
test_data.py.py：
所有系统里面的全局配置，主要记录测试信息，如用例编号，用例名称等
本地测试完成后，将会传给web服务，然后在前端页面展示。
"""


#当前测试者
tester = 'TangYong'

#当前测试版本
version_no = 'AF8.0.40'

#当前系统名称
sys_name = 'AF'


#单个测试用例信息，会在每个测试用例结束后存储最终的测试信息
test_info = {
    'case_no': '',          #用例编号
    'case_name': '',    #用例名称
    'case_story':'',    #测试 场景
    'exp_res':'',         #预期结果
    'act_res':'',         #实际结果
    'test_res': '',     #测试结果
    'tester':tester,
    'ver_no':version_no,
    'sys_name':sys_name
}

#测试用例记录容器，会存储所有测试用例信息 test_info
case_test_record_list = []


test_dict = {}