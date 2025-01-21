#methods are functions that belongs to objects

class students:
    def __init__(self,fullname):
        self.name=fullname
    def hello(self):
        print("hello", self.name)
ss1=students("sriram")
ss1.name
ss1.hello()

#creating a student class that takes names,marks of three subjects as arguments in constructor
# also creating a method to print the average

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi!",self.name,"your average score is:",sum/3)
s1=student("Harshith",[90,85,93])
s1.get_avg()

#static Methods
#methods that don't use self parameters
"""works at class levels"""

class college:
    @staticmethod #decorator
    def college_name():
        print("abc college")
# this is an example of how to use static method
""""decorator allows us to wrap another function in order to extend the behaviour of the wrapped fuction ,
     without permanently modified """

"""Abstracion:
     Hiding the implementation details of a class and only showing the essential features to the user.
     
    Encapsulation:
     wrapping data and functions into a single unit."""

class Account:
    def __init__(self,balance, accout_number):
        self.balance=balance
        self.account_number=accout_number

    def credit(self,amount):
        self.balance+=amount
        print("amount credited:",amount)
        print("remaining balance is:",self.get_balance())

    def debit(self,amount):
        self.balance-=amount
        print("amount debited:",amount)
        print("remaining balance is:",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(50000,"20311A0207")
acc1.balance
acc1.account_number
acc1.get_balance() 
acc1.credit(1000)
acc1.debit(5000)
acc1.credit(10050)


        
