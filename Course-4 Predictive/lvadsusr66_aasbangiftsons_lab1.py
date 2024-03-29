# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LuFUpmeqmxigVLwliADuZ521QykWzxze
"""

import pandas as pd
df = pd.read_csv("expenses.csv")
df.head()

#1
import matplotlib.pyplot as plt
import seaborn as sns

duplicates = df[df.duplicated()]
print("\nDuplicate rows:")
print(duplicates)
df.drop_duplicates(inplace=True)

print("\nMissing values in the dataset:")
print(df.isnull().sum())

print("\nSummary statistics of numerical features:")
print(df.describe())

df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

df.boxplot(figsize=(10, 6))
plt.tight_layout()
plt.show()

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

#2
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

df["sex"] = label_encoder.fit_transform(df["sex"])
df["smoker"] = label_encoder.fit_transform(df["smoker"])
df["region"] = label_encoder.fit_transform(df["region"])

print(df.head())

#3
from sklearn.preprocessing import StandardScaler
numerical_features = ['age', 'bmi','charges']
for feature in numerical_features:
    lower_bound = df[feature].quantile(0.05)
    upper_bound = df[feature].quantile(0.95)
    df[feature] = df[feature].clip(lower=lower_bound, upper=upper_bound)

#removing columns with less correlation
df = df.drop('sex',axis=1)
df = df.drop('children',axis=1)
df = df.drop('region',axis=1)

X = df.drop(columns=['charges'])
y = df['charges']

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
scaled_data = pd.DataFrame(X_scaled, columns=X.columns)

scaled_data['Target'] = y

df.head()

#4
from sklearn.model_selection import train_test_split

X = df[['age','bmi','smoker']]
y = df['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#5
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

#6
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

accuracy = model.score(X_test, y_test)

MSE = mean_squared_error(y_test, y_pred)

R_squared = r2_score(y_test, y_pred)

RMSE = sqrt(MSE)

print("Accuracy:", accuracy)
print("MSE:", MSE)
print("R-squared:", R_squared)
print("RMSE:", RMSE)

"""##The learning rate is a crucial hyperparameter in gradient descent algorithm. It controls the complexity of the steps taken towards the optimal solution during training. A proper rate ensures efficient convergence by balancing between fast convergence and stable optimization, preventing overfitting or slow convergence."""

