from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris=datasets.load_iris()
features=iris.data
labels=iris.target
model=KNeighborsClassifier()
model.fit(features,labels)
pred=model.predict([[9.1,0.2,0.1,0.1]])
print(pred)
