light=input("light colour:")
if (light=="red"):
    print("stop")
elif(light=="yellow"):
    print("get ready")
elif(light=="green"):
    print("go")
else:
    print("light is broken")


#string functions

string="i am linux engineer."
print(string.endswith("eer."))
print(string.capitalize())
print(string.replace("linux", "senior linux"))
print(string.find("am"))
print(string.count("am"))

#lists and it's functions
student=["srikanth",25,"kodangal"]
print(len(student))
student.append(45)
print(student)
student.reverse()
print(student)
student.insert(1,25000)
print(student)
student.remove(25000)
print(student)
student.pop(2)
print(student)

#tuple and it's fuction

tup=(87,64,33,95,76)
print(tup[0])
print(tup.index(76))
print(tup.count(2))

#strings and tuples are immutable , and lists are mutable

#dictionaries and it's methods
dict={
    "name":"harshith",
    "age":21,
    "marks": [99,98,93]
      }

print(dict["name"],dict["marks"],dict["age"])
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("marks"))
