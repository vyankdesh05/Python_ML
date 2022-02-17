#To check if no is divisable by 5

def ChkNo(val):
    if (val%5==0):
        print ("Entered number is divisable by 5")
    else:
        print("Entered number is not divisable by 5")
    return val

def main():
    print ("Enter number to be checked")
    no=int(input())
    ChkNo(no)

if __name__=="__main__":
    main()