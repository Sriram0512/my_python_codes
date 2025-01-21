 #fuctions a block of statements that performs some task
def sum(a,b):
    s=a+b
    return s
print(sum(3,4))

movies=["kalki 2898AD","devara","batman","the dark knight"]
cities=["hyderabad","khammam","delhi","banglore"]
def print_len(list):
    print(len(list))

print_len(movies)
print_len(cities)

def printlist(list):
    for items in list:
        print(items,end=" , ")
printlist(movies)

#waf to find the factorial of n.
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)
print(cal_fact(4))

#waf to convert USD to INR
def convert(usd_val):
    inr_val=usd_val*82
    print(usd_val,"USD=",inr_val,"INR")
print(convert(10))

#recursion
#print n to 1 backwards
def shown(n):
    if (n==0):
        return
    print(n)
    shown(n-1)
print(shown(10))

#for n!
def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))

#write a recursive function to calculate sum of n natural numbers
def cal_sumn(n):
    if (n==0):
        return 0
    return cal_sumn(n-1) + n
print(cal_sumn(10))

#write a recusive function to print all elements in the list
fruits=["mangoes","bananas","apples","guava"]
def printfln(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    printfln(list,idx+1)
printfln(fruits)
