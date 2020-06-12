# Program to demonstrate use of split function on string
# Author : Irfan Khan Mohammed

str = "this, string, is, separated, with, comma"
str2 = "abcbddefbgbhhibjb"
str3 = "string with simple blank spaces"

print(str)
print("Split func:")
print(str.split(","))

print()
print(str2)
print("Split func: (b)")
print(str2.split('b'))

print()
print(str3)
print("Split func: () - blank spaces")
print(str3.split(' '))
