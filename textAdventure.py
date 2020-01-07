#Author:    Johannes R. Falnes
#Date:      2019

import time
import random
from caves import firstCave
from forests import firstForest

def startGame():
    start = input(
        "Welcome to Text Based Adventure Game No. 1! What do you want to do? \n1.Explore the forest\n2.Explore the cave")
    if start == "1":
        print("You enter the forest!")
        firstForest()
    if start == "2":
        firstCave()
startGame()


