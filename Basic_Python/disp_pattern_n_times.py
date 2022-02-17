#To print * n no of times on screen. Take n from input

def Prnt(j):
    for i in range (0,j):
        print("*")

def main():
    print("Enter number of times * to be printed :")
    no=int(input())
    Prnt(no)

if __name__=="__main__":
    main()