#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: settings.py
# @Author: TangYong
# @Time: 二月 11, 2021

import  os
import time
import  logging


#当前路径
current_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

#项目根路径
project_root_path =  os.path.split(current_path)[0]

#用例根路径
case_root_path = os.path.join(project_root_path,'cases','system').replace('\\','/')

#测试报告根路径
report_root_path = os.path.join(project_root_path,'report')


#日志根路径
# log_root_path = os.path.join(project_root_path, 'logs','%s', time.strftime('%Y%m%d') + '_AutoTest.log').replace('\\','/')
log_root_path = os.path.join(project_root_path, 'logs','%s').replace('\\','/')


# #测试环境测试报告路径
test_allure_json_report = os.path.join(report_root_path,'test_report','%s','allure','json_report').replace('\\','/')
test_allure_html_report = os.path.join(report_root_path,'test_report','%s','allure','html_report').replace('\\','/')
test_raw_html_report = os.path.join(report_root_path,'test_report','%s','html').replace('\\','/')


#生产环境测试报告路径
product_allure_json_report = os.path.join(report_root_path,'product_report','%s','allure','json_report').replace('\\','/')
product_allure_html_report = os.path.join(report_root_path,'product_report','%s','allure','html_report').replace('\\','/')
product_raw_html_report = os.path.join(report_root_path,'product_report','%s','html').replace('\\','/')


#测试用例信息路径
test_case_info_data = os.path.join(project_root_path,'data','case_info.json')

#临时数据
tmp_data_info = os.path.join(project_root_path,'data','tmp_data.json')


#web服务器上传测试用例接口地址
web_server_test_case_host = 'http://192.168.1.4:9000/saveTestInfo/'

#web服务器上传测试报告接口地址
web_server_test_report_host = 'http://192.168.1.4:9000/getTestReport/'


#邮件配置信息
mail_info = {
    'connect':{
        'host':'smtp.qq.com',
        'port':465
    },
    'login':{
        'username':'578812638',
        'passwd':'' #填写授权码
    },
    'sender':'578812638@qq.com',
    'receiver':['tyongjob@163.com','ty334420163@qq.com'],
    'subject':'%s_自动化测试报告'
}

#日志层级
log_level_list={
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.CRITICAL
}
log_level = log_level_list['info']












