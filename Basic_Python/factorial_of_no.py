## To print factorial of no like 4!=4 * (4-1) * (4-2) * (4-3)

def Disp(val):
    j = 1
    op = 1
    while (j != (val + 1)):
        op = op * val
        val = val - 1
    print ("Factorial of number is :",op)

def main():
    print ("Enter number :")
    no=int(input())
    Disp(no)

if __name__=="__main__":
    main()
