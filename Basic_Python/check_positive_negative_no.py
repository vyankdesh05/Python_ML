## To check if no is postive ,negative or zero

def ChkNo(val):
    if val>0:
        print("Given number is positive")
    elif val<0:
        print("Given number is negative")
    elif val==0:
        print("Given number is zero")
    return val

def main():
    print("Enter number to be checked :")
    no=int(input())
    ChkNo(no)

if __name__=="__main__":
    main()