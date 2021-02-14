#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: conftest.py
# @Author: TangYong
# @Time: 二月 11, 2021
import pytest

@pytest.fixture(scope='function')
def fun():
    print('这是前置函数')


@pytest.fixture(scope='class')
def cls():
    print('这是前置类')


@pytest.fixture(scope='module')
def mod():
    print('这是前置模块')



@pytest.fixture(scope='session')
def mod():
    print('这是前置session')


@pytest.fixture()
def return_func():
    print('这是一个有返回值的函数')
    return 2021

@pytest.fixture()
def parm_func(request):
    par = request.param
    print(f'这是一个需要有参数的函数,参数值是:{par}')
    return par

