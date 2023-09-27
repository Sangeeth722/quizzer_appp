THEME_COLOR = "#375362"
from tkinter import*
from quiz_brain import QuizBrain


class UserInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)


        self.label = Label(text = f"Score ",bg=THEME_COLOR,fg="White",font=("Arial",12,"italic"))
        self.label.grid(column=1,row=0)


        self.canvas = Canvas(bg="White",height=250,width=300)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question_text = self.canvas.create_text(150,125,width=280,text="here is some text",
                                                     font=("Arial",20,"italic"),fill=THEME_COLOR)

        image_true = PhotoImage(file="images/true.png")





        self.button = Button(image = image_true,highlightthickness=0,bd=0,command=self.true_button_clicked)

        self.button.grid(row=2,column=0)

        image_false = PhotoImage(file="images/false.png")
        self.button2 = Button(image=image_false, highlightthickness=0, bd=0,command=self.false_button_pressed)

        self.button2.grid(row=2, column=1)

        total_q = self.quiz.question_list
        length_t_q = len(total_q)
        self.label2 = Label(text=f"Total questions = {length_t_q}",bg=THEME_COLOR,fg="White")
        self.label2.grid(row=0,column=0)


        self.next_question_ui()


        self.window.mainloop()

    def next_question_ui(self):
        self.canvas.config(bg="White")

        if self.quiz.still_has_questions():
            self.button2.config(state="normal")
            self.button.config(state="normal")
            self.label.config(text=f"Score : {self.quiz.score}")

            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text = q_txt)

        else:
            self.canvas.itemconfig(self.question_text,text = "You are reached the end of the quiz")
            self.button.config(state="disabled")
            self.button2.config(state="disabled")


    def true_button_clicked(self):
        #is_right = self.quiz.check_answer("True")
        self.feedback(self.quiz.check_answer("True"))
        #self.feedback(is_right)

    def  false_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def feedback(self,is_right):
        self.button2.config(state="disabled")
        self.button.config(state="disabled")
        if is_right:

            self.canvas.configure(bg="Green")
            self.canvas.update()
        else:

            self.canvas.configure(bg="Red")
            self.canvas.update()
        self.window.after(1000,self.next_question_ui)
















#
#






