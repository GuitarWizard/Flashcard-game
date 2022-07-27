from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Note in the __init__ line, quizbrain: Quizbrain, the : is a marker for what the datatype is
        # this helps the code developer with auto complete, the Quizbrain after the : tells us that the datatype
        # is from Quizbrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(height = 400, width=400)
        self.window.config(background=THEME_COLOR, padx = 20, pady = 20)
        self.score_label = Label(text = "score", bg=THEME_COLOR, fg= "White")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width = 300, height = 250, bg = "white", highlightthickness=0)

        self.question = self.canvas.create_text(150, 125, text="Question here", fill = THEME_COLOR,
                                                font =("Arial", 18, "italic"), width = 290)

        self.canvas.grid(columnspan = 2, row =1, column =0, pady = 20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column = 0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column = 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text= q_text)
