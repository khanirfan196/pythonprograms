# Demonstration of 'While' loop

# for i in range(0, 10):
#     print(i)

# Implementing same solution in while loop

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

#if i += 1 is not written under while loop
# then the loop continue to execute.
# Also while True condition continues the loop infinitely.

availabe_directions = ["north", "south", "east", "west"]
chosen_direction = ""

while chosen_direction not in availabe_directions:
    chosen_direction = input("Please enter the direction: ")

print("You are out of the loop...")

# Break and Continue keywords in while loop

while chosen_direction not in availabe_directions:
    chosen_direction = input("Please enter the direction: ")
    if chosen_direction.casefold() == "quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you got out of there")


# Acitivity to print numbers divisible by 11.
for i in range(0, 100, 7):
    if i>0 and i % 11 == 0:
        print(i)
        break

# Activit to print numbers that aren't divisible by 3 or 5.
for i in range(0, 20):
    if (i%3 == 0 or i%5 == 0):
        continue
    print(i)



