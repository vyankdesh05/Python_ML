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
fe1=fe1.fit_transform(feature1)
print(fe1)

feature2 = batch_sheet['Temperature'].tolist()
print(feature2)
fe2 = preprocessing.LabelEncoder()
fe2=fe2.fit_transform(feature2) ######## fit_transform(weather)
print(fe2)

fe3=list(zip(fe1,fe2))
print(fe3)

label1 = batch_sheet['Play'].tolist()
print(label1)
le = preprocessing.LabelEncoder()
le1=le.fit_transform(label1)
print(le1)

train_data,test_data,train_target,test_target=train_test_split(fe3,le1,test_size=0.5)

K_list=[]
for i in range (1,20):
    obj=KNeighborsClassifier(n_neighbors=i)
    obj1=obj.fit(train_data,train_target)
    result=obj1.predict(test_data)

    Accuracy=accuracy_score(test_target,result)
    Acc_per=Accuracy*100
    K_list.append([i,Acc_per])
    print(K_list)