
def main():
    #      [Python,PPA,  LSP, Angular]
    #      [0       1      2    3 ]
    fess = [12500,15000,21000,15500]

    print(fess)

    print("Please enter batch name")
    batch = input()

    print("Thank you for selecting : ",batch)
    
    if batch == "PPA":
        print("Fees are : ",fess[1])
    elif batch == "LSP":
        print("Fees are : ",fess[2])
    elif batch == "Python":
        print("Fees are : ",fess[0])
    elif batch == "Angular":
        print("Fees are : ",fess[3])
    else:
        print("There is no such batch in Marvellous")

if __name__ == "__main__":
    main()