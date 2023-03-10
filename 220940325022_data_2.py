# -*- coding: utf-8 -*-
"""220940325022_DATA_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y6aQGeYrgfcoV0VPzTXDuj71O53xirul
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel('data_final.xlsx')

df.head()

#checking no. of rows and columns
df.shape

#getting some info about the data
df.info()

#checking for null values. no null values are present.
df.isnull().sum()

df.describe()

# plotting pairplot for visualizing the data 
sns.pairplot(df)

#checking correlation of price(dependent cols) with remaining columns(independent cols).
# both are strongly correlated to price as correlation coef is close to 1.
# so no need to drop columns
df.corr()['price']

plt.scatter(df['feature'],df['price'])
plt.xlabel("Feature")
plt.ylabel("Price")
plt.title("ScatterPlot")
plt.show()

plt.scatter(df['observation'],df['price'])
plt.xlabel("observation")
plt.ylabel("Price")
plt.title("ScatterPlot")
plt.show()

# checking for the outliers in feature column
plt.boxplot(df['feature'],vert=False)
plt.show()

# checking for the ouliers in observation column
plt.boxplot(df['observation'],vert=False)
plt.show()

"""1.By visualizing scatter plots for each col with price we can see that linear regression will not be useful here.

2. By visualizing the boxplot we can conclude that no outliers are present in the data.
"""

# splitting the data into dependent and independent variables
X = df.iloc[:,:-1].values
X

y=df.iloc[:,-1].values
y

# checking the shape after splitting the data
print(X.shape,y.shape)

# splitting training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=12)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

"""**Multi Linear Regression Model**"""

from sklearn.linear_model import LinearRegression
model=LinearRegression()
# training the model
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
y_pred

plt.scatter(y_pred,y_test,color='red')
plt.plot(y_pred,y_test,color='green')

"""1= 180.38
2= 1312.07
3= 440.13
4= 343.72
"""

model.predict([[0.34,0.68]])

model.predict([[0.33,0.19]])

from sklearn import metrics as sm

# model performance

print("Regressor model performance")
print("MAE : ",round(sm.mean_absolute_error(y_test,y_pred),2))
print("MSE : ",round(sm.mean_squared_error(y_test,y_pred),2))
print("Explain variance score : ",round(sm.explained_variance_score(y_test,y_pred),2))

"""**Polynomial Regression Model**"""

from sklearn.preprocessing import PolynomialFeatures
model2=PolynomialFeatures(degree=2)
X_poly = model2.fit_transform(X_train)
lg1 = LinearRegression()
lg1.fit(X_poly,y_train)
lg1.score(X_poly,y_train)

y_pred1=lg1.predict(model2.fit_transform(X_test))
y_pred1

plt.scatter(y_pred1,y_test,color="red")
plt.plot(y_pred1,y_test,color="blue")

"""**Conclusion**


1.I have used Multiple Linear regression model and Polynomial Regression model. As I have plotted scatter-plot for these two models , it is seen that Polynomial regression model gives best regression line.

2.Almost all the points are on the regression line,hence Polynomial regression model is best to decide "price per square foot" .

3.Hence, for these DataSet ,Polynomial Regression model is more accurate than Multiple Linear regression model
"""