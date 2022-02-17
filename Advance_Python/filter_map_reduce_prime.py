from functools import reduce

def ChkPrime(no):
    if no > 10:
        if (no % 2 == 0) or (no % 3 == 0) or (no % 5 == 0) or (no % 7 ==0):
            return False
        else:
            return True

    elif no < 10:
        if no==2 or no==3 or no==5 or no==7:
            return True
        else:
            return False

Mult=lambda no:no*2


def main():
    data = []
    print("enter no of elements:")
    no1 = int(input())
    for i in range(0, no1):
        print("Enter number:")
        val = int(input())
        data.append(val)

    print ("Original data is:",data)
    newdata=list(filter(ChkPrime,data))

    print ("Prime number list is: ",newdata)

    mapdata=list(map(Mult,newdata))
    print("Mapped data is: ",mapdata)

    ret = reduce(max,mapdata)
    print("Reduced data is: ", ret)

if __name__=="__main__":
    main()