from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=650, height=320, bg="white")
        self.question_text = self.canvas.create_text(
            320,
            125,
            width=500,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.button_frame = Frame(self.window, bg=THEME_COLOR)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=20)

        self.button1 = Button(
            self.button_frame, text="Button 1", command=self.one_pressed)
        self.button1.grid(row=0, column=0, padx=10)

        self.button2 = Button(
            self.button_frame, text="Button 2", command=self.two_pressed)
        self.button2.grid(row=0, column=1, padx=10)

        self.button3 = Button(
            self.button_frame, text="Button 3", command=self.three_pressed)
        self.button3.grid(row=1, column=0, padx=10)

        self.button4 = Button(
            self.button_frame, text="Button 4", command=self.four_pressed)
        self.button4.grid(row=1, column=1, padx=10)
        
        self.button5 = Button(
            self.button_frame, text="Dont know", command=self.five_pressed)
        self.button5.grid(row=3, column=0, padx=10)
        
        
        
        self.buttons = [self.button1, self.button2,
                        self.button3, self.button4, self.button5]

        self.get_next_question()
        self.quiz.updateFile()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        for button in self.buttons:
            button.config(bg='white')
            button.config(state="normal")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

            choices = self.quiz.getChoices()

            self.button1.config(text=choices[0])
            self.button2.config(text=choices[1])
            self.button3.config(text=choices[2])
            self.button4.config(text=choices[3])

        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz.")
            for button in self.buttons:
                button.config(state="disabled")

    def one_pressed(self):
        self.give_feedback(self.quiz.check_answer(0))

    def two_pressed(self):
        self.give_feedback(self.quiz.check_answer(1))

    def three_pressed(self):
        self.give_feedback(self.quiz.check_answer(2))

    def four_pressed(self):
        self.give_feedback(self.quiz.check_answer(3))

    def five_pressed(self):
        self.give_feedback(self.quiz.check_answer("Dont Know"))

    # def false_pressed(self):
    #     is_right = self.quiz.check_answer("False")
    #     self.give_feedback(is_right)

    def give_feedback(self, is_right):
        buttonCount = 0
        for button in self.buttons:
            button.config(state="disabled")

        # correct
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1
            self.canvas.itemconfig(self.question_text, fill="white")
            for button in self.buttons:
                if self.quiz.check_answer(buttonCount):
                    button.config(bg='green')
                buttonCount += 1
            self.quiz.removeQuestion_AndUpdateF()
            self.window.after(1000, self.get_next_question)

        # wrong
        else:
            self.canvas.config(bg="red")
            for button in self.buttons:
                if self.quiz.check_answer(buttonCount):
                    button.config(bg='red')
                buttonCount += 1

            self.window.after(2000, self.get_next_question)
