class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __str__(self):
          return f'{self.name} is {self.age} years old'
class Student(Person):
      def __init__(self,name,age,estat):
          super().__init__(name,age)
          self.estat=estat
p1 = Student('God',36,'Phd')
print(p1,'and has done',p1.estat)
