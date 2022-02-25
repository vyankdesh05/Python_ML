from sys import *
import os
import shutil

def DirectoryWatcher(path,path1):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        print(os.path.abspath(path))
    exists = os.path.isdir(path)

    #path1="\Users\ManSup\PycharmProjects\pythonProject1\23_Jan\Demo1\"
    path1=os.path.abspath(path1)
    print (path1)
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                #print("File inside "+foldername+"is : "+filen)
                #os.chdir(path)
                src = os.path.join(path, filen)
                dest = os.path.join(path1, filen)
                print(src)
                print (dest)
                shutil.move(src,dest)
    else:
        print("Invalid Path")

def main():
    print("---- Move files from one to another folder -----")

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
        DirectoryWatcher(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
