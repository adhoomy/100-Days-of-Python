from replit import clear
import art
import random

def sumOfCards(listOfCards):
    sum = 0
    for card in listOfCards:
        sum += card
    return sum

def printFinals(userCards, compCards, userCardSum, compCardSum):
    print(f"Your hand is {userCards}, with a score of {userCardSum}.")
    print(f"Computer's hand is {compCards}, with a score of {compCardSum}.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards are not removed from deck when drawn
# each card in list will have equal probability even if drawn previously

def blackjack(cards):
        clear()
        print(art.logo)
        userCards = [cards[random.choice(cards)], cards[random.choice(cards)]]
        userCardSum = sumOfCards(userCards)
        print(f"Your cards are: {userCards}, current score is: {userCardSum}")
        compCards = [cards[random.choice(cards)], cards[random.choice(cards)]]
        compCardSum = sumOfCards(compCards)
        print(f"Computer's first card is: {compCards[0]}")
        choice2 = (input("Type 'y' to get another card, or type 'n' to pass: ")).lower()
        while choice2!="y" and choice2!="n":
            choice2 = (input("Please type a valid input: ")).lower()
        
        if choice2=="n":
            clear()
            print(art.logo)
            printFinals(userCards, compCards, userCardSum, compCardSum)
            while compCardSum < 17:
                compCards.append(cards[random.choice(cards)])
                compCardSum = sumOfCards(compCards)
                clear()
                print(art.logo)
                print(f"The Computer score is {compCardSum-compCards[-1]}, Computer will draw another card.")
                printFinals(userCards, compCards, userCardSum, compCardSum)
            
            if compCardSum > 21:
                print("Computer's score went over 21. You win.")
            elif userCardSum > compCardSum:
                if compCardSum < 17:
                    print("Your final score is greater than the Computer's. You win.")
            elif compCardSum > userCardSum:
                print("Your final score is less than the Computer's. You lose.")
            elif userCardSum == compCardSum:
                print("Your final score is equal to the Computer's. Draw.")
        
        if choice2=="y":
            clear()
            print(art.logo)
            userCards.append(cards[random.choice(cards)])
            userCardSum = sumOfCards(userCards)
            printFinals(userCards, compCards, userCardSum, compCardSum)
            while compCardSum < 17:
                compCards.append(cards[random.choice(cards)])
                compCardSum = sumOfCards(compCards)
                clear()
                print(art.logo)
                print(f"The Computer score is {compCardSum-compCards[-1]}, Computer will draw another card.")
                printFinals(userCards, compCards, userCardSum, compCardSum)
            
            if compCardSum > 21:
                print("Computer's score went over 21. You win.")
            elif userCardSum > 21:
                if userCards[2]==11:
                    userCards[2] = 1
                if userCardSum > 21:
                    print("Your final score is greater than 21. You lose.")
            elif userCardSum > compCardSum and userCardSum < 22:
                print("Your final score is greater than the Computer's. You win.")
            elif compCardSum > userCardSum:
                print("Your final score is less than the Computer's. You lose.")
            elif userCardSum == compCardSum:
                print("Your final score is equal to the Computer's. Draw.")

        choice3 = (input("Do you want to play another game of Blackjack? type 'y' or 'n': ")).lower()
        while choice3!="y" and choice3!="n":
            choice3 = (input("Please type a valid input: ")).lower()
        if choice3=="y":
            blackjack(cards)
        if choice3=="n":
            print("Thank you for playing.")

choice1 = (input("Do you want to play a game of Blackjack? type 'y' or 'n': ")).lower()
while choice1!="y" and choice1!="n":
    choice1 = (input("Please type a valid input: ")).lower()
if choice1=="n":
    print("Goodbye.")
if choice1=="y":
    blackjack(cards)