
class BookStore:
    NoOfbooks=0

    def __init__(self,N,A):
        self.Name=N
        self.Author=A
        BookStore.NoOfbooks+=1

    def Display(self):
        print("Name of book is:",self.Name)
        print("Author of book is:",self.Author)
        print("Number of books is:",BookStore.NoOfbooks)

def main():

    N1=input("Enter name of the book:")
    A1=input("Input author of the book:")
    obj1=BookStore(N1,A1)
    obj1.Display()

    N2=input("Input name of the book:")
    A2=input("Input author of the book:")
    obj2 = BookStore(N2, A2)
    obj2.Display()

if __name__=="__main__":
    main()
