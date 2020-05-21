# A simple demonstration of Binary Search with a list.
# This program is just to have an idea of Binary Search.
# Binary Search divides the list into low and high sections and
# then performs the search. Here the search is performed without an array.
# As the list keeps on growing, the number of steps keeps on increasing.

print("Program for binary search")

# Test1 : Perform search with this list
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Test2 : Perform search with this list
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Test3 : Perform search with this list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#            21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#            41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


# Test4 : Perform search with this list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print("Enter number to search")

a = int(input())

low = 1

high = len(my_list)

mid = int((high + low) / 2)

if a < low or a > high:
    print("Number does not exists in list")
else:
    count = 0
    while True:
        if a == mid or a == low or a == high:
            print(f'Answer is:',a)
            print(f'Total Steps:',count)
            break
        elif a > mid:
            low = mid
            mid = int((high + low) / 2)
            print("elif 1")
            print(low)
            print(mid)
            count += 1
        elif a < mid:
            high = mid
            mid = int((high + low) / 2)
            print("elif 2")
            print(high)
            print(mid)
            count += 1
        else:
            pass