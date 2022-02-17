from functools import reduce

CheckNo= lambda no:(no>=70 and no<=90)

Incr=lambda no:no+10

Mult=lambda a,b:a*b

def main():

    data=[]
    print ("enter no of elements")
    no1=int(input())
    for i in range (0,no1):
        print ("Enter number:")
        val=int(input())
        data.append(val)

    print ("Original data is:",data)
    newdata=list(filter(CheckNo,data))

    print ("Filtered data list is: ",newdata)

    mapdata=list(map(Incr,newdata))
    print("Mapped data list is: ",mapdata)

    reddata = reduce(Mult, mapdata)
    print("Reduced data is: ", reddata)

if __name__=="__main__":
    main()

