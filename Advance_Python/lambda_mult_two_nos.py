## accept two no and return it's multiplication

def main():
    print ("Enter first number: ")
    a=int(input())

    print("Enter second number: ")
    b = int(input())

    ans=lambda a,b:a*b

    ret=ans(a,b)

    print ("Multiplication of given numbers is :",ret)

if __name__=="__main__":
    main()