def Addition(no1,no2): #### basic code
    return no1+no2
## def func_name(parameter)
    #body

AddX =lambda no1,no2:no1+no2 ## lamda or anonimous finction. AddX is function name

print (type(lambda no1,no2:no1+no2))

print (lambda no1,no2:no1+no2) ### binary files text section address .
## diff address space gets allocated when run again

def main():
    ret=Addition(10,20)
    print ("addition is",ret)

    ret=AddX(10,20)
    print ("addition is",ret)

    print(type(Addition))
if __name__=="__main__":
    main()