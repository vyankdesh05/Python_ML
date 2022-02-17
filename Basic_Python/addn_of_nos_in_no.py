## To print addition of numbers in given number

def AddNo(val):
    l=len(val)
    ret=0
    for i in range (0,l):
        ret = ret + int(str(val)[i])
    print ("Addition of number is: ",ret)

def main():
    print("Enter number :")
    no=input()
    AddNo(no)

if __name__=="__main__":
    main()
