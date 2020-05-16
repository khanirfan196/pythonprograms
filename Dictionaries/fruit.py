

fruit = {"orange" : "a sweet citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a sour yellow citrus fruit",
         "grape" : "a small, sweet fruit gorowing in bunches",
         "lime" : "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage" : "every child's favorite",
       "sprouts" : "mmm, lovely",
       "spinach" : "can I have some more fruit, please"}

print(veg)

# use of update method to combine two dictionaries

veg.update(fruit)
print(veg)

fruit.update(veg)
print(fruit)

# Assigning entire dictionary to a new variable
print("output for nice and nasty")
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)