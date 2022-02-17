## accept one no and return power of two

def main():
    print ("Enter number: ")
    no=int(input())

    ans=lambda no:2**no

    ret=ans(no)

    print ("Power of given number is :",ret)

if __name__=="__main__":
    main()