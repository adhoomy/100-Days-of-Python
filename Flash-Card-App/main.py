from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/arabic_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flip_card():
    card.itemconfig(language, text="English", fill="white")
    card.itemconfig(word, text=current_card["English"], fill="white")
    card.itemconfig(background, image=back_card)


def learned():
    to_learn.remove(current_card)
    left_to_learn = pandas.DataFrame(to_learn)
    left_to_learn.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(language, text="Arabic", fill="black")
    card.itemconfig(word, text=current_card["Arabic"], fill="black")
    card.itemconfig(background, image=front_card)

    flip_timer = window.after(3000, flip_card)


window = Tk()
window.title("Arabic Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
background = card.create_image(400, 263, image=front_card)
language = card.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

x_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=learned)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()
