class student:
    name="karan kumar"
s1=student()
print(s1.name)

class students:
    def __init__(self,fullname):
        self.name=fullname

s2=students("srikanth")
s3=students("harshith")

print()
print(s2.name)
print(s3.name)

class college:
    college_name="HDFC School"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in the database:")
c1=college("Sriram",100)
print(c1.name)
print(c1.marks)
