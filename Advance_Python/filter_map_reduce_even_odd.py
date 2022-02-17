from functools import reduce

CheckEven= lambda no:(no % 2==0)

Sqr=lambda no:no*no

Add=lambda a,b:a+b

def main():
    data = []
    print("enter no of elements:")
    no1 = int(input())
    for i in range(0, no1):
        print("Enter number:")
        val = int(input())
        data.append(val)

    print ("Original data is:",data)
    newdata=list(filter(CheckEven,data))

    print ("Even data list is: ",newdata)

    mapdata=list(map(Sqr,newdata))
    print("Mapped data is: ",mapdata)

    reddata = reduce(Add, mapdata)
    print("Reduced data is: ", reddata)

if __name__=="__main__":
    main()
