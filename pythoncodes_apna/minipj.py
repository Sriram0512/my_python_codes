#Guess the number
import random
target=random.randint(1,100)
while True:
    userchoice=input("Guess the number or Quit(q):")
    if (userchoice=="q"):
        break
    userchoice=int(userchoice)
    if (userchoice == target):
        print("Success: Correct Guess")
        break
    elif (userchoice<target):
        print("your no. was too small. Take a bigger guess")
    else:
        print("your no. was too big. Try taking a smaller one")
print("___***GAME OVER***___")

#Random password generator

import random
import string

pass_len=int(input("enter the length of the password that you want to set:"))
charval=string.ascii_letters+string.digits+string.punctuation
Password=""
for i in range(pass_len):
    Password+=random.choice(charval)
print("your random password is",Password)

#other way to generate password

import random
import string

Pass_len=int(input("enter the length of the password that you want to generate:"))
charvalues=string.ascii_letters+string.digits+string.punctuation
#list comprehension[function for i in range(n)]
password = "".join([random.choice(charvalues) for i in range(Pass_len)])
print("your random password is:",password)

#.join - concatenate any number of strings