#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: product_build.py
# @Author: TangYong
# @Time: 二月 11, 2021


import os
import  sys
import time


cur_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.split(cur_path)[0]
sys.path.append(project_path)

from func import public
from config import settings

def exe_test_case(case_file_name):
    '''
    该文件中的代码只能用于Linux环境上进行生产构建
    :param case_file_name:  需要执行的用例文件名称
    :return:
    '''

    #年月日时分秒时间格式化
    cur_time = time.strftime('%Y%m%d%H%M%S')

    #执行指定文件中的测试用例
    case_path = os.path.join(settings.case_root_path,case_file_name).replace('\\','/')
    case_file_name = case_file_name.replace('\\', '')

    #测试报告根据执行的文件名命名
    product_raw_html_report = os.path.join(
        settings.product_raw_html_report,case_file_name+'_testReport_'+ cur_time+ '.html').replace('\\','/')


    if not os.path.exists(case_path):
        raise OSError(f'用例路径【{case_path}】不存在' )

    #文件对象
    handel_case_file = public.HandelCaseInfoFile()

    #执行用例，先清空测试用例信息文件中的内容
    handel_case_file.clear_case_info()

    #执行测试用例
    os.system( f'python3 -m pytest -s -n auto  -v {case_path}  --html={product_raw_html_report} --self-contained-html --alluredir={settings.product_allure_json_report} --clean-alluredir')

    #从用例信息中读取用例信息
    case_info_list = handel_case_file.get_test_case_info()
    print('case_info_list:',case_info_list)

    # 回传测试用例信息给web服务
    public.callback_test_case_info(case_info_list)

    #回传测试报告给web服务
    public.callback_test_test_report(product_raw_html_report)

     #生成allure的html报告
    os.system(f'allure generate {settings.product_allure_json_report} -o {settings.product_allure_html_report} --clean')

    #自动打开allure的html报告
    os.system(f'allure open {settings.product_allure_html_report}')



if __name__ == '__main__':
   #sys.argv 从命令行接收1个用例文件名称，如 AF或者AF/8040
   try:
        case_file_name = sys.argv[1]
        exe_test_case(case_file_name)
   except:
       raise NameError('需要执行的用例文件名称不能为空,如:AF或者AF\8040')


