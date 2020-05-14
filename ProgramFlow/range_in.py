myname = "Irfan Khan"

letter = input("Please enter the letter: ")

if letter in myname.casefold():
    print("The letter {} is in {}".format(letter, myname))
else:
    print("I don't need that letter")
