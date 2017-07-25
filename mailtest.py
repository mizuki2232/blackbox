# -*- coding: utf-8 -*-


import os
import smtplib


from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate


from_address = os.environ["from_address"]
to_address = os.environ["to_address"]

charset = 'ISO-2022-JP'
subject = u'件名'
text = u'本文'

# -*- coding: utf-8 -*-


import os
import smtplib


from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate


from_address = os.environ["from_address"]
to_address = os.environ["to_address"]

charset = 'ISO-2022-JP'
subject = u'件名'
text = u'本文'


def sendmail():
    msg = MIMEText(text.encode(charset), 'plain', charset)
    msg['Subject'] = Header(subject, charset)
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Date'] = formatdate(localtime=True)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(from_address, os.environ["passwd"])
    smtp.sendmail(from_address, to_address, msg.as_string())
    smtp.quit()


sendmail()
