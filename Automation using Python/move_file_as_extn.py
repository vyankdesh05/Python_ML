from sys import *
import os
import shutil


def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    # create 'dynamic' dir, if it does not exist

    path1 = os.path.join(path, 'TXT')
    if not os.path.exists(path1):
        os.makedirs(path1)

    path2 = os.path.join(path, 'DOC')
    if not os.path.exists(path2):
        os.makedirs(path2)

    path3 = os.path.join(path, 'PNG')
    if not os.path.exists(path3):
        os.makedirs(path3)

    path4 = os.path.join(path, 'PDF')
    if not os.path.exists(path4):
        os.makedirs(path4)

    if exists:
        
        for foldername, subfolder, filname in os.walk(path):

            for filen in filname:
                if os.path.splitext(filen)[-1].lower() == '.txt' :
                    src = os.path.join(path, filen)
                    dest = os.path.join(path1, filen)
                    shutil.move(src, dest)
                elif os.path.splitext(filen)[-1].lower() == '.doc' :
                    src = os.path.join(path, filen)
                    dest = os.path.join(path2, filen)
                    shutil.move(src, dest)
                elif os.path.splitext(filen)[-1].lower() == '.png' :
                    src = os.path.join(path, filen)
                    dest = os.path.join(path3, filen)
                    shutil.move(src, dest)
                elif os.path.splitext(filen)[-1].lower() == '.pdf' :
                    src = os.path.join(path, filen)
                    dest = os.path.join(path4, filen)
                    shutil.move(src, dest)
                else:
                    print ("No folder exist for given extension of file:",filen)
            print(' ')

    else:
        print("Invalid Path")

def main():
    print("---- Move files dynamically to folder as per extension -----")

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

   #except Exception:
    #    print("Error : Invalid input")

if __name__ == "__main__":
    main()
