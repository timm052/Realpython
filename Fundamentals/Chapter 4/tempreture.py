# Convert Tempretures


def c2f(temp):
    '''Coverts Celsius to Fahrenheit and returns raw numerical value'''
    return temp * 9 / 5 + 32


def f2c(temp):
    '''Coverts Fahrenheit to Celsius and returns raw numerical value'''
    return (temp - 32) * 5 / 9


cel = 37
fah = 72

print(f"{cel} degrees C = {c2f(cel)} degrees F")
print(f"{fah} degrees F = {f2c(fah)} degrees C")
