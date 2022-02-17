#Display Marvellous 5 times

def Disp(j):
    for i in range(0,j):
        print("Marvellous")

def main():
    print("Enter no of times we want to print :")
    no=int(input())
    Disp(no)

if __name__=="__main__":
    main()