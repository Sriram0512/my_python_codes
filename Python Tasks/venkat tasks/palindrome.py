string=input('enter a string:')

def palindrome(word):
    if word==word[::-1]:
        print('palindrome')
    else:
        print('not a palindrome')

palindrome(string)
