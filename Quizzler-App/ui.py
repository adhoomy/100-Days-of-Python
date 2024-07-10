from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=0, row=0)

        self.q_box = Canvas(width=300, height=250, bg="white")
        self.question_text = self.q_box.create_text(150, 125,
                                                    text="Question Here",
                                                    font=("Arial", 20, "italic"),
                                                    width=280)
        self.q_box.grid(column=0, row=1, columnspan=2, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_box.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.q_box.itemconfig(self.question_text, text=q_text)
        else:
            self.q_box.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.q_box.config(bg="green")
        else:
            self.q_box.config(bg="red")
        self.window.after(1000, self.get_next_question)
