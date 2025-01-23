def second_largest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements.")
    
    max_val = max(nums) 
    nums.remove(max_val)
    
    second_max = max(nums) 
    return print(second_max)

list1=[11,1,22,2,33,44,55,66,77]

second_largest(list1)