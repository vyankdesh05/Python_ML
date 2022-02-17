### arbitary argeuments

def Fun(*Value):
    print(Value)
    print(type(Value))

def main():
    Fun(10,20,30,40)

if __name__=="__main__":
    main()