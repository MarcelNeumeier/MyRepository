print("Welcome to the Multiplication/Exponent Table App")
#user input
name = input("\nHello, what is your name: ").title().strip()
number = float(input("What number would you like to work with: ")) 
print ("\nMultiplication Table For " + str(number))
#calculations multiplications
one = 1 * number
one = round(one , 2)
two = 2 * number
two = round(two , 2)
tree = 3 * number
tree = round(tree , 2)
four = 4 * number
four = round(four , 2)
five = 5 * number
five = round(five , 2)
six = 6 * number
six = round(six , 2)
seven = 7 * number
seven = round(seven , 2)
eight = 8 * number
eight = round(eight , 2)
nine = 9 * number
nine = round(nine , 2)
print("\n\t1.0 * " + str(number) + " = " + str(one))
print("\t2.0 * " + str(number) + " = " + str(two))
print("\t3.0 * " + str(number) + " = " + str(tree))
print("\t4.0 * " + str(number) + " = " + str(four))
print("\t5.0 * " + str(number) + " = " + str(five))
print("\t6.0 * " + str(number) + " = " + str(six))
print("\t7.0 * " + str(number) + " = " + str(seven))
print("\t8.0 * " + str(number) + " = " + str(eight))
print("\t9.0 * " + str(number) + " = " + str(nine))
print("\nExponent Table For " + str(number))
#calculations exponents
powone = number ** 1
powtwo = number ** 2
powtree = number ** 3
powfour = number ** 4
powfive = number ** 5
powsix = number ** 6
powseven = number ** 7
poweight = number ** 8
pownine = number ** 9
#round to four digits
powone = round(powone, 4)
powtwo = round(powtwo, 4)
powtree = round(powtree, 4)
powfour = round(powfour, 4)
powfive = round(powfive, 4)
powsix = round(powsix, 4)
powseven = round(powseven, 4)
poweight = round(poweight, 4)
pownine = round(pownine, 4)
print("\n\t" + str(number) + " ** 1 = " + str(powone))
print("\t" + str(number) + " ** 2 = " + str(powtwo))
print("\t" + str(number) + " ** 3 = " + str(powtree))
print("\t" + str(number) + " ** 4 = " + str(powfour))
print("\t" + str(number) + " ** 5 = " + str(powfive))
print("\t" + str(number) + " ** 6 = " + str(powsix))
print("\t" + str(number) + " ** 7 = " + str(powseven))
print("\t" + str(number) + " ** 8 = " + str(poweight))
print("\t" + str(number) + " ** 9 = " + str(pownine))
print("\n" + name.capitalize() + " Math is cool!")
print("\t" + name.lower() + " math is cool!")
print("\t\t" + name.capitalize() + " Math Is Cool!")
print("\t\t\t" + name.upper() + " MATH IS COOL!")
