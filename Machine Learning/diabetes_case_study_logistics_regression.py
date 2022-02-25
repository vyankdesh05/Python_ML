import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def DiabetesPredictor():
    data_file='diabetes.csv'

    df=pd.read_csv(data_file)

    print (df)

    x=df.drop("Outcome",axis=1)
    y=df["Outcome"]
    print ("Below are independent variables")
    print (x)

    print (" ")

    print ("Below are dependent variable")
    print (y)

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

    logmodel=LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    prediction=logmodel.predict(xtest)

    print("Classification report")
    print(classification_report(ytest,prediction))

    print("Confusion matrix of logsitics regression is :")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy score of logistics regression is :")
    print(accuracy_score(ytest,prediction))

def main():
    print ("*"*50)
    print ("DiabetesPredictor predictor case study using logistics regression")
    print("*" * 50)
    ## call prediction function

    DiabetesPredictor()

if __name__=="__main__":
    main()