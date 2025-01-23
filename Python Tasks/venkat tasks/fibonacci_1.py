def fibonacci(n):
    sequence=[0,1]

    for i in range (2,n):
        new_number=sequence[-1]+sequence[-2]
        sequence.append(new_number)
    
    return print(sequence[:n])
fibonacci(0)
