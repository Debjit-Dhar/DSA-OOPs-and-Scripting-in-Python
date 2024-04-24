from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as pl
# Loading Datasets
iris = datasets.load_digits()
x=iris.data
y=iris.target
print(len(y))
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)

print(iris.DESCR)


# Training the classifier
#for i in range(1,10):
clf = KNeighborsClassifier(n_neighbors=6)
clf.fit(x_train,y_train)
prediction=clf.predict(x_test)
print(confusion_matrix(y_test,prediction))
ac=accuracy_score(y_test,prediction)
print(ac)
#    pl.plot(i,ac,marker='o')
#pl.grid(True)
#pl.show()
