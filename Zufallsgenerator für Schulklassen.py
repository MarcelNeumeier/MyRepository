#Zufallsgenerator-Programm
import random

#Willkomensnachricht
print("Willkommen im Zufallsgenerator für Schulklassen!")
class_size = int(input("\nAus wie vielen Schülern besteht die Klasse? "))

running = True
while running:
    
    #Benutzereingabe
    pupil_num = int(input("Wieviele Schüler sollen ausgewählt werden? "))
    print("\nAusgewählt wurden die Schüler mit den folgenden Nummern:")

    #Generierung und Anzeige der zufällig ausgewählten Zahl
    pupils = []
    for pupil in range(pupil_num):
        random_num = random.randint(1, class_size)
        if random_num not in pupils:
            pupils.append(random_num)
    for i in pupils:
        print(i)

    choice = input("\nSollen noch weitere Schüler ausgewählt werden? (ja/nein): ").lower()
    if choice != "ja":
        running = False
        print("\nDanke für die Verwendung dieses Programms von Marcel Neumeier")
    
