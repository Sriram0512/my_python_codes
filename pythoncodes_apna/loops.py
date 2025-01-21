#loops are used to repeat the instructions
#while loop

i=1
while i <=5:
    print(i)
    i+=1

print()

#for loop
list=[69,1,2,3,4,5]
for el in list:
    print(el)
else:
    print("end")
for el in range (5):
    print (el)
for el in range (1,5):
    print(el)
for el in range(1,10,2):
    print(el)
print()

#wap to find the sum of first n numbers
#using while

n=int(input("enter the number:"))
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print ("total sum :",sum)

print()

#using for
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum =",sum)

print()

#wap to find the factorial of first n numbers
#using while
n = int(input("enter the number:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)

#for loop
n=int(input("enter the number:"))
fact=1
for i in range (1,n+1):
    fact*=i
print("factorial =",fact)
