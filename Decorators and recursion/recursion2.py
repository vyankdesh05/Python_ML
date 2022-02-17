
def DisplyR(no):
    if no > 0:
        print ("Marveloous")
        no=no-1
        DisplyR(no)

def main():
    DisplyR(4)
    #Display()

if __name__=="__main__":
    main()