#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_skip.py
# @Author: TangYong
# @Time: 二月 11, 2021
import requests
import allure
import pytest

@allure.title('测试skip')
def test_A():
    response = requests.post(
        url='http://192.168.1.6:9000/saveTestInfo/',
        json={'case_no': 'F0001', 'case_name': 'test01', 'case_story': '测试场景', 'exp_res': '预期结果', 'act_res': '实际结果'},
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
    )
    print('测试完成:', response.text)

    assert  5 == 5
    pytest.mark.skip('后面不执行了')


def test_B():
    response = requests.post(
        url='http://192.168.1.6:9000/saveTestInfo/',
        json={'case_no': 'F0001', 'case_name': 'test01', 'case_story': '测试场景', 'exp_res': '预期结果', 'act_res': '实际结果'},
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
    )
    print('测试完成:', response.text)
    return 8


pytest.mark.skipif(test_B() > 5,reason='不执行了')
def test_C():
    response = requests.post(
        url='http://192.168.1.6:9000/saveTestInfo/',
        json={'case_no': 'F0001', 'case_name': 'test01', 'case_story': '测试场景', 'exp_res': '预期结果', 'act_res': '实际结果'},
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
    )
    print('测试完成:', response.text)
    print('test_C')





if __name__ ==  '__main__':
    pass

