## addition of two no's

def Add(val1,val2):
    result=val1+val2
    return result

def main():
    print("Enter first no :")
    no1=int(input())

    print("Enter second no: ")
    no2=int(input())

    ret=Add(no1,no2)
    print("Addition of two numbers is :",ret)

if __name__=="__main__":
    main()