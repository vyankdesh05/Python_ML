from sys import *
import os
import shutil

def DirectoryWatcher(dir1,dir2,extn):
    flag = os.path.isabs(dir1)
    if flag == False:
        dir1 = os.path.abspath(dir1)

    #exists = os.path.isdir(dir1)
    os.mkdir(dir2)
    dir2 = os.path.abspath(dir2)
    print ("File copying started...")



    for file in os.listdir(dir1):
        ext = os.path.splitext(file)[-1].lower()
        if ext==extn:
            src=os.path.join(dir1,file)
            dest=os.path.join(dir2,file)
            shutil.copyfile(src,dest)
            print ("File copied is :",file)
    print ("All files are copied to folder ",dir2)

def main():
    print("Application name : " + argv[0])

    if (len(argv) != 4):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory File_extension")
        exit()

    try:
        DirectoryWatcher(argv[1], argv[2],argv[3])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
