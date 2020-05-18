# Demonstration of basic Tuple

t = ("a", "b", "c")
# or
t = "a", "b", "c"
print(t)

print("a", "b", "c")
# the above print statement treat abc as a string
print(("a", "b", "c"))
# the above print statement treat abc as a tuple
# as two round brackets have used to print them

# Whatever is enclosed in round brackets is treated as tuples.
# this kind of notation/syntax helps in passing values to functions.
# Tuples are immutable objects. You cannot assign any new value like
# in lists or change any value.
# It supports indexing and slicing likewise in lists.
# Tuples holds items of heterogeneous category which never changes.
# list holds homogeneous items.
# But if a tuple contains one element as list and it has few elements in
# it, then the tuple can be change only on the list values as it is mutable
# but not on any other tuple elements.

# Below are the tuples which stores information of music albums
# and the author with release year.

welcome = "Welcome to my Nightmare", "Irfan Khan", 1975
bad = "Bac Company" "Bac Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallic = "Ride the Lightning", "Metallica", 1984

print(metallic)
print(metallic[0])
print(metallic[1])
print(metallic[2])

# the below assignment results in error
# metallic[0] = "Master of puppets"
# TypeError: 'tuple' object does not support item assignment
# Also you cannot even append any value using append() function
# like how it can be done using list as the tuples are immutable.

# list dynamic changing example
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
# print(type(metallica2))


# assigning individual tuple values to new variables.
# this is called unpacking the tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)


# Nesting tuple Demo

imrankhan = "Unforgettable", "Imran Khan", 2000, (1, "Satisfya"), (2, "Imaginary GF"), (3, "You will know")


 print(imrankhan)
#
 title, artist, year, tracks = imrankhan
 print(title)
 print(artist)
 print(year)
 print(tracks)

# or

# title, artist, year, track1, track2, track3 = imrankhan
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)

# Using for loop to print the sub-tuple values

imrankhan = "Unforgettable", "Imran Khan", 2000, (
    (1, "Satisfya"), (2, "Imaginary GF"), (3, "You will know"))

title, artist, year, tracks = imrankhan
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))


products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London')
            )

imelda = 'More Mayhem', 'Imelda May', 2011, [
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Mayhem'),
    (4, 'Kentish Town Waltz')]

imelda[3].append(5, 'All For You')
print(imelda[3])