#Author:    Johannes R. Falnes
#Date:      2020

def road():
    viewSign = input("You're now on the kingsroad.\nInfront of you there is a sign. Press A to view it.")
    if viewSign == "A":
        print("------------------------------")
        print("|                            |")
        print("|<------FOREST & CAVES       |")
        print("|           CASTLE------>    |")
        print("|                            |")
        print("------------------------------")
        chooseRoad = input("What direction do you want to go?")
        if chooseRoad == "Left":
