######## Class example taken on 13th Feb
import numpy as np

X=[1,2,3,4,5]
X_bar=np.mean(X)
print(X_bar)

Y=[3,4,2,4,5]
Y_bar=np.mean(Y)
print(Y_bar)
Num=0
Denom=0
for i in range(len(X)):
    Num+=(X[i]-X_bar)*(Y[i]-Y_bar)
    Denom+=(X[i]-X_bar)*(X[i]-X_bar)
print(Num,Denom)
m=Num/Denom
print(m)

C=Y_bar-(m*X_bar)
print(C)
YP=[]  ### y=mX + C
for i in range(len(X)):
    YP.append((m*X[i]+C))

print(YP)
R_Num=0
R_Denom=0
for i in range(len(X)):
    R_Num+=(YP[i]-Y_bar)*(YP[i]-Y_bar)
    R_Denom+=(Y[i]-Y_bar)*(Y[i]-Y_bar)

R_Sqr=R_Num/R_Denom

print("Value of R^2 is:",R_Sqr)