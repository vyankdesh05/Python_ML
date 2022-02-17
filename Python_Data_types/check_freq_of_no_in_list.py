#To check Frequency of given number in list

def main():
    size=0
    Data = []
    print("Enter how many elements you want ? :")
    size=int(input())

    print("Enter no of elements: ")
    for i in range(0,size):
        Data.append(int(input()))
    print ("Data is : ",Data)

    print ("Enter number to be searched :")
    no=int(input())

    count=0
    for i in range(len(Data)):
       if Data[i]==no:
           count=count+1

    print ("Frequency of given number in list is :",count)

if __name__=="__main__":
    main()