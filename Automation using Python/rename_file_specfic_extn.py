from sys import *
import os

def DirectoryWatcher(path,extn1,extn2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for filname in os.listdir(path):
            print (path)
            print (filname)
            base = os.path.splitext(filname)[0]
            print(base)
            ext = os.path.splitext(filname)[-1].lower()
            print(ext)
            if ext == extn1:
                os.chdir(path)
                new_file=os.rename(filname,(base + extn2))
                print ("File has been renamed with extension",extn2)


    else:
        print("Invalid Path")


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
        DirectoryWatcher(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
