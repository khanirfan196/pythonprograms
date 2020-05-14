# Write a program which gives users list of options
# to choose from and print out message if right option
# is selected. Also give an option to exit the program

# Challenge - Video 81

# Author - Irfan Khan Mohammed
# Concepts Used:
#   - Lists
#   - For and While loops
#   - IF and ELSE conditions
#   - Some regular string functions
# ------------------------------------------------------------

options_list = ["Learn", "Play", "Swimming", "Adventure", "TV"]
user_option = ""

print("""Please choose your option from the list below: 
Enter 0 to terminate game""")
for i in range(len(options_list)):
    print("{}. {} ".format(i + 1, options_list[i]))

while True:
    # while user_option not in options_list:
    user_option = input().casefold()
    if user_option == "0":
        print("You are out of the game")
        break
    else:
        if user_option == options_list[0].casefold():
            print("{} Python from Udemy".format(options_list[0]))
        elif user_option == options_list[1].casefold():
            print("{} outside of the house".format(options_list[1]))
        elif user_option == options_list[2].casefold():
            print("Go to {} at club".format(options_list[2]))
        elif user_option == options_list[3].casefold():
            print("Packup for {} at park".format(options_list[3]))
        elif user_option == options_list[4].casefold():
            print("Watch {} at home".format(options_list[4]))
        else:
            print("Enter Valid option")
