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
# from  selenium import  webdriver
# driver = webdriver.Chrome()


@pytest.fixture(scope='function')
def global_fun():
    print('这是全局前置函数')



# from datetime import datetime
# from py.xml import html
# import pytest
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = driver.get_screenshot_as_file(r'D:\project\autotest\report\product_report\html\test.png')
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))