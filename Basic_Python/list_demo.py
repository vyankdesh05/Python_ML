def Addtion(val):
    sum=0
    for i in range(len(val)):
        sum=sum+val[i]
    return sum

def main():
    size=0
    Data = []
    print("Enter how many elements you want ? :")
    size=int(input())

    print("enter no of elements: ")
    for i in range(0,size):
        Data.append(int(input()))
    print ("Data is : ",Data)

    ret=Addtion(Data)
    print ("Addition is :",ret)

if __name__=="__main__":
    main()