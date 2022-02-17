
def Division(a,b):
    return a/b

def Deco(func_name):
    def Inner(c,d):
        if c < d:
            c,d=d,c ##

        return func_name(c,d)
    return Inner

Division=Deco(Division) #### Division= Deco(original divisio)

def main():
    no1=int(input("enter value of a: "))
    no2=int(input("enter value of b: "))

    ret=Division(no1,no2) ###ret=NEw division(2,10)

    print ("Division is:",ret)

if __name__=="__main__":
    main()