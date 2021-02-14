#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: conftest.py
# @Author: TangYong
# @Time: 二月 11, 2021

"""
该conftest.py文件为当前所有系统里面的全局前置，如登录，退出。
"""

import pytest
@pytest.fixture(scope='function')
def global_fun():
    print('这是全局前置函数')