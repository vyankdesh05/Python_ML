import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show

def TitanicPredictor():
    #load data
    excel_file='titanic_data.csv'

    df=pd.read_csv(excel_file)
    print (df)

    #Analyse data. Helps to determine which factors are affecting for survival
    figure()
    target="Survived"
    countplot(data=df,x=target).set_title("Survived and non survived passengers")
    show()

    figure()
    target = "Survived"
    countplot(data=df, x=target,hue="Sex").set_title("Survived and non survived passenger based on gender")
    show()

    figure()
    target = "Survived"
    countplot(data=df, x=target, hue="Pclass").set_title("Survived and non survived passenger based on class")
    show()

    figure()
    df["Age"].plot.hist().set_title("Survived and non survived passenger based on Age")
    show()

    figure()
    df["Fare"].plot.hist().set_title("Survived and non survived passenger based on Fare")
    show()

    #clean data
    df1=df.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
    df1.dropna(inplace=True) ##### drop NaN values
    print(df1)


    print (pd.get_dummies(df1["Sex"]))

    Sex=pd.get_dummies(df1["Sex"],drop_first=True)
    print(Sex)

    print(pd.get_dummies(df1["Sex"]))

    Embark = pd.get_dummies(df1["Embarked"], drop_first=True)
    print(Embark)
    df1=pd.concat([df1,Sex,Embark],axis=1)

    df1.drop(["Sex","Embarked"],axis=1,inplace=True)

    print(df1)

    x=df1.drop("Survived",axis=1)
    y=df1["Survived"]

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

    logmodel=LogisticRegression()

    logmodel.fit(xtrain,ytrain) ## added line 15 due to ValueError: Input contains NaN, infinity or a value too large for dtype('float64')

    prediction=logmodel.predict(xtest)

    print("Classification report")
    print(classification_report(ytest,prediction))

    print("Confusion matrix of logsitics regression is :")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy score of logistics regression is :")
    print(accuracy_score(ytest,prediction))

def main():
    print ("*"*50)
    print ("Titanic survival predictor case study using get dummies method")
    print("*" * 50)
    ## call prediction function

    TitanicPredictor()

if __name__=="__main__":
    main()