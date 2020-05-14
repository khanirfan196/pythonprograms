# Simple for loop using range
print("Simple for loop")
for i in range(1, 20):
    print("is is now {}".format(i))
print()
# if we do not provide the starting value in
# range the default is taken as zero.
print("Output - no first value in range")
for i in range(10):
    print(i)
print()


# Skipping one value while printing from 0.
# forward loop
print("Output - skipping one value")
for i in range(0, 10, 2):
    print(i)
print()

print("Output - skipping one value, reverse loop")
# Skipping one value but in reverse direction
for i in range(10, 0, -2):
    print(i)


# Activity printing all the numbers from 0 to 100
# which are divisible by 7. Include 0 in putput.

for i in range (0, 100):
    if i % 7 == 0:
        print("Numbers Divisible by 7 are {}".format(i))
        #or
        print(i)


