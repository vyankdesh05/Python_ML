######## Class example taken on 13th Feb
import numpy as np
import pandas as pd

excel_file='Advertising.csv'

df=pd.read_csv(excel_file,usecols=["TV","sales"])

X = df["TV"].tolist()
X_bar=np.mean(X)
print("Mean of X (TV) values is :",X_bar)

Y = df["sales"].tolist()
Y_bar=np.mean(Y)
print("Mean of Y (sales) values is:",Y_bar)

Num=0
Denom=0
for i in range(len(X)):
    Num+=(X[i]-X_bar)*(Y[i]-Y_bar)
    Denom+=(X[i]-X_bar)*(X[i]-X_bar)
m=Num/Denom
print("M value is :",m)

C=Y_bar-(m*X_bar)
print("C value is :",C)
YP=[]  ### y=mX + C
for i in range(len(X)):
    YP.append((m*X[i]+C))

R_Num=0
R_Denom=0
for i in range(len(X)):
    R_Num+=(YP[i]-Y_bar)*(YP[i]-Y_bar)
    R_Denom+=(Y[i]-Y_bar)*(Y[i]-Y_bar)

R_Sqr=R_Num/R_Denom

print("Value of R^2 is:",R_Sqr)