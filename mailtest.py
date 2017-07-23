# -*- coding: utf-8 -*-


import smtplib


from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate


from_address = "yabai@com"
to_address = "mizuki255@gmail.com"

charset = 'ISO-2022-JP'
subject = u'件名'
text = u'本文'


def sendmail():
    msg = MIMEText(text.encode(charset), 'plain', charset)
    msg['Subject'] = Header(subject, charset)
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Date'] = formatdate(localtime=True)

    smtp = smtplib.SMTP('localhost')
    smtp.connect()
    smtp.sendmail(from_address, to_address, msg.as_string())
    smtp.close()

sendmail()
