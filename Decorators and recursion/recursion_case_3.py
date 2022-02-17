
def DispR(i,j):
    if i>0:
        print(j,end=' ')
        i-=1
        j-=1
        DispR(i,j)

def main():
    Iter=int(input("Enter no of iterations:"))
    Iter1=Iter
    DispR(Iter,Iter1)

if __name__=="__main__":
    main()