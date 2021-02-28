#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_build.py
# @Author: TangYong
# @Time: 二月 11, 2021

import os
import  sys
import time

#添加执行路径
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

    #执行指定路径下文件中的系统名称与测试用例
    case_path = os.path.join(settings.case_root_path,case_file_name).replace('\\','/')

    sys_name = case_file_name.split('/')[0]
    case_file_name = case_file_name.replace('\\', '')


    #根据系统名称格式化系统报告路径
    test_raw_html_report = os.path.join(
        settings.test_raw_html_report,case_file_name+'_testReport_'+ cur_time+ '.html').replace('\\','/')%sys_name

    test_allure_json_report = settings.test_allure_json_report %sys_name
    test_allure_html_report = settings.test_allure_html_report %sys_name

    #根据不同系统生成不同的日志路径
    settings.sys_name = sys_name



    if not os.path.exists(case_path):
        raise OSError(f'用例路径【{case_path}】不存在' )

    #文件对象
    handel_file = public.HandelCaseInfoFile()

    #执行用例，先清空测试用例信息文件中的内容
    handel_file.clear_data()

    #将系统名称写入到临时文件
    handel_file.record_tmp_data({'sys_name':sys_name})


    #执行测试用例
    os.system( f'pytest -n auto  -vs {case_path}   --html={test_raw_html_report} --self-contained-html --alluredir={test_allure_json_report} --clean-alluredir')

    # #从用例信息中读取用例信息
    case_info_list = handel_file.get_test_case_info()
    print('case_info_list:',case_info_list)

    # 回传测试用例信息给web服务
    try:
        public.callback_test_case_info(case_info_list)
    except Exception as e:
        public.log_record(sys._getframe().f_lineno).warning('测试用例回传web服务失败:',str(e))

    # 回传测试报告给web服务
    try:
        public.callback_test_test_report(test_raw_html_report)
    except Exception as e:
        public.log_record(sys._getframe().f_lineno).warning('测试报告回传web服务失败:', str(e))

    #发送邮件：
    try:
        public.send_email(test_raw_html_report)
    except Exception as e:
        public.log_record(sys._getframe().f_lineno).warning('发送邮件失败:', str(e))


     #生成allure的html报告
    os.system(f'allure generate {test_allure_json_report} -o {test_allure_html_report} --clean')

    # #自动打开allure的html报告
    os.system(f'allure open {test_allure_html_report} --port 52001')



if __name__ == '__main__':
   #如 AF或者AF/8040
   exe_test_case('AC')



