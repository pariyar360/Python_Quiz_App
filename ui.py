from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        # Score Label
        self.score = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Testing",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, sticky="ew", pady=50)

        # Buttons
        right_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=right_image, bd=0, highlightthickness=0, command=self.right_button)
        self.true_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=wrong_image, bd=0, highlightthickness=0, command=self.wrong_button)
        self.false_button.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have completed the Quiz!\n"
                                        f"Final Score: {self.quiz.score}/{self.quiz.question_number}")
            # disabling the buttons after the quiz is finished
            self.disable_buttons()


    def right_button(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def wrong_button(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")

    def give_feedback(self, is_correct: bool):
        self.disable_buttons()
        self.score.config(text=f"Score: {self.quiz.score}")
        # disabling the buttons for 1 sec to avoid rapid presses
        self.window.after(1000, func=self.enable_buttons)
        self.window.after(1000, func=self.next_question)
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
