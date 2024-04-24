class Person:
    def __init__(self,name,age,salary):
        self.__name=name
        self.__age=age
        self.__salary=salary
    def __str__(self):
        return f"{self.__name} is aged {self.__age} years and earns {self.__salary} dollars per month."
    def calprov(self):
        return self.__salary-0.1*self.__salary

class American(Person):
    def __init__(self,name,age,salary,nog):
        super().__init__(name,age,salary)
        self.nog=nog

p1=Person("John Lincoln",21,2100)
print(p1)
print(p1._Person__name)#Name Mangling
pf=p1.calprov()
print(pf)
p2=American("Ben Johnson",31,3800,5)
print(p2)
print(p2._Person__name,"has",p2.nog,"guns.")#Name Mangling




