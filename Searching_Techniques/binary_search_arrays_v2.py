# Demonstration of Binary Search Program.
# This program search element from the specified list.
# Total number of steps are calculated at every single search.
# Author : Irfan Khan Mohammed.
# Improved the Code Design.
# Redundant code is removed.

print("Program for Binary Search - Arrays - Version 2")

my_list = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 63, 67, 75, 77, 81, 86, 88, 93, 96, 99, 1000]

low = 0

high = len(my_list) - 1

print("Enter the element to find:")

a = int(input())

count = 0

while low <= high:
    mid = int((low + high) / 2)
    if a == my_list[mid]:
        print(f"Element found at Index value:",mid)
        print(f'Total Steps:', count)
        break
    elif a > my_list[mid]:
        count += 1
        low = mid + 1
    elif a < my_list[mid]:
        count += 1
        high = mid - 1
else:
    print("Element does not exists")
    print(f'Total Steps:', count)
