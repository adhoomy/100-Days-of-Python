import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

options = [letters, numbers, symbols]

print("Welcome to the Password Generator!")
nr_letters = random.randint(8, 10)
nr_numbers = random.randint(2, 4)
nr_symbols = random.randint(2, 4)

total = nr_letters + nr_numbers + nr_symbols

# the code below creates the password foundation
password = []
for n in range(1,total+1):
    password.append('blank')

# the code below adds random letters to random blank parts of the password
l = 1
while l <= nr_letters:
    candidateLetter=random.randint(0,total-1)
    if password[candidateLetter] == 'blank':
        password[candidateLetter] = letters[random.randint(0,51)]
        l += 1

# the code below adds random numbers to random blank parts of the password
n = 1
while n <= nr_numbers:
    candidateNumber=random.randint(0,total-1)
    if password[candidateNumber] == 'blank':
        password[candidateNumber] = numbers[random.randint(0,9)]
        n += 1

# the code below adds random symbols to random blank parts of the password
s = 1
while s <= nr_symbols:
    candidateSymbol=random.randint(0,total-1)
    if password[candidateSymbol] == 'blank':
        password[candidateSymbol] = symbols[random.randint(0,8)]
        s += 1

finalPassword = str()
for slot in range(0,total):
    finalPassword += password[slot]

print(f"Here is your password: {finalPassword}")