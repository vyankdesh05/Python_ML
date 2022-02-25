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

from matplotlib import pyplot as plt

x = np.array(X)
y = np.array(Y)
yp = np.array(YP)
#plt.xlabel(x)
#plt.ylabel(y)
#plt.plot(x, y, c='green')

plt.plot(x, y, color='green', marker='o', markerfacecolor='blue', markersize=12)

plt.plot(x, yp, color='red',marker='o', markerfacecolor='yellow', markersize=12)

plt.margins(y=C)
plt.show()