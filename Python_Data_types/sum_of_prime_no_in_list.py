# to get sum of prime numbers in list

import MarvellousNum

def ListPrime(val):
    sum=0
    for i in range(len(val)):
        j=MarvellousNum.ChkPrime(val[i])
        sum = sum + j
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

    ret=ListPrime(Data)
    print ("Addition of prime numbers in list is :",ret)

if __name__=="__main__":
    main()