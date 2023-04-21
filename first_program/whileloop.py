# 1)

# whileloop : "tant que"

n = 0   # create a variable
# print(n)
# n = 1   # reaffect a variable
# print(n)
# n = n + 1   # increment
# print(n)

print("start of the loop")

while n < 4:
    print("n value is: " + str(n))
    n = n + 1
    
print("end of the loop")


# 2)

password = ""
while not password == "toto":
    password = input("What is the password ? ")

print("correct password, you have access")
