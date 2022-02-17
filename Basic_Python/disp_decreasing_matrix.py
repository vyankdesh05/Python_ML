#print n by n-1...n-(n-1) matrix

def Disp(row):
    for i in range(0, (row)):
        j = 0
        while (j != (row - 1)):
            print(end='* ')
            j = j + 1
        print('*', )
        row=row-1

def main():
    print("Enter no of row: ")
    no=int(input())

    Disp(no)

if __name__=="__main__":
    main()

0