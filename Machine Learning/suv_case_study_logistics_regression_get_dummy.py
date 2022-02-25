import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def SuvPredictor():
    excel_file='suv_data.csv'

    df=pd.read_csv(excel_file)

    print (df)

    df1=df.drop("User ID",axis=1)
    print(df1)

    sex=pd.get_dummies(df1["Gender"])

    print (sex.head(5))

    df1=pd.concat([df1,sex],axis=1)

    print(df1)

    df1.drop(["Gender"],axis=1,inplace=True)

    print(df1)

    x=df1.drop("Purchased",axis=1)
    y=df1["Purchased"]

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.8)

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
    print ("SUV predictor case study using get dummies menthod")
    print("*" * 50)
    ## call prediction function

    SuvPredictor()

if __name__=="__main__":
    main()