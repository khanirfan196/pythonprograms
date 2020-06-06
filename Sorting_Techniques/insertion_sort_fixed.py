# Program for Insertion sort.
# The previous code's logic was not correct.
# Author : Irfan Khan Md.

l = [9, 5, 1, 6, 3, 7, 11, 2]

for i in range(0, len(l)-1):
    if l[i] > l[i+1]:
        j = i + 1
        while j != 0:
            if l[j] < l[i]:
                t = l[i]
                l[i] = l[i+1]
                l[i+1] = t
                print(l)
            j -= 1
            i -= 1

print("After Insertion sort:")
print(l)