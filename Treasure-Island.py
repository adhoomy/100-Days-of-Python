print("                    ____...------------...____\n")
print("               _.-\"` /o/__ ____ __ __  __ \o\_`\"-._\n")
print("             .'     / /                    \ \     '.\n")
print("             |=====/o/======================\o\=====|\n")
print("             |____/_/________..____..________\_\____|\n")
print("             /   _/ \_     <_o#\__/#o_>     _/ \_   \\\n")
print("             \_________\####/_________/\n")
print("              |===\!/========================\!/===|")
print("              |   |=|          .---.         |=|   |\n")
print("              |===|o|=========/     \========|o|===|\n")
print("              |   | |         \() ()/        | |   |\n")
print("              |===|o|======{'-.) A (.-'}=====|o|===|\n")
print(r"              | __/ \__     '-.\uuu/.-'    __/ \__ |\n") #the r turns the string into a raw string
print("              |==== .'.'^'.'.====|\n")
print("          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|\n")
print("              `------------------------------------`\n\n")

print("Welcome to Treasure Island\nYour mission is to find the treasure.")
choice1=input('You\'re at a cross road, where do you want to go?\ntype "left" or "right"\n').lower()
if choice1=="left":
    choice2=input('You\'ve come to a lake. There is an island in the middle of the lake.\ntype "wait" to wait for a boat or type "swim" to swim across\n').lower()
    if choice2=="wait":
        choice3=input('You arrive at the island unharmed. There is a house with three doors; one red, one yellow, and one blue. Which color do you choose?\ntype "red", "yellow", or "blue"\n').lower()
        if choice3=="red":
            print("You were burned by fire.\nGame Over.")
        elif choice3=="blue":
            print("You were eaten by ravaging beasts.\nGame Over.")
        elif choice3=="yellow":
            print("You found the treasure!\nYou Win!")
        else:
            print("Game Over.")
    else:
        print("You were attacked by a trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")