#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import smtplib
import time


from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate


import cv2
import boto3

config_json = open('json/config.json', 'r')
config = json.load(config_json)


for attr in config.get("list"):
    if attr.get("id") == "Watch_Object":
        object = attr.get("body")
    elif attr.get("id") == "Desired_Count":
        desired_count = attr.get("body")
    elif attr.get("id") == "Desired_Wait_time":
        desired_wait_time = attr.get("body")
    elif attr.get("id") == "Desired_Mail_Address":
        to_address = attr.get("body")
    elif attr.get("id") == "bucket_name":
        bucket_name = attr.get("body")
    elif attr.get("id") == "from_address":
        from_address = attr.get("body")
    elif attr.get("id") == "mail_subject":
        subject = attr.get("body")
    elif attr.get("id") == "mail_text":
        text = attr.get("body")
    elif attr.get("id") == "passwd":
        passwd = attr.get("body")
    else:
        pass


client = boto3.client('rekognition')
s3 = boto3.resource('s3')

count = 0

charset = 'ISO-2022-JP'  # replace with environment varialbe later


def sendmail():
    msg = MIMEText(text.encode(charset), 'plain', charset)
    msg['Subject'] = Header(subject, charset)
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Date'] = formatdate(localtime=True)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(from_address, passwd)
    smtp.sendmail(from_address, to_address, msg.as_string())
    smtp.quit()


# getserial() works well in Raspberry pi
def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


identity = getserial()
capture_image = identity

if __name__ == "__main__":

    while True:

        time.sleep(desired_wait_time)
        print("take picture...")
        c = cv2.VideoCapture(0)
        r, img = c.read()
        cv2.imwrite('./' + capture_image , img)
        c.release()
        print("uploading to S3...")
        s3.Bucket(bucket_name).upload_file('./' + capture_image , capture_image)
        # rekognition
        print("analize image by rekognition...")
        response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': capture_image
            }
        },
        MaxLabels=123,
        MinConfidence=10,
        )

        print("")
        print("============Rekognition Response=================")
        print(response)
        print("=================================================")
        print("")

        for i in response['Labels']:
            if i['Confidence'] > 12:

                print("")
                print("==============Detected Thing====================")
                print(i['Name'])
                print("=================================================")
                print("")

                if i['Name'] == object:
                    print("Desired object [" + object + "] is Detected.")

                    count += 1
                    if count == desired_count:
                        try:
                            print("Send mail!")
                            sendmail()
                            print("reset count")
                            count = 0

                        except KeyboardInterrupt:
                            pass
