def Addition(no1,no2): ##### postional arguments
    Ans=0
    Ans=no1+no2
    return Ans

def main():
    print ("Enter first number: ")
    val1=int(input())

    print ("Enter second number :")
    val2=int(input())

    #ret=Addition(val1,val2) ##### postional arguments
    ret = Addition(no1=val1, no2=val2) ## keyword arguments
    print ("Addition is :",ret)

if __name__=="__main__":
    main()