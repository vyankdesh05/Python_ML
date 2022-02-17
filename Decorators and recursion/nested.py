
def outer():
    print ("Inside outer finction")

    def inner():
        print ("inside inner function")

    inner()
def main():
    outer()

if __name__=="__main__":
    main()