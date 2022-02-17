#To check if no is even or odd

def ChkNum(val):
    if (val%2==0):
        print("Number is even number")
    else:
        print("Number is odd number")
    return val

def main():
    print("Enter number to check even/odd :")
    no=int(input())
    ChkNum(no)

if __name__=="__main__":
    main()