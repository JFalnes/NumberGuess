#Author:    Johannes R. Falnes
#Date:      2019

from random import randint
import time

start = True
score = 0
wrongGuess = 0
while start == True:
    t = randint(1,10)
    print(t)

    numGuess = input("Guess a number between 1 and 10: ")
    guessNum = int(numGuess)

    if guessNum == t:
        print(t, ":", guessNum, "\nYour number was correct!")
        score = score + 1
        print("You have ", score, " correct guesses!")
    elif guessNum != t:
        print(t, ":", guessNum, "\nYour number was incorrect!")
        wrongGuess = wrongGuess + 1
        print("You have ", wrongGuess, "/3 wrong guesses!")
    elif guessNum == "":
        print("Please senor... not this")
    if wrongGuess >= 3:
        print("You lose!")
        time.sleep(1)
        start = False
    if score == 3:
        print("You win!")
        start = False
        startAgain = input("Do you want to play a game?" )
        if startAgain == "yes":
            start = True


