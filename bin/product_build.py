#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: product_build.py
# @Author: TangYong
# @Time: 二月 11, 2021


import os
import  sys
import time
import requests


cur_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.split(cur_path)[0]
sys.path.append(project_path)

from config import settings


def  get_test_report(test_report):
    '''

    :param test_report:  HTML原生测试报告地址
    :return:
    '''

    response = requests.post(
        url=settings.web_server_test_report_host,
        files= {'test_report':open(test_report,'rb') },
        # headers={
        #     'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        # }
    )
    print('上传测试报告:',response.text)


def exe_test_case(case_file_name=''):
    '''
    :param case_file_name:  需要执行的用例文件名称，默认为执行所有用例
    :return:
    '''
    cur_time = time.strftime('%Y%m%d%H%M%S')
    if case_file_name:

        #执行指定文件中的测试用例
        case_path = os.path.join(settings.case_root_path,case_file_name)

        case_file_name = case_file_name.replace('\\', '')
        #测试报告根据执行的文件名命名
        product_raw_html_report = os.path.join(
            settings.product_raw_html_report,case_file_name+'_testReport_'+ cur_time+ '.html').replace('\\','/')


    else:
        #执行所有测试用例
        case_path = settings.case_root_path

        product_raw_html_report =os.path.join(settings.product_raw_html_report,'all_sys_TestReport_'+cur_time+'.html').replace('\\','/')


    if not os.path.exists(case_path):
        raise OSError(f'用例路径【{case_path}】不存在' )


    # 切换到项目根路径
    project_root_path = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')
    os.chdir(project_root_path)

    os.system( f'pytest -s -n auto  -v {case_path}  --html={product_raw_html_report} --self-contained-html --alluredir={settings.product_allure_html_report} --clean-alluredir')


    os.system(f'allure generate {settings.product_allure_json_report} -o {settings.product_allure_html_report} --clean')

    get_test_report(product_raw_html_report)

    os.system(f'allure open {settings.test_allure_html_report}')
    #




if __name__ == '__main__':
    try:
        case_path = sys.argv[1]
    except Exception:
       case_path =project_path

    exe_test_case()
