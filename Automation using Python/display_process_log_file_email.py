import psutil
import re
from sys import *
import os
import time
import datetime
import shutil

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def DispProc(path,email_id):

    exists = os.path.isdir(path)
    if not exists:
        os.mkdir(path)
    else:
        print ("Path already exist")

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    file='project_log_file_'+str(nowTime)+'.log'
    fd=os.path.join(path,file)
    log_file=open(fd, 'w+')

    header="*" * 80
    curr_time=datetime.datetime.now()

    log_file.write(header+"\n")
    log_file.write("Log file of the project created at" + " " + str(curr_time) + "\n")
    log_file.write(header + "\n")


    proclist=[]
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            proclist.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    for row in proclist:
        log_file.write(str(row)+"\n")
    row_count=len(proclist)
    log_file.write(header + "\n")
    log_file.write("Current process count is : "+ str(row_count) + "\n")
    log_file.write(header + "\n")
    log_file.close()
    #shutil.copyfile(log_file,file_1)

    print ("log file name ",log_file)

    fromaddr = email_id
    toaddr = "supriyakale100@gmail.com"

    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Log file of the project"

    # string to store the body of the mail
    body = "Body_of_the_mail"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent


    attachment = open(os.path.join(path, file), "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % file)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "deshp@nd3")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

def main():

    print("---- Display information about specific process -----")

    print("Application name : " + argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to display information about specific process")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName folder_name")
        exit()

    DispProc(argv[1],argv[2])


if __name__ == "__main__":
    main()
