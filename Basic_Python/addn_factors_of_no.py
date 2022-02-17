## To accept one number form user and return addition of its factors.

def Calc(val):
    ret = 0
    for i in range(2, (val + 1)):
        if ((val % i) == 0):
            val1 = val / i
            print(val1)
            ret = val1 + ret
    return ret

def main():
    print ("Enter number :")
    no=int(input())
    addn=Calc(no)
    print ("Addition of factors is :",addn)

if __name__=="__main__":
    main()
