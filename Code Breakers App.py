#Dictionaries Challenge 25: Code Breakers App

from collections import Counter

print("Welcome to the Code Breakers App")

#list of elements to remove from all text for analysis
non_letters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", "?", "!", ",", '"', "'", ":", ";", "(", ")", "%", "$", "&", "#", "\n", "\t", "+", "-", "_", "—"]

#Comment out user input for key_phrase_1
#Information for the first key: key_phrase_1
#key_phrase_1 = input("\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()

#Hard code a pre-determined key_phrase_1 for communication purposes
key_phrase_1 = "Once there was a man who had a wife and daughter. He loved his wife and daughter dearly, for they were both kind and loving. Sadly, his wife died before she was thirty years old. Soon the man decided to marry again. His new wife was not kind like the first, but proud and cruel. She also had two daughters, who were just like her. She did not like her new daughter at all, who was much kinder and prettier than herself and her daughters. So the poor girl was given the dirtiest work in the house. She had to scrub dishes and floors. She was made to clean out the fireplaces. She was treated like a slave. Her sisters had fine rooms to sleep in, with lovely, soft beds. But she only had a small, cold room in the attic, and her bed was made of straw."
key_phrase_1 = key_phrase_1.lower()

#Removing all non letters from key_phrase_1
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, "")

total_occurrences = len(key_phrase_1)

#Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)

#Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t"+ str(percentage) + "%")

#make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

#print the list
print("\nLetters ordered form highest occurrence to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end="")

#Comment out user input for key_phase_2
#Information for the second key: key_phrase_2
#key_phrase_2 = input("\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()

#Hard code a pre-determined key_phrase_2 for communication purposes.
key_phrase_2 = "Professor Hallberg-Smith teaches a hybrid course in econometrics. Instead of using an expensive textbook, she posts course content in Brightspace that she herself wrote. During class sessions students work in groups to solve and review problem sets, and she takes questions about the readings and the problems. Hallberg-Smith has not had time to create her own problem sets for the course; instead she uses problems from the textbook Introduction to Econometrics written by James H. Stock. Aware of the high cost of this book, Professor Hallberg-Smith does not want students to have to buy it just for the problem sets, so she scans the problems to PDF and posts them in Brightspace for students to download and use. Is this fair use?"
key_phrase_2 = key_phrase_2.lower()

#Removing all non letters from key_phrase_2
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, "")

total_occurrences = len(key_phrase_2)

#Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_2)

#Determine the frequency analysis for the message
print("\n\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t"+ str(percentage) + "%")

#make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])

#print the list
print("\nLetters ordered form highest occurrence to lowest: ")
for letter in key_phrase_2_ordered_letters:
    print(letter, end="")

#encode/decode a given message using key_phrase_1 and key_phrase_2
choice = input("\n\nWould you like to encode or decode a message: ").lower()
phrase = input("What is the phrase: ").lower()

#Removing all non letters from the users phrase
for non_letter in non_letters:
    phrase = phrase.replace(non_letter, "")

#user wants to encode a message
if choice == "encode":
    encoded_phrase = []
    for letter in phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)

    print("\nThe encoded message is: ")
    for letter in encoded_phrase:
        print(letter, end="")

#user wants to decode a message
elif choice == "decode":
    decoded_phrase = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)

    print("\nThe decoded message is: ")
    for letter in decoded_phrase:
        print(letter, end="")

#user entered an invalid option
else:
    print("Please type 'encode' or 'decode'. Try again.")
        
