import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()
correct_guesses = []

score = 0
while score < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50", prompt="Guess a state:").title()

    if guess == "Exit":
        missing_states = [state for state in state_names if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if guess in state_names:
        if guess not in correct_guesses:
            score += 1
            correct_guesses.append(guess)
            new_state = turtle.Turtle()
            new_state.hideturtle()
            new_state.penup()
            state_data = data[data.state == guess]
            new_state.goto(int(state_data.x), int(state_data.y))
            new_state.write(guess)
