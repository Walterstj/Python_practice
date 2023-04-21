

name = input("What is you name ?")


age = 0
while age == 0:
    age_str = input("How old are you?")
    try:
        age = int(age_str)

    except:
        print("ERRORS: You need to put a number for age")

# print("and of the whileloop")

print("Your name is "+ name + ", you are " + str(age) + " years old")
print("next year you will have " + str(age+1) + " years")

