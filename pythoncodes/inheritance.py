#when one class (child) derives the properties and methods to another class (parent)
class Car:
    clolur="black"
    
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class TokyoCar(Car):
    def __init__(self,name):
        self.name=name

car1=TokyoCar("fortuner")
car2=TokyoCar("inova")

print(car1.name)
print(car2.name)
print(car1.clolur)
car1.start()

#using class methods
class Person:
    name = "anonymous"
    @classmethod
    def changename(cls,name):
        cls.name=name
p1=Person()
print(Person.name)
p1.changename("k.l. rahul")
print(p1.name)
print(Person.name)

#'@property'
# we use property method or any other method in the class, to use the method as a property
class Student:
    def __init__(self,phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def persentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
stu1= Student(99,96,92)
print(stu1.persentage)
