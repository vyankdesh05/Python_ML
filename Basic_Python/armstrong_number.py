## 370= 3*3*3 + 7*7*7

def main():
    no=input("Enter number: ")
    print (no[0])
    Sum=0
    for i in range (len(no)):
        c=int((no[i]))
        d=c*c*c
        Sum=Sum+d
    print(Sum)
    if int(no)==Sum:
        print ("number is armstrong")
    else:
        print ("number is not armstrong")

if __name__=="__main__":
    main()