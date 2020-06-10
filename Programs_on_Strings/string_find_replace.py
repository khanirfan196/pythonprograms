# Program to demonstrate use of find() and replace() functions.
# Author : Irfan Khan Mohammed

str = "Apple's color is red"
str2 = "Color of grapes is green"

print(str)
print()

a = str.find("color")
print("Use of find func:")
print(f"Index of word 'color' is ", a)
print(f"Index of letter 's' is", str.index('s'))
print()

print(str2)
print("Replace func:")
print(str2.replace("grapes", "watermelon"))


