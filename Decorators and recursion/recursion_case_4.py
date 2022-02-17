j=1
Add=0
def DispR(i):
    global Add,j
    Len=len(i)
    k=Len-j

    if k >= 0:
        Add = Add + int(i[k])
        j+=1
        DispR(i)

    return Add

def main():
    No=input("Enter number of your choice:")
    ret=DispR(No)
    print ("Addition of all digits is: ",ret)

if __name__=="__main__":
    main()