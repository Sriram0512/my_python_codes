def max_min(numbers):
    
    if not numbers:
        return None, None 
    
    max_num = max(numbers)  
    min_num = min(numbers) 
    
    return print("maximum number is:",max_num,"minimum number is:", min_num)

num1=[1,2,34,56,78,90]

max_min(num1)

