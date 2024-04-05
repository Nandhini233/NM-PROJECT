# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14I1D3-g6UASOlMrASyVN0Izw1mCOjXOI
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = pd.read_csv('C:\\Users\\Sarmila\\Documents')
sns.pairplot(data)
plt.show()
X = data[['temperature', 'humidity', 'day_of_week', 'hour_of_day']]  # Features
y = data['energy_consumption']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
new_data = np.array([[25, 60, 4, 14]])
predicted_energy_consumption = model.predict(new_data)
print("Predicted energy consumption:", predicted_energy_consumption)



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = pd.read_csv('/content/drive/MyDrive/ibm/ibm 1.csv')
sns.pairplot(data)
plt.show()
X = data[['temperature', 'humidity', 'day_of_week', 'hour_of_day']]  # Features
y = data['energy_consumption']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
new_data = np.array([[25, 60, 4, 14]])
predicted_energy_consumption = model.predict(new_data)
print("Predicted energy consumption:", predicted_energy_consumption)

from google.colab import drive
drive.mount('/content/drive')