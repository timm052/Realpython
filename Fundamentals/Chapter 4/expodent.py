# Perform calculations on user input
print('This program will ask you for 2 numbers and rasie the first number to the power of the second\n')

# get values user wishes to multiply
num_1_s = input("Enter first number:  ")
num_2_s = input("Enter the Second number:  ")

# convert to float
num_1 = float(num_1_s)
num_2 = float(num_2_s)

# return equation and result to user
print(f"{num_1_s}^{num_2_s} = {num_1 ** num_2}")
