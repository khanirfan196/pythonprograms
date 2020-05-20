# Program to demonstrate bubble sort
# Author : Irfan Khan Mohammed

my_list = [1, 8, 9, 3, 6, 11, 20, 12, 15, 30, 45, 50, 23, 5, 4, 14, 16]

print("list order: ")
print(my_list)

lt = len(my_list)-1

for i in range(lt):
    for j in range(lt):
        if my_list[j] > my_list[j+1]:
            var = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = var
            var = None

print("Sorted List is :")
print(my_list)