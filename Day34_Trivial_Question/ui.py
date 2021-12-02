from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FALSE_IMG = "images/false.png"
TRUE_IMG = "images/true.png"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
            width=280,
            text="Kanye Quote Goes HERE",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
           )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_img = PhotoImage(file=TRUE_IMG)
        self.check_button = Button(image=check_img, command=self.press_check_button, highlightthickness=0, borderwidth=0)
        self.check_button.grid(column=0, row=2)
        cross_img = PhotoImage(file=FALSE_IMG)
        self.cross_button = Button(image=cross_img, command=self.press_cross_button, highlightthickness=0, borderwidth=0)
        self.cross_button.grid(column=1, row=2)
        
        self.get_next_question()

        self.window.mainloop()
    def press_check_button(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def press_cross_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()  
            self.canvas.itemconfig(self.question_text, text=q_text)
        else: 
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz.")
            self.cross_button.config(state="disable")
            self.check_button.config(state="disable")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
