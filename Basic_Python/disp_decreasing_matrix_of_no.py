#print n by n matrix of numbers like below
#1 2 3
#1 2
#1

def Disp(row):
    for i in range (1,(row)):
        j=1
        while (j != (i+1)):
            print(j,end =' ')
            j=j+1
        print(j,' ')
        row=row+1

def main():
    print("Enter no of row: ")
    no=int(input())

    Disp(no)

if __name__=="__main__":
    main()