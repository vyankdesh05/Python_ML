# arbitary arguments

def Addition(*Value):
    ans=0
    for i in Value:
        ans=ans+i
    return ans


def main():
    ret=Addition()
    print ("Additon is ",ret)

    ret=Addition(10,20,30)
    print ("Additon is ",ret)

if __name__=="__main__":
    main()