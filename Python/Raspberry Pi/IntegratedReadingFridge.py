# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:10:14 2018

@author: Pinlei
"""

import numpy as np
from decimal import Decimal
import struct
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from datetime import datetime

string_list=["LineSize(bytes)", "LineNumber", "Time(secs)", "P2 Condense (Bar)", "P1 Tank (Bar)", "P5 ForepumpBack (Bar)", "P3 Still (mBar)", "P4 TurboBack (mBar)", "Dewar (mBar)", "Input Water Temp", "Output Water Temp", "Helium Temp", "Oil Temp", "Motor Current", "Low Pressure", "High Pressure", "PT2 Head t(s)", "PT2 Head T(K)", "PT2 Head R(Ohm)", "PT2 Plate t(s)", "PT2 Plate T(K)", "PT2 Plate R(Ohm)", "Still Plate t(s)", "Still Plate T(K)", "Still Plate R(Ohm)", "100mK Plate t(s)", "100mK Plate T(K)", "100mK Plate R(Ohm)", "MC Plate Cernox t(s)", "MC Plate Cernox T(K)", "MC Plate Cernox R(Ohm)", "PT1 Head t(s)", "PT1 Head T(K)", "PT1 Head R(Ohm)", "PT1 Plate t(s)", "PT1 Plate T(K)", "PT1 Plate R(Ohm)", "MC Plate RuO2 t(s)", "MC Plate RuO2 T(K)", "MC Plate RuO2 R(Ohm)", "chan[8] t(s)", "chan[8] T(K)", "chan[8] R(Ohm)", "chan[9] t(s)", "chan[9] T(K)", "chan[9] R(Ohm)", "chan[10] t(s)", "chan[10] T(K)", "chan[10] R(Ohm)", "chan[11] t(s)", "chan[11] T(K)", "chan[11] R(Ohm)", "chan[12] t(s)", "chan[12] T(K)", "chan[12] R(Ohm)", "Still heater (W)", "chamber heater (W)", "IVC sorb heater (W)", "turbo current(A)", "turbo power(W)", "turbo speed(Hz)", "turbo motor(C)", "turbo bottom(C)"]
def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
    return struct.unpack('>d', bf)[0]

def int_to_bytes(n, minlen=0):  # Helper function
    nbits = n.bit_length() + (1 if n < 0 else 0)  # +1 for any sign bit.
    nbytes = (nbits+7) // 8  # Number of whole bytes.
    b = bytearray()
    for _ in range(nbytes):
        b.append(n & 0xff)
        n >>= 8
    if minlen and len(b) < minlen: 
        b.extend([0] * (minlen-len(b)))
    return bytearray(reversed(b))  # High bytes first.

def send_email(receiver, content_text):
    mail_host="smtp.gmail.com" 
    mail_user="HatlabOxford@gmail.com" 
    mail_pass="Jpccool@pitt"

    sender = 'Hatlab_Oxford@gmail.com'
    receivers = [receiver]

    message = MIMEText(content_text, 'plain', 'utf-8')
    message['From'] = Header("Hatlab_Oxford", 'utf-8')
    subject = 'Oxford Daily Report'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 587)
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "Succeed!!!"
        smtpObj.quit()
    except smtplib.SMTPException:
        raise
    
def read_log(filename):
    """
    Return the lastest value of log file
    """
    file_ = open(filename, "rb")
    read = file_.read()
    data = read[12288:]
    data_list = np.zeros(63)
    for j in range(63):
        double_float = ""
        for i in range(8):
            digit = 7-i
            temp = np.binary_repr(ord(data[-1008:-504][8*j + digit]), 8)
            double_float+=temp
        data_list[j] = bin_to_float(double_float)
    return data_list

def generate_content(data_list):
    content = "Dear All," + "\n" + "    This is the daily status of the Oxford Fridge, if you have any question, please contact ..." + "\n"
    for i in range(63):
        if i==2: # time conversion
            content += string_list[i] + " : " + datetime.fromtimestamp(data_list[i]).strftime("%A, %B %d, %Y %I:%M:%S") + "\n"
        else:
            content += string_list[i] + " : " + str(data_list[i]) + "\n"
    content += "Powered by Pinlei and Chao from Hatlab"
    return content
    
filename = "C:\Users\zctid.LAPTOP-150KME16\Desktop\\test.vcl"#raw_input('Please Input filename:')
receiver = "zctide@live.com"#raw_input('Please Input the email address you want to send in:')





while True:
    data_list = read_log(filename)
    if data_list[38]*1000>30:
        print "!!!!!!!Fridge is Burning!!!!!!!!\n","MC Plate RuO2 T(mK) :", data_list[38]*1000,"\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        content = generate_content(data_list)
        send_email(receiver, content)
        break
    else:
        print "MC Plate RuO2 T(mK):", data_list[38]*1000
    time.sleep(30)


