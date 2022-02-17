#To find minimum number in list

def main():
    size=0
    Data = []
    print("Enter how many elements you want ? :")
    size=int(input())

    print("enter no of elements: ")
    for i in range(0,size):
        Data.append(int(input()))
    print ("Data is : ",Data)

    ret=min(Data)
    print ("Minimum number in list is :",ret)

if __name__=="__main__":
    main()