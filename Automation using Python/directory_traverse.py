from sys import *
import os

def DirectoryWatcher(path,extn):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        print("Below are file names with given extension")
        for filname in os.listdir(path):
                ext =os.path.splitext(filname)[-1].lower()
                if ext == extn:
                    print (filname)
    else:
        print("Invalid Path")


def main():

    print("Application name : " + argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to display files with extension")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory File_extension")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
