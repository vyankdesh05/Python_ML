from sys import *
import os
import hashlib

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    file_dir=dict()
    List=[]
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                print("File inside "+foldername+"is : "+filen)
                os.chdir(path)
                f_name = open(filen, "rb")
                Data = f_name.read()
                Hash_val = hashlib.md5(Data).hexdigest()
                if Hash_val in file_dir:
                    List.append(filen)
                else:
                    file_dir.update({Hash_val:filen})
            print ("Duplicate file names are written in Log.txt in same folder")
            fd = open("Log.txt", "a")
            fd.write("Below are duplicate file are deleted from folder\n")
            for i in range(len(List)):
                print(List[i])
                Val=(List[i])
                fd.write(Val)
                fd.write("\n")
                os.remove(Val)
            fd.close()

    else:
        print("Invalid Path")

def main():
    print("---- Duplicate file deletion from folder-----")

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
