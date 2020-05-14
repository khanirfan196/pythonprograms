#

numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("The numbers are acceptable")
# Above else statement is tied with for loop not with
# the 'if' statement. quite tricky!!

