day = "Saturday"
temperature = 30
raining = True

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python")



if 0:
    print("True")
else:
    print("False")
name = input("Please enter your name: ")
#if name:
#or
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")