#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# Third-party SMTP service
mail_host = "smtp.XXX.com"  # Set the server
mail_user = "XXXX"  # Username
mail_pass = "XXXXXX"  # Password

sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # Receive email, you can set it to your QQ email or other email

message = MIMEText('Python email sending test...', 'plain', 'utf-8')
message['From'] = Header("Tutorial", 'utf-8')
message['To'] = Header("Test", 'utf-8')

subject = 'Python SMTP email test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 is the SMTP port number
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print
    "Email sent successfully"
except smtplib.SMTPException:
    print
    "Error: Unable to send email"
