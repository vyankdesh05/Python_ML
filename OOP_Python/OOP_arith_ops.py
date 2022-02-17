class Arithmetic:

    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def Accept(self):
        print("Enter first number:")
        val1 = int(input())

        print("Enter second number:")
        val2 = int(input())

        self.A = val1
        self.B = val2

        print(self.A)
        print(self.B)

    def Addition(self):
        Sum = self.A + self.B
        return Sum

    def Substraction(self):
        Sub = self.A - self.B
        return Sub

    def Multiplication(self):
        Mult = self.A * self.B
        return Mult

    def Division(self):
        Div = self.A / self.B
        return Div


def main():
    obj = Arithmetic(0, 0)
    obj.Accept()

    ret1 = obj.Addition()
    print("Addition of numbers is:", ret1)

    ret2 = obj.Substraction()
    print("Substraction of numbers is:", ret2)

    ret3 = obj.Multiplication()
    print("Multipliction of numbers is:", ret3)

    ret4 = obj.Division()
    print("Division of numbers is:", ret4)

if __name__ == "__main__":
    main()

