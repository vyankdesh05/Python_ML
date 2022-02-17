
Fact=1

def DispR(i):
    global Fact

    if i > 0:
        Fact = Fact * i
        i-=1
        DispR(i)

    return Fact

def main():
    No=int(input("Enter number of your choice:"))
    ret=DispR(No)
    print ("Factorial of given number is: ",ret)

if __name__=="__main__":
    main()