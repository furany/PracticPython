#Guess the number game
import random

print("Hello. What is your name?")
name = input()

print("Well, " +name +" I am thinking of a number between 1-20")
secretNumber = random.randint(1,20)

for guessesTaken in range (1, 7):
    print("take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Too low")
    elif guess > secretNumber:
        print("Too high")
    else:
        break #condition for right guess
if guess == secretNumber:
    print("Good job " + name +" You guessed in " + str(guessesTaken))
else:
    print("Nope it was " +str(secretNumber))
    

print("you took " + str(guessesTaken)+" guesses")
