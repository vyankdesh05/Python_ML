class Circle:
    def __init__(self,R,A,C):
        self.radius=R
        self.area=A
        self.circum=C

    def Accept(self):
        print (self.radius)

    def CalculateArea(self):
        self.area=self.radius*self.radius*3.14
        return self.area

    def CalculateCircum(self):
        self.circum=2*3.14*self.radius
        return self.circum

    def Display(self):
        print (self.radius)
        print (self.area)
        print (self.circum)

def main():
    Area=0
    Circ=0
    print ("Enter value of radius :")
    val=int(input())

    rad=Circle(val,Area,Circ)

    ret=rad.CalculateArea()
    ret1=rad.CalculateCircum()
    print ("Area of circle is",ret)
    print("Circumference of circle is", ret1)
    rad.Display()

if __name__=="__main__":
    main()