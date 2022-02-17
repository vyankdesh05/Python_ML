class Numbers:

    def __init__(self,A):
        self.no=A

    def ChkPrime(self):
        if self.no >= 10:
            if (self.no)%2 == 0 or (self.no)%3 == 0 or (self.no)%5 == 0 or (self.no)%7 == 0:
                print ("Given number IS NOT Prime")
            else:
                print ("Given number IS Prime")
        else:
            if self.no==2 or self.no==3 or self.no==5 or self.no==7:
                print ("Given number IS Prime")
            else:
                print ("Given number is NOT Prime")


    def ChkPerfect(self):
        self.sum=0
        for i in range(1,self.no):
            if (self.no) % i == 0:
                self.sum=i+self.sum
        print(self.sum)
        if self.sum==self.no:
            print("Given number is perfect")
        else:
            print("Given number is NOT perfect")


    def Factors(self):
        print ("Factors of given number:",end=' ')
        for i in range(1, self.no):
           if (self.no) % i == 0:
               print(i,end=' ')
        print (" ")

    def SumFactors(self):
        self.sum = 0
        for i in range(1, self.no):
            if (self.no) % i == 0:
               self.sum = i + self.sum
        print("Sum of all factors of given number is:",self.sum)


def main():
    print ("Enter number to be checked:")
    val=int(input())
    obj=Numbers(val)
    obj.ChkPrime()
    obj.ChkPerfect()
    obj.Factors()
    obj.SumFactors()

if __name__=="__main__":
    main()