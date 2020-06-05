# Program on finding intersecting elements between two lists.
# Implemented a function and passing lists as arguments which returns
# the intersecting elements.

def FindIntersection(strArr1, strArr2):
    # Code goes here
    inter = []
    for i in range(0, len(strArr1)):
        for j in range(0, len(strArr2)):
             if strArr1[i] == strArr2[j]:
                if strArr1[i] in inter:
                    pass
                else:
                    inter.append(strArr1[i])
    if len(inter) == 0:
        return "No value matches"
    else:
        inter.sort()
        return inter

list1 = [1, 3, 4, 5, 6, 7, 8]
list2 = [1, 7, 8, 9]

# Calling the function
c = FindIntersection(list1, list2)
print(f"Intersecting Elements:",c)

