#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_build.py
# @Author: TangYong
# @Time: 二月 11, 2021

import  os
from config import  settings

import pytest
case_path = r'D:\autotest\cases\system\AF\8041'
def exe_test_case():
    # 切换到项目根路径
    project_root_path = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')
    os.chdir(project_root_path)
    os.system(
        f'pytest -s -n auto  -v {case_path}  --html={settings.test_raw_html_report} --self-contained-html --alluredir={settings.test_allure_json_report} --clean-alluredir')
    os.system(f'allure generate {settings.test_allure_json_report} -o {settings.test_allure_html_report} --clean')

    os.system(f'allure open {settings.test_allure_html_report}')










if __name__ == '__main__':


    exe_test_case()






