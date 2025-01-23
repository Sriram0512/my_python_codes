def fibonacci(n):
    if n<=0:
        return print([])
    elif n==1:
        return print([0])
    
    sequence=[0,1]
    a,b=0,1
    for i in range (2,n):
        a,b=b,a+b
        sequence.append(b)
    

    print(sequence)
fibonacci(1)