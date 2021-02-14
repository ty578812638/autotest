#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_param.py
# @Author: TangYong
# @Time: 二月 11, 2021

import allure
import pytest
from cases.system.AF import case_data


@pytest.mark.parametrize('data',[1,2,3])
def test_1(data):
    case_data.case_test_record_list.append(
        {'case_no': 'F0001', 'case_name': 'test01', 'case_story': '测试场景', 'exp_res': '预期结果', 'act_res': '实际结果'})
    assert data > 2


@pytest.mark.parametrize('data1,data2',[(2,3),(4,5),(6,7)])
def test_2(data1,data2):
    assert data1+data2 > 9


@pytest.mark.usefixtures('fun')
@allure.title('测试usefixtures调用fixture没有返回值')
def test_3():
    print('test_3')


@allure.title('测试parametrize调用fixture有返回值')
@allure.description('indirect=True 就是相当于把 return_func当成1个函数去执行,第二个参数是必填')
@pytest.mark.parametrize('return_func','', indirect=True)
def test_4(return_func):
    value  = return_func
    assert  value == 2020


@pytest.mark.usefixtures('global_fun')
@allure.title('测试调用全局中conftest中的函数')
def test_5():
    print('test_5')




if __name__ ==  '__main__':
    pass
