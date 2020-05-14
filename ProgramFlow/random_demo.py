# Demonstration of random module/package

import random

# # Basic code for random demo
# answer = random.randint(1, 10)
# print(answer)

# Creating guessing game

highest = 10
# answer = random.randint(1, highest)

# print("Please guess number 1 and {}:".format(highest))
# guess = int(input())
#
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
#
# # there is feature called todo: remove after testing
# # Its an IntelliJ feature not python
#
# # Acitivity: Create a program which allows users to guess continously
# # until they get the right answer. Also keep the count of guesses
# # and display at the end.
#
# highest = 10
# count = 0
#
# while True:
#     count += 1
#     answer = random.randint(1, highest)
#     print("Please guess number 1 and {}:".format(highest))
#     guess = int(input())
#
#     if guess == answer:
#         print("You got it first time")
#         break
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")
#         guess = int(input())
#         if guess == answer:
#             print("Well done, you guessed it")
#             break
#         else:
#             print("Sorry, you have not guessed correctly")
# print("You are out of the game. Total counts {}".format(count))


# Simplifying the above code
count = 0
answer = random.randint(1, highest)
print("Please guess number 1 and {}:".format(highest))
while True:
    count += 1 # Augmented Assignment - writing in reduce form. count = count + 1
    guess = int(input())
    if guess == 0:
        break
    if guess == answer and count == 1:
        print("Well done!! you got it in first guess.")
        break
    if guess == answer:
        print("Well done!! you guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
print("You are out of the game. Total counts {}".format(count))

