# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:43:48 2023

@author: karie
"""

import hashlib
import smtplib

from email.message import EmailMessage

print("Hello and welcome to Karien's File Integrity Monitor. Enter the file path of the file you wish to monitor.\n\n")

file_path = input("Enter file path (ex. /home/downloads/sensitivefiles/):\n")

usr_email = input("Enter your email:\n")

usr_passwd = input("Enter the password to your email:\n")

print("Ensure thaT 2 factor authentication is enabled")

def get_hash(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        hash = file.read()
        md5.update(hash)
        return md5.hexdigest()
    
def send_email():
    message = EmailMessage()
    message.set_content(" ")
    message['subject'] = "Someone edited one of your files on your computer"
    message['from'] = usr_email
    message['to'] = usr_email   
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(usr_email, usr_passwd)
    server.send_message(message)
    server.quit()

baseline = get_hash(file_path)
print("[+] Just calculated your baseline")
print('[+] Checking')

while True:
    check = get_hash(file_path)
    if check != baseline:
        send_email()
        print("[+] Someone edited your file")
        baseline = check










