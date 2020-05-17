# Demonstration of Iteration on sequence/string

string = "1234567890"
#
# for char in string:
#     print(char)


# Using iter() and next() functions

my_iterator = iter(string)
print(my_iterator)
# the above print statement prints the memory location of string variable
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print()

# Activity: Video# 90

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print next item.
# Hint: Use the len() function to get the length of the string.
print("Output for the Activity")

my_list = ["irfan", "rahman", "farhan", "uneera", "sidra", "nafeesa"]

new_iterator = iter(my_list)

for i in range(len(my_list)):
    print(next(new_iterator))
# or
for i in my_list:
    print(i)

# --------------------------------------------------------------------------