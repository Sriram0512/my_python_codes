str=input("enter a word:")

def rev_string(str):
    new_string=""
    for char in str:
        new_string= char + new_string
    return print(new_string)

rev_string(str)

