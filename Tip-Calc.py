print("Welcome to the Tip Calculator.")
total=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
ppl=int(input("How many people to split the bill? "))

newTip=1+tip/100
newTotal=total*newTip
split=round(newTotal/ppl, 2)
fixedSplit="{:.2f}".format(split)
#the fixedSplit variable forces 2 decimal places

print(f"Each person should pay: ${fixedSplit}")