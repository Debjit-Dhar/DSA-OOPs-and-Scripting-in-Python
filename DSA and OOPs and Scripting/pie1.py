import matplotlib.pyplot as pl
x=['USA','China','Russia','Japan','UK','Germany','France','India','N. Korea']
y=[100,85,70,80,72,66,69,18,1]
expl=[0.2,0,0,0,0,0,0,0,0]
colorchart=['blue','red','green','cyan','bisque','hotpink','purple','brown','cornsilk']
pl.axis('equal')
pl.pie(y,colors=colorchart,shadow=True,labels=x,explode=expl,autopct="%2.2f%%")
pl.title('Technology Scores')
pl.show()