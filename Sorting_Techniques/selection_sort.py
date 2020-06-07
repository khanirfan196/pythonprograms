# Program for selection sort
# Author : Irfan Khan Md.

l = [9, 5, 1, 6, 3, 7, 11, 2]

print(l)
print("Selection sort starts:")

for i in range(0, len(l)):
    lv = l[i]
    for n in range(i+1, len(l)):
        if lv > l[n]:
            lv = l[n]
            j = n
    if l[i] > lv:
        t = l[i]
        l[i] = lv
        l[j] = t
        print(l)

print("After selection sort:")
print(l)