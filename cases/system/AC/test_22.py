#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_22.py
# @Author: TangYong
# @Time: 二月 21, 2021
import sys
import allure
import pytest
from  func import  public

# @pytest.fixture(scope='function')
# def test_one():
#    print('这是一个前置条件')
#
#
#
# def test_A_A():
#     with allure.step('日志记录1'):
#         public.log_record(sys._getframe().f_lineno).info('999999999999')
#
# def test_A_B():
#     with allure.step('日志记录2'):
#         public.log_record(sys._getframe().f_lineno).info('999999999999')



@pytest.fixture(scope='class')
def login():
    print("输入账号，密码先登录")


def test_1(login):
    print("用例1：登录之后，操作")

@pytest.mark.usefixtures('login')
def test_2():
    print("用例2：不登录，直接操作")


@pytest.mark.parametrize("login", [1,2,3], ids=[4,5,6], indirect=True)
def test_3(login):
    print("用例3：登录之后，操作")


class TestTwo:
    def test_1_1(self):
        print("test_1_1：登录之后，操作")




import pytest
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度")
    yield
    print("执行teardown")
    print("最后关闭浏览器")
def test_10(open):
    print("test_1:搜索fix1")
def test_20():
    print("test_2:搜索fix2")
def test_30():
    print("test_3:搜索fix3")





if __name__=="__main__":
 pytest.main(["-s","test_22.py"])

