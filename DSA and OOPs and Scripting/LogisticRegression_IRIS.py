import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
dataset=pd.read_csv("All_signal/Final_result_all.csv")
x=dataset.iloc[:,[2,3,4,5,6,7]]
y=dataset.iloc[:, -1].values
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=42,shuffle=True)
model=LogisticRegression(max_iter=1000000)
model.fit(x_train,y_train)
prediction=model.predict(x_test)
print(confusion_matrix(y_test,prediction))
print(accuracy_score(y_test,prediction)*100,"%")