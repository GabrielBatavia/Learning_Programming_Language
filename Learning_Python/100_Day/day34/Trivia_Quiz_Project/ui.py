from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=200,text="Some Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        
        self.true_image = PhotoImage(file="./Trivia_Quiz_Project/images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        
        self.false_image = PhotoImage(file="./Trivia_Quiz_Project/images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_pressed(self):
        self.quiz.check_answer("True")
    
    def false_pressed(self):
        self.quiz.check_answer("False")