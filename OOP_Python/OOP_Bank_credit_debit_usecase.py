class BankAccount:
    ROI=10.5

    def __init__(self,N,AD,W):
        self.Name=N
        self.Depos=AD
        self.WDraw=W
        self.Amount=1000

    def Display(self):
        print ("Name of customer is:",self.Name)
        print ("Amount entered is:",self.Amount)

    def Deposit(self):
        self.Depos=self.Amount + self.Depos
        return self.Depos

    def Withdraw(self):
        self.WDraw=self.Depos-self.WDraw
        return self.WDraw

    def CalculateIntrest(self):
        IntAmt=((self.Depos*BankAccount.ROI)/100)
        return IntAmt

def main():

    N1=input("Enter name of customer:")
    print("Enter amount to be deposited :")
    A1=int(input())

    print("Enter amount to be withdraw :")
    W1=int(input())

    obj=BankAccount(N1,A1,W1)

    obj.Display()
    ret=obj.Deposit()
    print("Balance after deposited amount is:", ret)

    ret1=obj.Withdraw()
    print("Balance after withdrawn amount is:", ret1)

    ret2=obj.CalculateIntrest()
    print("Yearly interest amount is:", ret2)

if __name__=="__main__":
    main()
