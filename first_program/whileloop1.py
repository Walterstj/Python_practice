

name = input("What is you name ?")


next_year = 0
while next_year == 0:
    age = input("How old are you?")
    try:
        next_year = int(age) + 1

    except:
        print("ERRORS: You need to put a number for age")

# print("and of the whileloop")

print("Your name is "+ name + ", you are " + str(age) + " years old")
print("next year you will have " + str(next_year) + " years")

