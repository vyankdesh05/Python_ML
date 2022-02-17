#print n by n matrix of *

def Disp(row):
    for i in range (0,(row)):
        j=0
        while (j != (row-1)):
            print(end ='* ')
            j=j+1
        print('*',)

def main():
    print("Enter no of row: ")
    no=int(input())

    Disp(no)

if __name__=="__main__":
    main()
