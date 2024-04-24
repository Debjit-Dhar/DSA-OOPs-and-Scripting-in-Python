from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LassoLars
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
dataset=fetch_california_housing()
x=dataset.data
y=dataset.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)
model=LassoLars(alpha=0.0001)
model.fit(x_train,y_train)
prediction=model.predict(x_test)
print("r2 score= ",r2_score(y_test,prediction))

