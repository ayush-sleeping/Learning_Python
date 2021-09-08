# Stone, Paper, Sissors Game in Python...

import random

def gamewin(comp , you):
    if comp == "Stone":
        if you == "Paper":
            return True
        elif you == "Sisor":
            return False
    elif comp == "Paper":
        if you == "Sissor":
            return True
        elif you == "Stone":
            return  False
    elif comp == "Sissor":
        if you == "Stone":
            return True
        elif you == "Paper":
            return False

print("comp will chose from Stone(S) , Paper(P) and Sissors(R)" )
randNo = random.randint(1,3)

if randNo == 1:
    comp = "Stone"
elif randNo == 2:
    comp = "Paper"
else:
    comp = "Sissor"
    
you = input("Choose a sing from Stone(S) , Paper(p) and Sissors(R)")
a = gamewin(comp , you)

print(f"The computer choosed : {comp}")
print(f"You choosed : {you}")

if comp == you:
    print("the game is a tie")
elif a:
    print("You win")
else:
    print("you loose")
gamewin(comp , you)
