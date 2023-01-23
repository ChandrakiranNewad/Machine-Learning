# -*- coding: utf-8 -*-
"""220940325022_DATA_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g-B0B60I2pCwn9pm9fVnSUZMrb50Soww
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('data_1.csv')

df.head()

#checking no. of rows and columns
df.shape

#getting some info about the data
df.info()

#checking for null values. no null values are present.
df.isnull().sum()

# finding stats of the data.
df.describe()

# checking for unique values for the categorical columns of the data.
df['Fuel_Type'].unique()

df['Seller_Type'].unique()

df['Transmission'].unique()

df['Owner'].unique()

df.columns

# checking correlation of dependent var(selling_price) with independent var.
df.corr()['Selling_Price']

#duplicating the dataframe
df1=df

df1.info()

# converting object datatype to category data type
df1['Fuel_Type']=df1['Fuel_Type'].astype('category')
df1['Seller_Type']=df1['Seller_Type'].astype('category')
df1['Transmission']=df1['Transmission'].astype('category')
df1['Owner']=df1['Owner'].astype('category')

df1.info()

# creating dummy for categorical columns
Fuel_Type_D = pd.get_dummies(df1['Fuel_Type'],drop_first=True)
df1=pd.concat([df1,Fuel_Type_D],axis=1)
df1=df1.drop('Fuel_Type',axis=1)

Seller_Type_D = pd.get_dummies(df1['Seller_Type'],drop_first=True)
df1=pd.concat([df1,Seller_Type_D],axis=1)
df1=df1.drop('Seller_Type',axis=1)

Transmission_D = pd.get_dummies(df1['Transmission'],drop_first=True)
df1=pd.concat([df1,Transmission_D],axis=1)
df1=df1.drop('Transmission',axis=1)

Owner_D = pd.get_dummies(df1['Owner'],drop_first=True)
df1=pd.concat([df1,Owner_D],axis=1)
df1=df1.drop('Owner',axis=1)

df1.head()

# checking the correlation. KMs_Driven is not strongly correlated to y var 
# but by the domain knowlegde it is an imp feature.

df1.corr()['Selling_Price']

#droping car_name col because info can get from year also so dropping it by info domain knowledge
df1=df1.drop(['Car_Name'],axis=1)

df1.head()

#shape before splitting.
df1.shape

#splitting the data into X and y

X=df1.iloc[:,[0,2,3,4,5,6,7,8,9,10,11]].values
X.shape

y=df1.iloc[:,1].values
y.shape

from sklearn.model_selection import train_test_split

# splitting the data into train and test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=123)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()

# Training the model
rf.fit(X_train,y_train)

# Model summary
y_pred_rf=rf.predict(X_test)

from sklearn.metrics import r2_score
from sklearn import metrics as sm
r_sq=r2_score(y_test,y_pred_rf)
rmse=sm.mean_squared_error(y_test,y_pred_rf)
print("R_Squared : ",r_sq,"MSE : ",rmse)

"""**Conclusion :**

1. Present price of a car plays an important role in predicting Selling price, one increases the other gradually increases.(Highly correlated)

2.Selling Price of cars with fuel type diesel is higher.
3.Car of manual type is of less priced whereas of automatic type is high.
4. car sold by individual tend to get less selling price when sold by dealers
"""