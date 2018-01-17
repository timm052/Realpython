# Find the factors of a Number
number = 0

print("This program will find all the factors of a number")
number = int(input("Enter a Number: "))

for i in range(1, int(number/2) + 1):
    result = number % i
    if result == 0:
        times = int(number/i)
        print(f"{i} is a divisor of {number} and divides {times} times")

print(f"{number} is a divisor of {number} and divides 1 time")
