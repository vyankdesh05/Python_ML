from sys import *
import os
import shutil

def DirectoryWatcher(path,path1):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        print(os.path.abspath(path))
    exists = os.path.isdir(path)
    if not os.path.isdir(path1):
        os.mkdir(path1)
    os.rename(path1,TXT)
    dir2 = os.path.abspath(dir2)

    #path1="\Users\ManSup\PycharmProjects\pythonProject1\23_Jan\Demo1\"
    path1=os.path.abspath(path1)
    print (path1)
    Base=[]
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:

                base = os.path.splitext(filen)[0]
                ext = os.path.splitext(filen)[-1].lower()
                Base.append(ext)

                print(ext)
            print(Base)
            Base1=set(Base)
            print (Base1)
            Base2=list(Base1)
            print (Base2[0])

            for file1 in filname:
                #print("File inside "+foldername+"is : "+filen)
                #os.chdir(path)
                src = os.path.join(path, file1)
                dest = os.path.join(path1, file1)
                print(src)
                print(dest)
                if os.path.splitext(file1)[-1].lower() == Base2[0] :
                    shutil.move(src, dest)
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

    #except Exception:
     #   print("Error : Invalid input")

if __name__ == "__main__":
    main()
