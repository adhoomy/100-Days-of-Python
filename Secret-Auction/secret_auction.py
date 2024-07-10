from replit import clear
import art

print(art.logo)
auction = {}

def addBid(bidderName, bidderBid):
    auction[bidderName] = bidderBid

keepGoing = True
while keepGoing==True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    decision = (input('Is there another person joining the bid? type "yes" or "no": ')).lower()
    while decision!="yes" and decision!="no":
        decision = (input('Please type only "yes" or "no": ')).lower()
    if decision=="yes":
        clear()
    if decision=="no":
        keepGoing = False
        clear()
    addBid(name, bid)

winner = str()
highest = 0
for name in auction:
    if auction[name] > highest:
        winner = name
        highest = auction[name]

print(f"Congradulations to {winner}, with the highest bid of ${highest}!")