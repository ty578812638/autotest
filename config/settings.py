#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: settings.py
# @Author: TangYong
# @Time: 二月 11, 2021

import  os
import  logging


#当前路径
current_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

#项目根路径
project_root_path =  os.path.split(current_path)[0]

#用例根路径
case_root_path = os.path.join(project_root_path,'cases','system').replace('\\','/')

#测试报告根路径
report_root_path = os.path.join(project_root_path,'report')

#测试环境测试报告路径
test_allure_json_report = os.path.join(report_root_path,'test_report','allure','json_report').replace('\\','/')
test_allure_html_report = os.path.join(report_root_path,'test_report','allure','html_report').replace('\\','/')
test_raw_html_report = os.path.join(report_root_path,'test_report','html','test_report.html').replace('\\','/')

#生产环境测试报告路径
product_allure_json_report = os.path.join(report_root_path,'product_report','allure','json_report').replace('\\','/')
product_allure_html_report = os.path.join(report_root_path,'product_report','allure','html_report').replace('\\','/')
product_raw_html_report = os.path.join(report_root_path,'product_report','html').replace('\\','/')

#web服务器上传测试用例接口地址
web_server_test_case_host = 'http://192.168.1.4:9000/saveTestInfo/'

#web服务器上传测试报告接口地址
web_server_test_report_host = 'http://192.168.1.4:9000/getTestReport/'

#邮件配置信息
mail_info = {
    'concent':{
        'host':'mail.tcl.com',
        'port':25
    },
    'login':{
        'username':'tangyong01',
        'passwd':'jy170530.'
    },
    'sender':'tangyong01@kuyumall.com',
    'receiver':['tangyong01@kuyumall.com','tyongjob@163.com','ty334420163@qq.com'],
    'subject':'聚采平台自动化测试'
}

#日志层级
log_level_list={
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.critical
}
log_level = log_level_list['info']


























# from  selenium import  webdriver
# from  selenium.webdriver.common.by import By
# import smtplib
# from email.header import Header
# from email.mime.text import  MIMEText
# from email.mime.multipart import MIMEMultipart
# import  xlrd
# driver  =webdriver.Chrome()
#
# url  = 'http://10.0.101.163:81/JcLogin'
#
# def get_excel_data(row_no,col_no,file_name,sheet_index=0):
#     file_dir = os.path.join(base_dir,'settings',file_name)
#     work_bok = xlrd.open_workbook(file_dir)
#     sheet = work_bok.sheet_by_index(sheet_index)
#     cell_data = sheet.cell(row_no,col_no).value
#     return  cell_data


