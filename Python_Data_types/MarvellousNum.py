## To check if given no is prime or not 17 19 29

def ChkPrime(no):
    ret=0
    if no > 10:
        if (no % 2 == 0) or (no % 3 == 0) or (no % 5 == 0):
            print("Number is not prime")
        else:
            ret=no

    elif no < 10:
        if no==2 or no==3 or no==5 or no==7:
            print ("Number is prime")
            ret=no
    return ret

