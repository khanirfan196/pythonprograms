# Program to demonstrate Insertion sort

print("Insertion Sort:")

# Sample list 1
#a = [1, 4, 6, 5, 9, 13, 20, 16, 12, 15]

# Sample list 2
a = [2, 20, 10, 15, 9, 3, 4, 16, 21, 11]

t = 0

print(len(a))
for i in range(1, len(a)):
    while a[i-1] > a[i]:
    # Here we need to keep on swapping the i+1 element with the sorted sublist
        t = a[i-1]
        a[i-1] = a[i]
        a[i] = t
        i -= 1

print("After insertion sort:")
print(a)