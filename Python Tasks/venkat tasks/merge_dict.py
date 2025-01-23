def merge_dicts(dict1, dict2):
    dict = dict1.copy()  
    for key, value in dict2.items(): 
        if key in dict:
            dict[key] += value  
        else:
            dict[key] = value  
    return print(dict)

dictionary1 = {'a': 1, 'b': 2, 'c': 3}
dictionary2 = {'b': 3, 'c': 4, 'd': 5}

merge_dicts(dictionary1, dictionary2)
