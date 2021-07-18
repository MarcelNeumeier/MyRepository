#welcome message
print("Welcome to the Temperature Conversion Program\n")
#definition of input fahrenheit
fahrenheit = float(input("What is the given temperature in degrees Fahrenheit: "))
fahrenheit = round(fahrenheit, 4)
print("\nDegrees Fahrenheit:\t" + str(fahrenheit))
#definition of celsius
celsius = (fahrenheit - 32) * 5 / 9
celsius = round(celsius, 4)
print("Degrees Celsius:\t" + str(celsius))
#definition of kelvin
kelvin = (fahrenheit + 459.67) / 1.8
kelvin = round(kelvin, 4)
print("Degrees Kelvin:\t\t " + str(kelvin))
