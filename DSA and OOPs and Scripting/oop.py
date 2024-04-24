class car:
    def __init__(self,model,price):
        self.model=model
        self.price=price
class RollsRoyce(car):
    def __init__(self,model,price,version):
        car.__init__(self,model,price)
        self.version=version
class RollsRoyce1(RollsRoyce):
    pass
x=RollsRoyce1('rolls royce',100,'rr101')
print(x.model)
print(x.price)
print(x.version)