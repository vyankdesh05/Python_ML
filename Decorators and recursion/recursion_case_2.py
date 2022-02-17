
j=1
def DispR(i):
    global j
    if i>0:
        print(j,end=' ')
        i-=1
        j+=1
        DispR(i)

def main():
    Iter=int(input("Enter no of iterations:"))
    DispR(Iter)

if __name__=="__main__":
    main()