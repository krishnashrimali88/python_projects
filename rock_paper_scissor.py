#rock paper scissor

# rock beats scissor gets lost by paper
# paper beats rock gets lost by scissor 
# scissor beats paper gets lost by rock
# 1.rock
# 2.paper
# 3.scissor

import random

print("Welcome to rock, paper, scissor")
n = input("1.Rock,2.paper,3.scissor:")

user = int(n)

comp = random.randint(1,3)


def game(user,comp):
    if user ==  comp:
        print("draw!")

    elif user == 1 and comp ==  2 or user == 2 and comp == 3 or user == 3 and comp == 1:
        print("you lose")

    else:
        print("you won!")         


game(user,comp)       