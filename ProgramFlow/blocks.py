# Python Blocks

# the blocks in python is started with : symbol as it does not
# have any {} braces or BEGIN and END statements to open or close the blocks.

for i in range(1, 13):
    print("No. {} squared is {} and cube is {:4}".format(i, i ** 2, i ** 3))
print("*" * 80)
# the last print statement is not under the for loop as it is not indented.

for i in range(1, 13):
    print("No. {} squared is {} and cube is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)
# the last print statement is including in the loop.

# The IF Statement

name = input("What's your name: ")
age = int(input("How old are you {0} ".format(name)))
print(age)
if age == 100:
    print("Sorry, you gotta die soon")
# Including ELIF statement.
elif age < 18:
    print("You are not eligible to vote")
    print("Please come back in {0} years".format(18 - age))
    # Including ELSE statement.
else:
    print("You are eligible to vote")







