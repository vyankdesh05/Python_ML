from functools import reduce

def CheckEven(no):
    if (no % 2==0):
        return True
    else:
        return False
def Incr(no):
    return no+2

def Add(a,b):
    return a+b

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