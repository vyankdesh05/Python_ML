#program to display 10 to 1 like 10,9,8...1

def Disp(j,k,l):
    for i in range(j,k,l):
        print(i)

def main():
    print("Enter starting no :")
    no1=int(input())

    print("Enter ending no : ")
    no2=int(input())

    print("Enter increment factor : ")
    no3=int(input())

    Disp(no1,no2,no3)

if __name__=="__main__":
    main()