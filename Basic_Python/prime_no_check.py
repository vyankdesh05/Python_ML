## To check if given no is prime or not 17 19 29

def ChkPrime(no):
    if no > 10:
        if (no % 2 == 0) or (no % 3 == 0) or (no % 5 == 0):
            print("Number is not prime")
        else:
            print("Number is prime")
    elif no < 10:
        if no==2 or no==3 or no==5 or no==7:
            print ("Number is prime")
        else:
            print ("Number is not prime")

def main():
    print ("Enter number :")
    val=int(input())
    ChkPrime(val)

if __name__=="__main__":
    main()