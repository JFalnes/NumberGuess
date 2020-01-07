#Author:    Johannes R. Falnes
#Date:      2019
import time
import random
from outside import road
chest = random.randint(0, 3)

def firstCave():
    chestItem = ["Magic Sword", "Magic Shield", "Health Potion", "Nothing"]
    inventory = []
    print("You enter the cave...")
    time.sleep(1)
    openChest = input("In front of you, there is a chest. Do you want to open it? Y/N")
    if openChest == "Y":
        print("You open the chest...")
        time.sleep(0.5)
        if chest == 0:
            print("The chest contains ", chestItem[0], "! Congratulations.")
            inventory.append(chestItem[0])
            print(inventory)
        elif chest == 1:
            print("The chest contains ", chestItem[1], "! Congratulations.")
            inventory.append(chestItem[1])
            print(inventory)
        elif chest == 2:
            print("The chest contains ", chestItem[2], "! Congratulations.")
            inventory.append(chestItem[2])
            print(inventory)
        elif chest == 3:
            print("The chest contains ", chestItem[3], "! Congratulations.")
            inventory.append(chestItem[3])
            print(inventory)
    exitCave = input("There seems to be little else of interest in this cave, do you want to exit? Y/n")
    if exitCave == "Y":
        print("You exit the cave...")
        time.sleep(0.5)
        road()
    elif exitCave == "N":
        print("Alright, take a look around.")

def secondCave():
    print("This cave is bigger, but does not seem to contain any loot. \nBehind you you hear a sound.")