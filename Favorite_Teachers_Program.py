#Lists Challenge 10: Favorite Teachers Programm

#Welcome message
print("Welcome to the Favorite Teachers Program")

#Define List
teachers = []

#Get user input and adding to list
first_favorite = input("\nWho is your first favorite teacher: ").title()
teachers.append(first_favorite)
second_favorite = input("Who is your second favorite teacher: ").title()
teachers.append(second_favorite)
third_favorite = input("Who is your third favorite teacher: ").title()
teachers.append(third_favorite)
fourth_favorite = input("Who is your fourth favorite teacher: ").title()
teachers.append(fourth_favorite)

#print lists
print("\nYour favorite teachers ranked are: " + str(teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(teachers, reverse = True)))

#print top teachers
print("\nYour top two teachers are: " + str(teachers[0]) + " and " + str(teachers[1]) + ".")
print("Your next two favorite teachers are: " + str(teachers[2]) + " and " + str(teachers[3]) + ".")
print("Your last favorite teacher is: " + str(teachers[3]) + ".")
print("You have a total of " + str(len(teachers)) + " favorite teachers.")

#definition new first favorite teacher
new_first_favorite = input("\nOops, " + str(teachers[0]) + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title()
#insert new first favorite teacher into existing list
teachers.insert(0, new_first_favorite)

print("\nYour favorite teachers ranked are: " + str(teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(teachers, reverse = True)))

#print top teachers
print("\nYour top two teachers are: " + str(teachers[0]) + " and " + str(teachers[1]) + ".")
print("Your next two favorite teachers are: " + str(teachers[2]) + " and " + str(teachers[3]) + ".")
print("Your last favorite teacher is: " + str(teachers[4]) + ".")
print("You have a total of " + str(len(teachers)) + " favorite teachers.")

#definition of removed teacher
teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())

print("\nYour favorite teachers ranked are: " + str(teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(teachers, reverse = True)))

#print top teachers
print("\nYour top two teachers are: " + str(teachers[0]) + " and " + str(teachers[1]) + ".")
print("Your next two favorite teachers are: " + str(teachers[2]) + " and " + str(teachers[3]) + ".")
print("Your last favorite teacher is: " + str(teachers[3]) + ".")
print("You have a total of " + str(len(teachers)) + " favorite teachers.")
