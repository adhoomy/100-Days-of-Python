import random

humanChoice=int(input("Lets play Rock Paper Scissors!\nWhat do you choose? type 0 for rock, 1 for paper, and 2 for scissors\n"))
if humanChoice<0 or humanChoice>2:
    print("You gave an invalid choice, you lose.\n")

if humanChoice==0:
    print("    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n\n")
if humanChoice==1:
    print("    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)\n\n")
if humanChoice==2:
    print("    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)\n")

print("Computer chose:\n")
computerChoice=random.randint(0,2)
if computerChoice==0:
    print("    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n\n")
if computerChoice==1:
    print("    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)\n\n")
if computerChoice==2:
    print("    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)\n")

if humanChoice==computerChoice:
    print("Tie!\n")
if humanChoice==0 and computerChoice==2:
    print("You Win!\n")
if humanChoice==1 and computerChoice==0:
    print("You Win!\n")
if humanChoice==2 and computerChoice==1:
    print("You Win!\n")
if computerChoice==0 and humanChoice==2:
    print("You Lose!\n")
if computerChoice==1 and humanChoice==0:
    print("You Lose!\n")
if computerChoice==2 and humanChoice==1:
    print("You Lose!\n")