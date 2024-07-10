from replit import clear

def add(n1 ,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    keepGoing = True
    while keepGoing == True:
        for sign in operators:
            print(sign)
        operatorChoice = input("Pick an operation above: ")
        num2 = float(input("What's the next number?: "))
        answer = operators[operatorChoice](num1, num2)
        print(f"{num1} {operatorChoice} {num2} = {answer}")
        num1 = answer
        choice = (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to not: ")).lower()
        while choice!="y" and choice!="n":
            choice = (input("Please enter a valid input: ")).lower()
        if choice=="n":
            clear()
            calculator()

calculator()