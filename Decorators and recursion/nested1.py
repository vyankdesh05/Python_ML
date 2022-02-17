
def outer():
    print ("Inside outer finction")

    def inner():
        print ("inside inner function")

    return inner ### return hasccode.

def main():
    funct_name=outer()
    print ("hello") # just to undersand sequence
    funct_name() ## this deisqlify abstraction

if __name__=="__main__":
    main()