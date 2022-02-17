def Area(radius,pi=3.14): ### default value.
#def Area(pi=3.14, radius):  ### default value.gives error by compiler . right to left
    ans=0
    ans=pi*radius*radius
    return ans

def main():
    print ("Enter radius of circle")
    value= float(input())
    ret=0
    ret=Area(value,7.10)
    #ret=Area(pi=7.10,radius=value) ### keyword agrs
    print (ret)

if __name__=="__main__":
    main()