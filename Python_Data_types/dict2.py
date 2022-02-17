
def main():
    #      [Python,PPA,  LSP, Angular]
    # fess = [12500,15000,21000,15500]
    fess = {"Python" : 12500, "PPA" : 15000, "LSP" : 21000, "Angular" : 15500}

    print(fess)

    print("Please enter batch name")
    batch = input()

    print("Thank you for selecting : ",batch)
    
    print("Fees are : ",fess[batch])

if __name__ == "__main__":
    main()