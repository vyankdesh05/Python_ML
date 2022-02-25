import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

excel_file='WinePredictor.csv'

batch_sheet=pd.read_csv(excel_file,skiprows=1)
print (batch_sheet)

target = batch_sheet.columns[0]
print(target)

X = batch_sheet.drop(target, axis = 1)
print(X)
y = batch_sheet.drop(X, axis = 1)
print(y)

train_data,test_data,train_target,test_target=train_test_split(X,y,test_size=0.7)

obj=KNeighborsClassifier(n_neighbors=9)
obj1=obj.fit(train_data,train_target)
result=obj1.predict(test_data)
print(result)

Accuracy=accuracy_score(test_target,result)
print(Accuracy*100)