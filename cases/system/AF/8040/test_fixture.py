#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_fixture.py
# @Author: TangYong
# @Time: 二月 11, 2021

import allure
import pytest
from cases.system.AF import case_data


@allure.story('测试fixture的参数化')
class TestFixture:
    @pytest.mark.parametrize('parm_func', [2020], indirect=True)
    def test_fix1(self,parm_func):
        v = parm_func
        case_data.case_test_record_list.append(
            {'case_no': 'F0001', 'case_name': 'test01', 'case_story': '测试场景', 'exp_res': '预期结果', 'act_res': '实际结果'})
        assert  v == '2020'

    @pytest.mark.parametrize('parm_func', [2020], indirect=True)
    def test_fix1(self, parm_func):
        case_data.case_test_record_list.append(
            {'case_no': 'F0001', 'case_name': 'test01', 'case_story': '测试场景', 'exp_res': '预期结果', 'act_res': '实际结果'})
        v = parm_func
        assert v == '2021'



if __name__ ==  '__main__':
    pass

