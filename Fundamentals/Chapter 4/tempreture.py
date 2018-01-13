# Convert Tempretures


def celtofah(temp):
    '''Coverts Celsius to Fahrenheit and returns raw numerical value'''
    return temp * 9 / 5 + 32


def fahtocel(temp):
    '''Coverts Fahrenheit to Celsius and returns raw numerical value'''
    return (temp - 32) * 5 / 9


cel = 37
fah = 72

print(f"{cel} degrees C = {celtofah(cel)} degrees F")
print(f"{fah} degrees F = {fahtocel(fah)} degrees C")
