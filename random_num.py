import random

round = input("Enter the number of rounds:")
round1 =  int(round)
print("Enter the number from 1-10:")    

def guess():
    guesses = input()
    guessed = int(guesses)
    num = random.randint(1,10)

    if guessed == num:
        print("you won")

    else:
        print("Better luck next time")



for i in range(1,round1):
    guess()
