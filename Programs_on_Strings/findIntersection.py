# Program to find the intersecting elements between two lists.

str = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

uni = []

for i in range(0, len(str[0])-1):
    for j in range(0, len(str[1])-1):
        if str[0][i] == str[1][j] and str[0][i] != ' ' and str[0][i] != ',':
            t = str[0][i]
            if t in uni:
                break
            else:
                uni.append(t)

print(uni)
print(len(uni))

