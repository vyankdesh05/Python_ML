    import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

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
fe2=fe2.transform(feature2)
print(fe2)

fe3=[]
for i in range(len(fe1)):
    fe3.append([(fe1[i]),(fe2[i])])

print(fe3)

label1 = batch_sheet['Play'].tolist()
print(label1)
le = preprocessing.LabelEncoder()
le.fit(label1)
le1=le.transform(label1)
print(le1)

obj=KNeighborsClassifier()
obj1=obj.fit(fe3,le1)

wether=input("Enter weather:")
temp=input("Enter temprature:")

if wether.lower()=="sunny":
    wether=2

elif wether.lower()=="overcast":
    wether=0

elif wether.lower()=="rainy":
    wether=1

else:
    print ("Invalid input")

if temp.lower()=="hot":
    temp=1

elif temp.lower()=="mild":
    temp=2

elif temp.lower()=="cool":
    temp=0

else:
    print ("Invalid input")

result=obj1.predict([[wether,temp]])

if result==0:
    print ("NO")

elif result==1:
    print("YES ")
