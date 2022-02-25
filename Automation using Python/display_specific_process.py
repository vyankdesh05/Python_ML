import psutil
import re
from sys import *


def DispProc(App):
    proclist = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            for key, value in pinfo.items():
                if key == 'name':
                    if re.match(App, value):
                        proclist.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return proclist


def main():
    print("---- Display information about specific process -----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        print ("Try -h / -u option to get more details")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to display information about specific process")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName Process_name/pattern")
        exit()

    ret = DispProc(argv[1])
    print("Below are the process information for given process")
    for name in ret:
        print(name)


if __name__ == "__main__":
    main()
