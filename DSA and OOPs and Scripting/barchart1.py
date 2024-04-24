import matplotlib.pyplot as pl
x=['USA','China','Russia','Japan','UK','Germany','France','India','N. Korea']
y=[100,85,70,80,72,66,69,18,1]
colors=['blue','red','green','cyan','black','hotpink','purple','brown','cornsilk']
pl.bar(x,y,color=colors,width=0.9)
pl.xlabel('Countries')
pl.ylabel('Score')
pl.title('Technology Scores')
pl.grid()
pl.show()