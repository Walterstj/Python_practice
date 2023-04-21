

# First program
"""Python training
leanning programation"""

name = input("What is you name ?")
age = input("How old are you?")

try:
    next_year = int(age) + 1
except:
    print("ERRORS: You need to put a number for age")

else:
    print("Your name is "+ name + ", you are " + str(age) + " years old")
    print("next year you will have " + str(next_year) + " years")
