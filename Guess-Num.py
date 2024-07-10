import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = (input("Choose a difficulty. type 'easy' or 'hard': ")).lower()
while difficulty!="easy" and difficulty!="hard":
    difficulty = (input("Choose a difficulty. type 'easy' or 'hard': ")).lower()
if difficulty=="easy":
    chances = 10
else:
    chances = 5

# create a list of already guessed numbers so we can remind the user they already guessed the same number
guesses = []

while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Guess: "))
    # the user will not lose chances for guesses out of range or guessing the same number multiple times
    while guess < 1 or guess > 100:
        guess = int(input("Please make a valid guess: "))
    while guess in guesses:
        guess = int(input("You already guessed this, please try again: "))
    if guess > number:
        print("Too high.")
        chances -= 1
    if guess < number:
        print("Too low.")
        chances -= 1
    if guess == number:
        chances = -1
    
    # after every new guess, at it to the guesses list
    guesses.append(guess)

if chances==0:
    print(f"You ran out of guesses, the number was {number}. You lose.")
if chances==-1:
    print(f"You guessed the correct number. You win.")