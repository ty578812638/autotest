#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_21.py
# @Author: TangYong
# @Time: 二月 20, 2021


# __*__coding:utf-8 __*__

import allure

@allure.step('1')
def test_dome_10():
    '''用例描述: 用例一的接口'''
    print("这个是第一个用例对应的接口")
    allure.step('9990000')

@allure.step('2')
def test_dome_20():
    '''用例描述: 用例二的接口'''
    print("这个是第二个用例对应的接口")
    allure.step('999999')

@allure.step('3')
@allure.feature("资源管理模块")
class test_dome_30(object):
    '''这个是一个模块的测试'''
    @allure.step("操作步骤: 新增资源个人信息")
    def test_dome_40(self):
        '''用例描述: 用例三的新增内容接口'''
        print("这个是第三个用例对应的接口一")
        allure.step('999')

    @allure.step("操作步骤: 查询资源在线信息")
    def test_dome_50(self):
        '''用例描述: 用例三的查询内容接口'''
        print("这个是第三个用例对应的接口二")


    @allure.step("操作步骤: 修改资源身份信息")
    def test_dome_60(self):
        '''用例描述: 用例三的编辑内容接口'''
        print("这个是第三个用例对应的接口三")

    @allure.step("操作步骤: 删除资源全部信息")
    def test_dome_70(self):
        '''用例描述: 用例三的删除内容接口'''
        print("这个是第三个用例对应的接口四")