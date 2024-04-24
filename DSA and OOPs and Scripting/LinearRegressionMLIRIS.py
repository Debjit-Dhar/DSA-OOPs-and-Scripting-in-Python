import numpy as np
import math
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
iris=datasets.load_iris()
#dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
iris_x=iris.data
iris_y=iris.target
iris_x_train=iris_x[:-60]
iris_x_test=iris_x[30:]
iris_y_train=iris_y[:-60]
iris_y_test=iris_y[30:]
model=linear_model.LinearRegression()
model.fit(iris_x_train,iris_y_train)
iris_y_predicted=model.predict(iris_x_test)
print("mean squared error :",mean_squared_error(iris_y_test,iris_y_predicted))
print("Weights :",model.coef_)
print("Intercepts :",model.intercept_)
print("Predictions\tActual")
for i in range(30):
    if round(iris_y_predicted[i])==0:
        print("Setosa",end='\t')
    elif round(iris_y_predicted[i])==2:
        print("Virginica",end='\t')
    else:#1 for Versicolor
        print("Versicolor",end='\t')
    if round(iris_y_test[i])==0:
        print("Setosa")
    elif round(iris_y_test[i])==2:
        print("Virginica")
    else:#1 for Versicolor
        print("Versicolor")