# Program to print Arithmetic Series

series_list = []
print("Program for Arithmetic Series")

print("Enter the first number of series:")

a = int(input())
series_list.append(a)

print("Enter the common difference:")

d = int(input())

print("How many elements you want:")

n = int(input())

for i in range(1, n):
    t = a+(i * d)
    series_list.append(t)

print(series_list)

sum_series = (n * (series_list[0] + series_list[len(series_list)-1])) // 2

print(f"\nSum of the entire series:", sum_series)
