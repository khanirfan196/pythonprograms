# Demonstration of 'Range()' function

# print(range(100))
# # this shows the range from 0 to 100.
# # but it does not print 1 to 100 numbers.
#
# my_list = list(range(10))
# print(my_list)
# # prints values from 1 to 10
#
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
#
# print(even)
# print(odd)

# Use of index() function.

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# # prints the position number of character 'e' in string
#
# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print('='*50)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100 ,-2):
#     print(i)

# back_string = "eguagnal lufrewop yrev a si nohtyP"
# print(back_string[::-1])
#
# r = range(0, 10)
# for i in r[::-1]:
#     print(i)

# Activity:
# Experiement with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#

o = range(0, 100 ,4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)
# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

