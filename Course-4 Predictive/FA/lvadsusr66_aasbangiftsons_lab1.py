# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11sSXI6M87V_rRA65z9djFkwJxHcN7SdN
"""

import pandas as pd
data = pd.read_csv("loan_approval.csv")
data.head()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dcl
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

data = pd.read_csv("loan_approval.csv")

# Check for missing values
print(data.isnull().sum())

# No missing data
data.dropna(inplace=True)

# Outlier Handling (you can choose a specific feature for outlier detection)
Q1 = data[' income_annum'].quantile(0.25)
Q3 = data[' income_annum'].quantile(0.75)
IQR = Q3 - Q1
data = data[~((data[' income_annum'] < (Q1 - 1.5 * IQR)) | (data[' income_annum'] > (Q3 + 1.5 * IQR)))]

# EDA
print(data.describe())
print(data.info())

# Visualize distribution of loan_status
sns.countplot(x=' loan_status', data=data)
plt.title('Loan Status Distribution')
plt.show()

# Feature analysis
sns.pairplot(data, hue=' loan_status')
plt.title('Pairplot of Features by Loan Status')
plt.show()

# Convert categorical variables to numerical
label_encoder = LabelEncoder()
data[' education'] = label_encoder.fit_transform(data[[' education']])
data[' loan_status'] = label_encoder.fit_transform(data[[' loan_status']])
data[' self_employed'] = label_encoder.fit_transform(data[[' self_employed']])



# Splitting data into features and target variable
X = data.drop(['loan_id', ' loan_status'], axis=1)
y = data[' loan_status']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression model
model = dcl()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=1)
recall = recall_score(y_test, y_pred, pos_label=1)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print('Confusion Matrix:')
print(conf_matrix)

# Visualize the Confusion Matrix
sns.heatmap(conf_matrix, annot=True, cmap='Blues')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

