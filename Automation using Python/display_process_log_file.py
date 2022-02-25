import psutil
import re
from sys import *
import os
import time
import datetime

def DispProc(path):

    exists = os.path.isdir(path)
    if not exists:
        os.mkdir(path)
    else:
        print ("Path already exist")

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    file='project_log_file_'+str(nowTime)+'.log'
    fd=os.path.join(path,file)
    log_file=open(fd, 'w')

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

def main():

    print("---- Display information about specific process -----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to display information about specific process")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName folder_name")
        exit()

    DispProc(argv[1])


if __name__ == "__main__":
    main()
