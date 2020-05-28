# Program to calculate factorial of a number.


print("Program for Fibonacci Series")

i = 1

fact = 1

print("Enter the number to print its factorial")

a = int(input())

if a == 1 or a == 0:
    print("Factorial is 1")
else:
    while i <= a:
        fact = fact * i
        i = i + 1
    print(f"Factorial is:",fact)