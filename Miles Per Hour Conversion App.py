#Basic Data Types Challenge 2: MPH to MPS Conversion App

print("Welcome to the MPH to MPS Conversion App\n")

#Gather user input
mph = float(input("What is your speed in miles per hour: "))

#Convert to mps
mps = mph * 0.44704
print("Your speed in meters per second is " + str(round(mps,2)) + ".")
