#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: public.py
# @Author: TangYong
# @Time: 二月 11, 2021



import os
import  time
import json
import smtplib
import requests
from email.header import Header
from email.mime.text import MIMEText


from config import  settings

class GetCurrentTime:
    '''
    生成不同格式的时间
    '''

    def __init__(self):
        self.current_time = time.localtime()

    def all_number_time(self):

        year = (self.current_time[0])
        year = str(year)

        month = self.current_time[1]
        if month < 10:
            month = ''.join(['0', str(month)])
        else:
            month = str((self.current_time[1]))

        day = self.current_time[2]
        if day < 10:
            day = ''.join(['0', str(day)])
        else:
            day = str((self.current_time[2]))

        hour = self.current_time[3]
        if hour < 10:
            hour = ''.join(['0', str(hour)])
        else:
            hour = str((self.current_time[3]))

        # min = self.current_time[4]
        # if min < 10:
        #     min = ''.join(['0', str(min)])
        # else:
        #     min = str((self.current_time[4]))

        final_time = ''.join([year, month, day, hour])

        return final_time

    def year_mont_day(self):

        year = (self.current_time[0])
        year = str(year)

        month = self.current_time[1]
        if month < 10:
            month = ''.join(['0', str(month)])
        else:
            month = str((self.current_time[1]))

        day = self.current_time[2]
        if day < 10:
            day = ''.join(['0', str(day)])
        else:
            day = str((self.current_time[2]))

        final_date = '/'.join([year, month, day])

        return final_date

    def hour_min_sec(self):

        hour = self.current_time[3]
        if hour < 10:
            hour = ''.join(['0', str(hour)])
        else:
            hour = str((self.current_time[3]))

        min = self.current_time[4]
        if min < 10:
            min = ''.join(['0', str(min)])
        else:
            min = str((self.current_time[4]))

        sec = self.current_time[4]

        if sec < 10:
            sec = ''.join(['0', str(sec)])
        else:
            sec = str((self.current_time[4]))

        final_time = ':'.join([hour, min, sec])

        return final_time

    @classmethod
    def complete_time(cls):
        return  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


class HandelCaseInfoFile:
    '''
    操作用例信息文件，增、删、查
    '''

    def __init__(self):
        '''
        获取用例信息文件路径
        '''
        self.test_case_info_data = settings.test_case_info_data

    def record_test_case_info(self,case_info: dict):
        '''
        将每个case中的用例信息保存到json文件中，
        :param case_info:  每个case中的用例信息，字典形式
        :return:
        '''

        with open(self.test_case_info_data, 'a') as fw:
            fw.write(f"""{case_info}\n""")

    def get_test_case_info(self):
        '''
        将json文件中的用例信息转换成字典
        :param case_info_file: 记录测试用例信息文件
        :return: 字典列表
        '''
        case_info_list = []

        with open(self.test_case_info_data, 'r') as fr:
            case_data = fr.readlines()
            for data in case_data:
                data = data.replace("'",'"')
                js_dt = json.loads(data)
                js_dt['create_time'] = time.strftime('%Y%m%d%H%M%S')
                try:
                    case_info_list.append(js_dt)
                except:
                    pass
            return case_info_list

    def clear_case_info(self):
        '''
        清空测试用例信息
        :return:
        '''
        with open(settings.test_case_info_data, 'w') as fw:
            fw.seek(0)
            fw.truncate()

def generate_test_report(pid,sys_name):

    sys_name = sys_name.replace('\\','_')

    #生成测试报告
    build_report_path = os.path.join(settings.report_root_path,'build').replace('\\','/')
    if not os.path.exists(build_report_path ):
        os.makedirs(build_report_path)

    current_time = time.strftime('%y%m%d%H%M%S')
    report_name = ''.join([pid,'_',sys_name,'_TestReport_',current_time,'.html'])
    report_dir = os.path.join(build_report_path,report_name).replace('\\','/')

    #测试报告详情信息
    report_info = {
        'report_dir':report_dir,
        'report_title':'%s_Auto_Test_Report'%sys_name,
         'report_detail':'请查看附件详情测试报告'
    }

    return report_info


def get_new_report():
    '''
    获取最新测试报告
    :return: 最近一次测试报告
    '''

    report_dir = os.path.join(settings.project_root_path,'report')
    report_list = os.listdir(report_dir)
    '''
    1.在存放报告的路径下对报告的更新时间从早到晚进行排序
    2.lambda:匿名函数，fun参数，用来接收 os.path.getctime(report_dir) 然后将它计算出来的值赋值给key(固定写法)
    '''
    # report_list.sort(key=lambda fn:os.path.getctime(report_dir+'\\'+fn))
    report_list.sort(key=lambda fun: os.path.getctime(report_dir))

    #获取最新测试报告
    new_report = os.path.join(report_dir,report_list[-1])

    return new_report

#发邮件
def send_email():

    #获取最新测试报告并打开
    test_report = get_new_report()
    if test_report:pass
    else:
        return '当前无可用测试报告'

    try:
        with open(test_report,'rb') as fr:
            mail_data = fr.read()

        #定义附件的格式
        mail_attachment = MIMEText(mail_data, 'bases64', 'utf-8')

        # 附件的类型为8进制
        mail_attachment['Content-Type'] = 'application/octet-stream'

        # 添加附件内容的配置信息
        mail_attachment['Content-Disposition'] =" attachment;filename='auto_test_report.html' "

        #创建电子邮件对象,related:表示出了可以发送邮件正文以外,还可以携带各种附件
        mail_content = MIMEText('related')

        # #添加邮件主题
        mail_content['subject'] = Header(settings.mail_info['subject'])

        #添加邮件正文
        mail_content.attach(MIMEText( mail_data,'html','utf-8'))

        #添加邮件附件
        mail_content.attach(mail_attachment)

        smtp = smtplib.SMTP()
        smtp.connect(settings.mail_info['connect']['host'],settings.mail_info['connect']['port'])
        smtp.login(settings.mail_info['login']['username'],settings.mail_info['login']['passwd'])
        smtp.sendmail(settings.mail_info['sender'],settings.mail_info['receiver'],mail_content.as_string())
        smtp.quit()

    except Exception as e:
        return e


#日志记录
def log_record(log_title,lineno,log_content):
    '''
    :param log_title:  日志标题
    :param log_content: 日志内容
    :return: 日志记录
    '''

    current_format_time = GetCurrentTime()


    #创建loger对象
    logger = settings.logging.getLogger(log_title)
    logger.setLevel(settings.log_level)

    #添加文件/屏幕日志输出对象
    log_dir = os.path.join(settings.project_root_path, 'logs', 'AutoTest_' + current_format_time.all_number_time() + '.log').replace('\\','/')
    fh = settings.logging.FileHandler(log_dir)
    # sh = config.logging.StreamHandler()
    # sh.setLevel(config.log_level)

    #设置输出log输出格式
    formatter = settings.logging.Formatter('%(asctime)s, %(levelname)s, line-' + str(lineno) + ', %(name)s: %(message)s')
    fh.setFormatter(formatter)
    # sh.setFormatter(formatter)

    #输出日志到屏幕和文件中
    logger.addHandler(fh)
    # logger.addHandler(sh)

    # 输出日志的内容
    logger.debug(log_content)
    logger.info(log_content)
    logger.warning(log_content)
    logger.error(log_content)
    logger.critical(log_content)

    logger.removeFilter(fh)
    # logger.removeHandler(sh)

    return  logger



#调用web服务,保存测试用例
def callback_test_case_info(case_info:list):
    '''
    所有用例执行完毕后将所有用例信息传给web服务，前端用来展示

    :param case_info: case_info:  每个case中的用例信息，字典形式
    :return: 回传成功
    '''
    response = requests.post(
        url=settings.web_server_test_case_host,
        json=case_info,
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
    )
    # print('上传测试用例:', response.text)

#调用web服务,保存测试报告
def  callback_test_test_report(test_report):
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
    # print('上传测试报告:',response.text)





if __name__ == '__main__':
    handel_file = HandelCaseInfoFile()
    r = handel_file.get_test_case_info()
    print(r)


