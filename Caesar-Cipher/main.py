import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    textList = []
    if direction=="encode":
        for letter in text:
            if letter in alphabet:
                textList.append(alphabet[(alphabet.index(letter)+shift)%26])
            else:
                textList.append(letter)
    if direction=="decode":
        for letter in text:
            if letter in alphabet:
                textList.append(alphabet[(alphabet.index(letter)-shift)%26])
            else:
                textList.append(letter)
    finalText = str()
    for letter in textList:
        finalText += letter
    print(f"The decoded text is {finalText}")

print(art.logo)
go = True
while go==True:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    if direction=="encode" or direction=="decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
        choice = (input('Would you like to continue encoding or decoding, please type "yes" or "no":\n')).lower()
        if choice=="no":
            go = False
    else:
        direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')