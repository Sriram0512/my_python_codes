# waf to find the area and perimeter of a circle

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius

c1=Circle(21)
print("area of circle is",c1.area())
print("perimeter of circle is",c1.perimeter())

#define a employee class with attributes role, department, &salary.
#showdetails()
#create a engineer class that inherits prop. from employee & has additional attributes: name and age

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        print("role:",self.role)
        print("department",self.department)
        print("salary",self.salary)
    
class Engineer(Employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT Infra",97668)

    def showdetails(self):
        # Add additional details to the showdetails method
        print("Name:", self.name)
        print("Age:", self.age)
        # Use the parent class's showdetails method
        super().showdetails()


engg1=Engineer("Sriram",22)
engg1.showdetails()


"""create a class called order.
    store the items and it's price. 
    use dender fuction __gt__() to convey that:
    order1 > order2 if price of order1 > price of order2"""

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self,order2):
        return self.price>order2.price
ord1=Order("chips",30)
ord2=Order("coke",20)
print(ord1>ord2)