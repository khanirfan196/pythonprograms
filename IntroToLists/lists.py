# Demonstration of Basic Lists

ipAddress = input("Please enter an IP address: ")
print(ipAddress.count("."))

parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]
for state in parrot_list:
    print("This parrat is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
number = even + odd
#number.sort()
# sort() sorts the number in ascending order
#print(number.sort())
# the above print statement will not work.
print(number)
print(sorted(number))
# sorted() function sorts the number and allows to
# print at the same time unlike sort() method.

numbers_in_order = sorted(number)

print(numbers_in_order)

if sorted(number) == numbers_in_order:
    print("The list values are sorted")
else:
    print("The list values are not sorted")

# We can create list in the following way
print(list("Irfan Khan"))

# Following contains:
# Adding list to another empty list
# Comparing lists and returning True if correct
# Reversing the list after sorting (descending order)

even = [2, 4, 6, 8]
another_even = even
print(another_even)
print(another_even == even) # Returns True as it is comparing the two lists.
another_even.sort(reverse=True)
print(another_even)

# Using for loop to fetch list

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd # adding two lists.

for number_set in numbers:
    print(number_set)



