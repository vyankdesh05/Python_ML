from sys import *
import os
import re
import subprocess

def Find(string):
    App=re.findall(r'[A-Z]:.*\.exe$',string)
    return App

def Proc_launch(file):
    with open(file) as fp:
        for line in fp:
            App=Find(line)
            for str in App:
                subprocess.Popen(str,shell=True)

def main():
    print("---- Process launcher-----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to launch processes ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName File_having_list_of_process")
        exit()

    try:
        Proc_launch(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
