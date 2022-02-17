from functools import reduce

def main():

    reddata = reduce(lambda a,b:a+b, (list(map(lambda no:no+2,(list(filter(lambda no:(no % 2==0),[5,7,6,8,4])))))))
    print("Reduced data is: ", reddata)

if __name__=="__main__":
    main()