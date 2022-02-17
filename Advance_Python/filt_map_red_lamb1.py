from functools import reduce

def main():

    data=[5,7,6,8,4]
    print ("Original data is:",data)
    newdata=list(filter(lambda no:(no % 2==0),data))

    print ("Even data list is: ",newdata)

    mapdata=list(map(lambda no:no+2,newdata))
    print("Mapped data is: ",mapdata)

    reddata = reduce(lambda a,b:a+b, mapdata)
    print("Reduced data is: ", reddata)

if __name__=="__main__":
    main()

 #print ("enter no of elements")
    #no=int(input())
    #for i in range (0,no)
    #data.