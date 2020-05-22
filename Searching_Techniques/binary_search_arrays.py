# Demonstration of Binary Search Program.
# This program search element from the specified list.
# Total number of steps are calculated at every single search.
# Author : Irfan Khan Mohammed.

print("Program for Binary Search - Arrays")

# Test1 : Perform search with this list
# my_list = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
#           0,  1,  2,  3,  4,  5,  6,  7,  8,  9

# Test2 : Perform search with this list
my_list = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 63, 67, 75, 77, 81, 86, 88, 93, 96, 99, 1000]

# Calculating low, high, and mid values for the list (array values).
low = 0

high = len(my_list) - 1

mid = int((low + high) / 2)

print("Enter the element to find:")

a = int(input())

count = 0

while low != mid:
    count += 1
    if a == my_list[mid]:
        print(f"Element found at Index value:",mid)
        print(f'Total Steps:', count)
        break
    elif a > my_list[mid]:
        low = mid
        mid =int((low + high) / 2) + 1
    elif a < my_list[mid]:
        high = mid
        mid = int((low + high) / 2)
    if a == my_list[low]:
        print(f'Element found at Index value:',low)
        print(f'Total Steps:', count)
        break
    if mid > len(my_list) - 1:
        print("Element does not exists!!")
        print(f'Total Steps:', count)
        break
else:
    print("Element does not exists")
    print(f'Total Steps:', count)
