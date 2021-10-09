import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

file = pd.read_csv("Covid_Confirmed_Data.csv")
headerlist = ['Date', 'Cases', 'Deaths', 'Recovered']

file.to_csv("Covid_Confirmed_Data_New.csv", header=headerlist, index=True, index_label='index')

file_new = pd.read_csv("Covid_Confirmed_Data_New.csv")
print(file_new)

X = file_new.index.values
Y = file_new.Cases.values

plt.scatter(X, Y)
plt.show()

X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)
#print(X)
#print(Y)

#Prediction of Positive Cases
model = LinearRegression()
model.fit(X, Y)

b0 = model.intercept_
b1 = model.coef_

Y1 = model.predict(X)
print(X[558], Y[558], Y1[558])

score = r2_score(Y, Y1)
print("r2 score is:", score)

print("Linear Equation: Y = {} + {}*X".format(b0[0], b1[0][0]))