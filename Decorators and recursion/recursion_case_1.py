
def DispR(i):
    if i>0:
        print ("*",end=' ')
        i=i-1
        DispR(i)

def main():
    Iter=int(input("Enter no of iterations:"))
    DispR(Iter)

if __name__=="__main__":
    main()