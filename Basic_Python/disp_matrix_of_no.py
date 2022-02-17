#print n by n matrix of numbers
#1 2 3
#1 2 3
#1 2 3

def Disp(row):
    for i in range (0,(row)):
        j=1
        while (j != (row)):
            print(j,end =' ')
            j=j+1
        print(j,' ')

def main():
    print("Enter no of row: ")
    no=int(input())

    Disp(no)

if __name__=="__main__":
    main()