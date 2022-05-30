
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('aa.csv')
X = dataset.iloc[:, 1:10].values
Y = dataset.iloc[:,8].values


# Encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1.fit_transform(X[:, 0])
labelencoder_X_2 = LabelEncoder()
X[:, 1] = labelencoder_X_2.fit_transform(X[:, 1])

# Country column
ct = ColumnTransformer([("Location", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)
X = X.toarray()
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Part 2 - Making the ANN
# Importing the keras libraries and packages
import keras
#import The sequential module that is required to initialize our neural network
from keras.models import Sequential
#import the Dent Module that is required to build the layers of the ann.
from keras.layers import Dense

#initializing the ANN
ann = Sequential()
ann.add(keras.Input(26,))
# Adding the first hidden layer
ann.add(Dense(5, kernel_initializer='uniform', activation='relu'))
# Add the second hidden layer
ann.add(Dense(5, kernel_initializer='uniform', activation='relu'))
# Add the output layer
ann.add(Dense(1, kernel_initializer='uniform', activation='relu'))
# Compiling the ANN
ann.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
# Fitting ann to the Training set
ann.fit(x_train, y_train, batch_size=1, epochs=1000)


# Predicting the Test set results
y_pred = ann.predict(x_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
# Predicting a single new observation
"""
new_prediction = ann.predict(sc.transform(np.array([[0,0,600,1,40,3,60000,2,1,1,50000]])))
new_prediction = (new_prediction > 0.5)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)"""