# Lists Continuation

# Use of append() function to list

# menu = []
# menu.append(["milk", "banana", "cookie"])
# # the values got added to empty list menu[]
# print(menu)

# menu = []
# menu.append(["milk, banana, burger"])
# menu.append(["burger", "juice", "omlette"])
# menu.append(["banana", "milk", "coffee", "burger"])
#
# # using for loop to fetch list
#
# for meal in menu:
#     if not "burger" in meal:
#         print(meal)

# Activity: Video# 89
# Add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as did in lines 5-13


menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# the above list is from Monty Python List

print("Below is the entire menu")
print(menu)

print()
for meal in menu:
    if not "spam" in meal:
        print(meal)
        # printing each value in list seprately on single line
        for ingredient in meal:
            print(ingredient)














