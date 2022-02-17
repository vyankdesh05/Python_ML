from functools import reduce

CheckEven= lambda no:(no % 2==0)

Incr=lambda no:no+2

Add=lambda a,b:a+b

def main():

    data=[5,7,6,8,4]
    print ("Original data is:",data)
    newdata=list(filter(CheckEven,data))

    print ("Even data list is: ",newdata)

    mapdata=list(map(Incr,newdata))
    print("Mapped data is: ",mapdata)

    reddata = reduce(Add, mapdata)
    print("Reduced data is: ", reddata)

if __name__=="__main__":
    main()

 #print ("enter no of elements")
    #no=int(input())
    #for i in range (0,no)
    #data.