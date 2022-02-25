######## Class example taken on 13th Feb
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

excel_file='Advertising.csv'

df=pd.read_csv(excel_file)

X=df.drop('sales',axis=1)
Y = df["sales"]


# Split the data into training/testing sets
X_train = X[:-20]
X_test = X[-20:]

# Split the targets into training/testing sets
Y_train = Y[:-20]
Y_test = Y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train,Y_train)

# Make predictions using the testing set
Y_pred = regr.predict(X_test)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(Y_test, Y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(Y_test, Y_pred))
