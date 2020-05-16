# Demonstration of Dictionaries and Sets
# Author : Irfan Khan Mohammed

# Dictionaries are like hash sets in java which stores
# values based on the key value pair. Another example is
# JSON files where data is bind with key value pair.
# We cannot use indexes here to retrieve values in dictionaries
# like in lists and tuples.
# We cannot use list in dictionaries.
# Values can be either string or integers or
# string with integers or wise versa.

# Basic dictionary

fruit = {"orange" : "a sweet citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a sour yellow citrus fruit",
         "grape" : "a small, sweet fruit gorowing in bunches",
         "lime" : "a sour, green citrus fruit"}
         #"apple" : "round and soft"}
         # Here the apple is getting updating/changed while the
         # dictionary is defined. Thus it will print the last
         # value for the key apple.

print(fruit)
print(fruit["lemon"]) # value is retrieved using the key which is lemon.

# adding new values (like appending in list)

fruit["pear"] = "an odd shaped apple"
print(fruit)
print(fruit["pear"])

# changing/updating value using key

fruit["lime"] = "great with tequila"
print(fruit)

# to delete any value in the dictionary
# del keyword is used and dictionary with key
# example below
# del fruit["lemen"]
# if proper key is not used with using 'del' it will
# delete the entire dictionary
# example below
# del fruit -- deletes entire dictionary

# Use clear() function to remove all the values along with keys
# so that the dictionary remains with no values.
# like TRUNCATE command in sql.

# Program to check the key available in dictionary

# while True:
#     dict_key = input("Please enter a fruit: ").casefold()
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)
# by default the code returns none if key not found.

# prints only keys
print(fruit.keys())
# prints only values
print(fruit.values())

# converting dictionary to tuple

f_tuple = tuple(fruit.items())
print(f_tuple)

# we can also use some tuple functions
print("Output for line 79")

f_tuple = tuple(fruit.items())
print(f_tuple)

print("Output for loop")

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

# turning the tuple again back to dictionary
print("output for line 89")
print(dict(f_tuple))
