# Program to perform simple linear search
# Author : Irfan Khan Mohammed

print("Linear Search Program")

my_list = [1, 3, 8, 9, 15, 17, 10, 25, 33, 7, 6]

print(my_list)
print("Enter number to search: ")
a = int(input())
i = 0

while i < len(my_list):
    if a == my_list[i]:
        print("Element found at index value {} ".format(i))
        break
    i += 1
else:
    print("Element not found")




