import art, game_data, random
from replit import clear

score = 0
# compareA is outside of the loop so we can assign it to the account number from the list with more followers for the next round
compareA = random.randint(0, len(game_data.data)-1)

streak = True
while streak == True:
    print(f"{art.logo}\n")
    
    # makes accountA the dictionary in the list
    accountA = game_data.data[compareA]
    print(f"Compare A: {accountA['name']}, a {accountA['description']}, from {accountA['country']}.")
    followersA = accountA['follower_count']
    print(f"{art.vs}\n")
    
    # makes accountB another account to compare accountA to
    compareB = random.randint(0, len(game_data.data)-1)
    while compareB == compareA:
        compareB = random.randint(0, len(game_data.data)-1)
    accountB = game_data.data[compareB]
    print(f"Compare B: {accountB['name']}, a {accountB['description']}, from {accountB['country']}.\n")
    followersB = accountB['follower_count']

    # sets the answers to the account with more followers
    if followersA > followersB:
        answer = 'a'
    if followersB > followersA:
        answer = 'b'

    # checks if the guess is valid
    # compares the guess to the answer and if the streak continues
    guess = input("Who has more followers? type 'A' or 'B': ").lower()
    while guess != 'a' and guess != 'b':
        guess = input("Please enter a valid input: ").lower()
    if guess != answer:
        clear()
        print(art.logo)
        print(f"Wrong, your final score is: {score}.")
        streak = False
    if guess == answer:
        score += 1
        compareA = compareB
        clear()
