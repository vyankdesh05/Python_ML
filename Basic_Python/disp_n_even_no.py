#Display first 10 even no's on screen

def Disp(j,k,l):
    for i in range(j,k,l):
        if (i%2==0):
            print(i)
            if (i==20):
                break

def main():
    print("Enter starting number :")
    no=int(input())

    print("Enter ending number : ")
    no1=int(input())

    print("Enter increment factor: ")
    no2=int(input())

    Disp(no,no1,no2)

if __name__=="__main__":
    main()