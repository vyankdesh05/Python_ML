#program which accept name from user and display length of its name.

def main():
    stng=input("Enter string: ") 
    leng=len(stng)
    print("Length of string is : ",leng)

if __name__=="__main__":
    main()