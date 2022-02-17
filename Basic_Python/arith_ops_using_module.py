##main program
import arith_modl

def main():
    print("Enter first no: ")
    no1=int(input())

    print("Enter second no: ")
    no2=int(input())

    ret = arith_modl.Add(no1,no2)
    print ("Addition of two numbers is :",ret)

    ret = arith_modl.Sub(no1, no2)
    print("Substraction of two numbers is :", ret)

    ret = arith_modl.Mult(no1, no2)
    print("Multiplication of two numbers is :", ret)

    ret = arith_modl.Div(no1, no2)
    print("Division of two numbers is :", ret)

if __name__=="__main__":
    main()