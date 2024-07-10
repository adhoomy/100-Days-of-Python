import random
import words
import art

print("Lets play Hangman!")
stage = -1
print(art.stages[stage])

chosenWord = words.wordList[random.randint(0,len(words.wordList))]

display = []
for x in range(len(chosenWord)):
    display.append("_")
print(f"{display}\n")

lives = 6

while lives > 0:
    guess = (input("Guess a letter: ")).lower()
    if guess in display:
        guess = input(f"You already guessed {guess}, guess again: ").lower()
    
    # if the letter guessed is in the chosen word, then its placed in the same position in the display
    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if guess==letter:
            display[position] = letter
    if guess in chosenWord:
        print(f"The letter {guess}, is in the word!")

    # if the letter guessed is not in the chosen word, then you lose a life
    if chosenWord.count(guess)==0:
        print(f"The letter {guess}, is not in the word.")
        lives -= 1
        stage -= 1

    # prints the diplay of correct letters guessed and the stage
    print(f"{art.stages[stage]}")
    print(f"{display}\n")

    # after checking a letter, if there are no '_' in the display, then the display is completed and you win
    if '_' not in display:
        print("You Win!")
        print(f"The word was {chosenWord}.")
        lives = -1

# if lives reaches 0, then you lose
if lives==0:
    print("You Lose!")
    print(f"The word was {chosenWord}.")