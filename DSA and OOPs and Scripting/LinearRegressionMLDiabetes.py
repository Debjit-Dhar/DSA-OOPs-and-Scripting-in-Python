import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Split the dataset into features and target
diabetes_X = diabetes.data
diabetes_Y = diabetes.target

# Split the data into training and testing sets
diabetes_X_train = diabetes_X[:-30]  # last 30 for training
diabetes_X_test = diabetes_X[-30:]   # first 30 for testing
diabetes_Y_train = diabetes_Y[:-30]
diabetes_Y_test = diabetes_Y[-30:]

# Create and train the linear regression model
model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_Y_train)

# Predict on the test set
diabetes_Y_predicted = model.predict(diabetes_X_test)

# Print mean squared error, weights, and intercept
print("Mean squared error is:", mean_squared_error(diabetes_Y_test, diabetes_Y_predicted))
print("Weights:", model.coef_)
print("Intercept:", model.intercept_)

# Plot the scatter plot and regression line
plt.scatter(diabetes_X_test[:, 2], diabetes_Y_test, color='blue')
plt.plot(diabetes_X_test[:, 2], diabetes_Y_predicted, color='red', linewidth=2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Diabetes dataset - Linear Regression")
plt.show()
