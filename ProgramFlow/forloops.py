parrot = "Norwegian Blue"

for character in parrot:
    print(character)



numbers = "9,233;372:0336 854,775;807"
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

print (separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


# Taking input from user

numbers = input("Please enter a series of numbers separated by characters: ")
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

#print (separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# Activity for fetching Capital letters in string

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

new_quote =""

for char in quote:
    if char.isupper():
        new_quote = new_quote + char

print(new_quote)



