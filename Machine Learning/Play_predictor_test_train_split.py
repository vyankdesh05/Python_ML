import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

excel_file='MarvellousInfosystems_PlayPredictor.xlsx'

batch_sheet=pd.read_excel(excel_file,skiprows=1)
feature1 = batch_sheet['Wether'].tolist()
print(feature1)
fe1 = preprocessing.LabelEncoder()
fe1.fit(feature1)
fe1=fe1.transform(feature1)
print(fe1)

feature2 = batch_sheet['Temperature'].tolist()
print(feature2)
fe2 = preprocessing.LabelEncoder()
fe2.fit(feature2)
fe2=fe2.transform(feature2) ######## fit_transform(weather)
print(fe2)

fe3=[]
for i in range(len(fe1)):
    fe3.append([(fe1[i]),(fe2[i])]) ###### zip function does the same

print(fe3)

label1 = batch_sheet['Play'].tolist()
print(label1)
le = preprocessing.LabelEncoder()
le.fit(label1)
le1=le.transform(label1)
print(le1)

train_data,test_data,train_target,test_target=train_test_split(fe3,le1,test_size=0.5)

obj=KNeighborsClassifier(n_neighbors=3)
obj1=obj.fit(train_data,train_target)
result=obj1.predict(test_data)
print(result)

Accuracy=accuracy_score(test_target,result)
print(Accuracy*100)