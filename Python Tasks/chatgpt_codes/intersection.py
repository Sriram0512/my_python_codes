list1=eval(input('enter the elements list1:'))
list2=eval(input('enter the elements in list2:'))

def intersection_of_2_lists(a,b):
    
    return print(list(set(a).intersection(set(b))))

intersection_of_2_lists(list1,list2)