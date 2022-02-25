from sys import *
import os
import hashlib

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    Dir=dict()
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                #print("File inside "+foldername+"is : "+filen)
                os.chdir(path)
                size=os.path.getsize(filen)
                size_in_kb=size/1024
                Dir.update({size_in_kb:filen})
                print ('File size of {} file is {} KB'.format(filen,size_in_kb))
                #max_val=max()
            for key,value in Dir.items():
                if key== max(Dir):
                    print("File of maximum size is :",value)
            #print(Dir.items())

    else:
        print("Invalid Path")

def main():
    print("---- Display file having maximum size from folder -----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
