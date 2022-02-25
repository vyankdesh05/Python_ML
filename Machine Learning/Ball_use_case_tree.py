from sklearn import tree


def Train_data(weight,surface):

    BallType=[[90,0],[30,1],[85,0],[100,0],[35,1]]
    Surf=[2,1,2,2,1]

    obj=tree.DecisionTreeClassifier()
    obj1=obj.fit(BallType,Surf)
    result=obj1.predict([[weight,surface]])

    if result==1:
        print ("Tennis ball")

    elif result==2:
        print("Cricket ball ")
def main():
    print("---- Predict ball use case -----")
    weight=input("Enter weight of the ball:")
    surface=input("Enter surface of the ball:")

    if surface.lower()=="rough":
        surface=1

    elif surface.lower()=="smooth":
        surface=0

    Train_data(weight,surface)


if __name__ == "__main__":
    main()
