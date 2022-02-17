
def Division(a,b):
    return a/b

def Deco(c,d):
    if c > d:
        ans=Division(c,d)
        return ans
    else:
        c,d=d,c
        ans=Division(c,d)
        return ans

def main():
    no1=int(input("enter value of a: "))
    no2=int(input("enter value of b: "))

    ret=Deco(no1,no2)

    print ("Division is:",ret)

    
if __name__=="__main__":
    main()