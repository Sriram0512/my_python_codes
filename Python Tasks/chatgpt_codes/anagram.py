str1=input("enter a string: ")
str2=input("enter a string: ")

def check(s1,s2):
    if sorted(s1)==sorted(s2):
        print("it's an anagram")
    else:
        print("not an anagram")

check(str1,str2)
