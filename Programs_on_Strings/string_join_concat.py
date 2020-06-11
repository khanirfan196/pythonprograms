# Program to demonstrate join() func and concatenating strings
# Author : Irfan Khan Md.

str1 = "Lemon is yellow in color"
str2 = "It is sour in taste"
str3 = "Hello, I am Python"

print(str1)
print(str2)
print("After concatenating two strings:")
print(str1+"." + " "+ str2)

print()
print(str3)
print("Join func: white space")
print(" ".join(str3))
print("Join func: use of ':'")
print(":".join(str3))