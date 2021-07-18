#welcome message
print("Welcome to the Grade Sorter App")
#gather user input
first_grade = int(input("\nWhat is your first grade (0-100): "))
second_grade = int(input("What is your second grade (0-100): "))
third_grade = int(input("What is your third grade (0-100): "))
fourth_grade = int(input("What is your fourth grade (0-100): "))
#definition of list "grades"
grades = [first_grade, second_grade, third_grade, fourth_grade]
#print "grades"
print("\nYour grades are: " + str(grades))
#define reverse sorted grades
sorted_grades = sorted(grades, reverse=True)
#print sorted grades
print("\nYour grades from highest to lowest are: " + str(sorted_grades))
print("\nThe lowest two grades will now be dropped.")
#remove and print the two lowest grades
print("Removed grade: " + str(sorted_grades.pop(3)))
print("Removed grade: " + str(sorted_grades.pop(2)))
#print remaining grades
print("\nYour remaining grades are: " + str(sorted_grades))
#print highest grade
print("Nice work! Your highest grade is a " + str(sorted_grades[0]) + ".")
