# Program on finding Union elements between two lists.
# Implemented a function and passing lists as arguments which returns
# the list with union elements.

def FindIntersection(strArr1, strArr2):
    # Code goes here
    uni = []
    if len(strArr1) == 0 or len(strArr2) == 0:
        return "List(s) are empty"
    else:
        for i in range(0, len(strArr1)):
            for j in range(0, len(strArr2)):
                if strArr1[i] != strArr2[j]:
                    if strArr1[i] not in uni:
                        uni.append(strArr1[i])
                    if strArr2[j] not in uni:
                        uni.append(strArr2[j])

    uni.sort()
    return uni

list1 = [1, 2, 3, 5, 7]
list2 = [5, 6, 7, 3, 8]

# Calling the function
c = FindIntersection(list1, list2)
print(f"Intersecting Elements:",c)

