#palindrome like manam m=0 a=1  n=2 a=3 m=4
#mannam

i=0
str=input("enter string to check: ")

j=len(str)

if str[i] != str[j-1]:
    print ("string is not palindrome")
else :
    while j >= i:
        if str[i] == str[j - 1]:
            j=j-1
            i=i+1
        else :
            print("string is not palindrome")
            exit(0)
    print ("string is palindrome")




