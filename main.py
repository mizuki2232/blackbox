#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import cv2
import os
import sys
import smtplib
import time


from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate


bucket_name = os.environ["bucket_name"]
client = boto3.client('rekognition')
s3 = boto3.resource('s3')

object = os.environ["object_name"]
desired_count = os.environ["desired_count"]
cpuserial = getserial()
capture_image = cpuserial
count = 0
object = os.environ["object_name"]
desired_count = os.environ["desired_count"]

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

    smtp = smtplib.SMTP()
    smtp.connect()
    smtp.sendmail(from_address, to_address, msg.as_string())
    smtp.close()


def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial = line[10:26]
        f.close()
    except:
      cpuserial = "ERROR000000000"

    return cpuserial


if __name__ == "__main__":

    while True:

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
                    print("Desired object [" + object  + "] is Detected.")

                    count += 1
                    if count == disired_count:
                        try:
                            print("Send mail!")
                            """send mail"""
                            print("reset count")
                            count = 0

                        except KeyboardInterrupt:
                            pass


        time.sleep(1.5)
