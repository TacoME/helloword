#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# ������ SMTP ����
mail_host="smtp.qq.com"  #���÷�����
mail_user="1131617381@qq.com"    #�û���
mail_pass=""   #���� 
 
 
sender = '1131617381@qq.com'
receivers = ['1131617381@qq.com']  # �����ʼ���������Ϊ���QQ���������������
 
message = MIMEText('Python mail send... this is a good job', 'plain', 'utf-8')
message['From'] = Header("Andy", 'utf-8')
message['To'] =  Header("ToAndy", 'utf-8')
 
subject = 'happy new year'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
    #smtpObj.connect(mail_host, 465)    # 25 Ϊ SMTP �˿ں�
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print "send OK"
except smtplib.SMTPException,e:
    print "Error: can not send,%s"%e
