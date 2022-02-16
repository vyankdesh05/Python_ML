from sys import *
import os
import hashlib
import time
import DupFile
import send_email

def main():
    print("---- Duplicate file deletion + print execution time-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DupFile.DirectoryWatcher(argv[1])
        print ("Send email start")
        send_email.DispProc(argv[1],argv[2])
        print("Send email ends")

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__ == "__main__":
    print ("Script execution started .....")
    starttime = time.time()
    main()
    endtime=time.time()
    print ("Script ended successfully ....")
    print('Execution time required by script is {} seconds'.format(endtime - starttime))
