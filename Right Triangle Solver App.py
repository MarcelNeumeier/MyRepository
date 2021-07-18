#import library
import math
#welcome message
print("Welcome to the Right Triangle Solver App")
#gather user input
first_leg = float(input("\nWhat is the first leg of the triangle: "))
second_leg = float(input("What is the second leg of the triangle: "))
#calculate and round hypotenuse
hypotenuse = math.sqrt(math.pow(first_leg, 2) + math.pow(second_leg, 2))
hypotenuse = round(hypotenuse, 3)
#calculate and round area
area = 0.5 * first_leg * second_leg
area = round(area, 3)
#output results
print("\nFor a triangle with legs of " + str(first_leg) + " and " + str(second_leg) + " the hypotenuse is " + str(hypotenuse) + ".")
print("For a triangle with legs of " + str(first_leg) + " and " + str(second_leg) + " the area is " + str(area) + ".")
 
