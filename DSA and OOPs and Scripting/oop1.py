class car:
    def __init__(self,model,price):
        self.model=model
        self.price=price
class plane:
    def __init__(self,model,price,company):
        self.model=model
        self.price=price
        self.company=company
class transport(car,plane):
    pass
x=car('rolls royce',100)
y=plane('dreamliner',1000,'usair')
print(x.model)
print(x.price)
print(y.model)
print(y.price)
print(y.company)
