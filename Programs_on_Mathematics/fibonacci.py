# Program to print Fibonacci Series

print("Fibonacci Series:")

i = 0

b = 1

sum = 0

a = 0

print("Enter the number of elements to print")

n = int(input())

while(a <= n):
    a += 1
    i = b
    b = sum
    sum = i + b
    print(sum)