#Welcome messages
print("Welcome to the Quidditch Roster Program")

#Definition of Position
keeper = input("\nWho is your keeper: ").title()
first_beater = input("Who is your first beater: ").title()
second_beater = input("Who is your second beater: ").title()
first_hunter = input("Who is your first hunter: ").title()
second_hunter = input("Who is your second hunter: ").title()
third_hunter = input("Who is your third hunter: ").title()
seeker = input("Who is your seeker: ").title()

#Original roster
print("\n\tYour starting 7 for the upcoming Quidditch season")
print("\t\tKeeper:\t\t\t" + keeper)
print("\t\tFirst Beater:\t\t" + first_beater)
print("\t\tSecond Beater:\t\t" + second_beater)
print("\t\tFirst Hunter:\t\t" + first_hunter)
print("\t\tSecond Hunter:\t\t" + second_hunter)
print("\t\tThird Hunter:\t\t" + third_hunter)
print("\t\tSeeker:\t\t\t" + seeker)

#Injured Player
print("\nOh no, " + first_hunter + " is injured.")
print("Your roster only has 6 players.")
new_hunter = input("Who will take " + first_hunter + "'s spot: ").title()

#New roster
print("\n Your starting 7 for the upcoming Quidditch season")
print("\t\tKeeper:\t\t\t" + keeper)
print("\t\tFirst Beater:\t\t" + first_beater)
print("\t\tSecond Beater:\t\t" + second_beater)
print("\t\tFirst Hunter:\t\t" + new_hunter)
print("\t\tSecond Hunter:\t\t" + second_hunter)
print("\t\tThird Hunter:\t\t" + third_hunter)
print("\t\tSeeker:\t\t\t" + seeker)

#Final announcement
print("\nGood luck " + new_hunter + " you will do great!")
print("Your roster now has 7 players.")
