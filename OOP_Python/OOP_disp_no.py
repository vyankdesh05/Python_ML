class Demo:

    def __init__(self,a,b):
        self.no1=a
        self.no2=b

    def fun(self):
        print (self.no1)

    def gun(self):
        print(self.no2)

def main():
    print ("Enter first number for first object:")
    val1=int(input())

    print ("Enter second number for first object:")
    val2=int(input())

    obj1=Demo(val1,val2)
    print ("Value of first number in class is:",obj1.no1)
    print("Value of second number in class is:", obj1.no2)

    print("Enter first number for first object:")
    val3 = int(input())

    print("Enter second number for first object:")
    val4 = int(input())

    obj2=Demo(val3,val4)
    print("Value of first number in class is:", obj2.no1)
    print("Value of second number in class is:", obj2.no2)

    print("Value of first number in object 1 is:")
    obj1.fun()

    print("Value of first number in object 2 is:")
    obj2.fun()

    print("Value of second number in object 1 is:")
    obj1.gun()

    print("Value of second number in object 2 is:")
    obj2.gun()

if __name__=="__main__":
    main()



