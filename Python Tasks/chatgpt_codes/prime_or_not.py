num= int(input("enter a number:"))

def prime(n):
    if n<=1:
        return print('it is not a prime number')
    
    for i in range(2,n):
        if (n%i)==0:
            print('not a prime number')
            break
    else:
        return print('prime number')

prime(num)