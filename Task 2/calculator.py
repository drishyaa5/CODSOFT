from tkinter import *

class Calculator():
    def __init__(self):
        #for the GUI
        self.window = Tk()
        self.window.title("Calculator App")
        self.window.geometry("458x650")
        self.window.resizable(False,False)

        self.window.config(bg="black") #setting the background color of the window to black


        #result panel where the results will be displayed after the calculation
        self.resultpanel = Entry(self.window,borderwidth=5,relief=SUNKEN,width=29)
        self.resultpanel.grid(row=0,column=0,columnspan=6,pady=(50,0),padx=3)
        self.resultpanel.config(font=("Arial",20))

        #rendering buttons and setting up their positions
        self.button1 = Button(self.window, text="1", width=5, command=lambda:self.ins('1'),relief=RAISED,bg='grey')
        self.button1.grid(row=2,column=0, padx=3, pady=10)
        self.button1.config(font=("Arial", 20))

        self.button2 = Button(self.window, text="2", width=5, command=lambda:self.ins('2'),relief=RAISED,bg='grey')
        self.button2.grid(row=2,column=1, padx=3, pady=10)
        self.button2.config(font=("Arial", 20))

        self.button3 = Button(self.window, text="3", width=5, command=lambda:self.ins('3'),relief=RAISED,bg='grey')
        self.button3.grid(row=2,column=2, padx=3, pady=10)
        self.button3.config(font=("Arial", 20))

        self.button4 = Button(self.window, text="4", width=5, command=lambda:self.ins('4'),relief=RAISED,bg='grey')
        self.button4.grid(row=3,column=0, padx=3, pady=10)
        self.button4.config(font=("Arial", 20))

        self.button5 = Button(self.window, text="5", width=5, command=lambda:self.ins('5'),relief=RAISED,bg='grey')
        self.button5.grid(row=3,column=1, padx=3, pady=10)
        self.button5.config(font=("Arial", 20))

        self.button6 = Button(self.window, text="6", width=5, command=lambda:self.ins('6'),relief=RAISED,bg='grey')
        self.button6.grid(row=3,column=2, padx=3, pady=10)
        self.button6.config(font=("Arial", 20))

        self.button7 = Button(self.window, text="7", width=5, command=lambda:self.ins('7'),relief=RAISED,bg='grey')
        self.button7.grid(row=4,column=0, padx=3, pady=10)
        self.button7.config(font=("Arial", 20))

        self.button8 = Button(self.window, text="8", width=5, command=lambda:self.ins('8'),relief=RAISED,bg='grey')
        self.button8.grid(row=4,column=1, padx=3, pady=10)
        self.button8.config(font=("Arial", 20))

        self.button9 = Button(self.window, text="9", width=5, command=lambda:self.ins('9'),relief=RAISED,bg='grey')
        self.button9.grid(row=4,column=2, padx=3, pady=10)
        self.button9.config(font=("Arial", 20))

        self.button0 = Button(self.window, text="0", width=13, command=lambda:self.ins('0'),relief=RAISED,bg='grey')
        self.button0.grid(row=5, column=0, padx=5, pady=3, columnspan=2)
        self.button0.config(font=("Arial", 20))

        #operator buttons
        self.buttondot = Button(self.window, text=".", width=5, command=lambda:self.ins('.'),relief=RAISED,bg='grey')
        self.buttondot.grid(row=5,column=2, padx=3, pady=10)
        self.buttondot.config(font=("Arial", 20))

        self.buttoncancel = Button(self.window, text="C", width=5, command=lambda:self.backspace(),relief=RAISED,bg='orange')
        self.buttoncancel.grid(row=1,column=0, padx=3, pady=(100,10))
        self.buttoncancel.config(font=("Arial", 20))
        
        self.buttondelete = Button(self.window, text="AC", width=5, command=lambda:self.delete(),relief=RAISED,bg='orange')
        self.buttondelete.grid(row=1,column=1, padx=3, pady=(100,10))
        self.buttondelete.config(font=("Arial", 20))

        self.buttonopen = Button(self.window, text="(", width=5, command=lambda:self.ins('('),relief=RAISED,bg='orange')
        self.buttonopen.grid(row=1,column=2, padx=3, pady=(100,10))
        self.buttonopen.config(font=("Arial", 20))

        self.buttonclosed = Button(self.window, text=")", width=5, command=lambda:self.ins(')'),relief=RAISED,bg='orange')
        self.buttonclosed.grid(row=1,column=3, padx=3, pady=(100,10))
        self.buttonclosed.config(font=("Arial", 20))

        self.buttonadd = Button(self.window, text="+", width=5, command=lambda:self.ins('+'),relief=RAISED,bg='orange')
        self.buttonadd.grid(row=2,column=3, padx=3, pady=10)
        self.buttonadd.config(font=("Arial", 20))

        self.buttonsub = Button(self.window, text="-", width=5, command=lambda:self.ins('-'),relief=RAISED,bg='orange')
        self.buttonsub.grid(row=3,column=3, padx=3, pady=10)
        self.buttonsub.config(font=("Arial", 20))

        self.buttondiv = Button(self.window, text="/", width=5, command=lambda:self.ins('/'),relief=RAISED,bg='orange')
        self.buttondiv.grid(row=4,column=3, padx=3, pady=10)
        self.buttondiv.config(font=("Arial", 20))

        self.buttonmul = Button(self.window, text="x", width=5, command=lambda:self.ins('*'),relief=RAISED,bg='orange')
        self.buttonmul.grid(row=5,column=3, padx=3, pady=10)
        self.buttonmul.config(font=("Arial", 20))

        self.buttoncalc = Button(self.window, text="=", width=27, command=lambda:self.execute(),relief=RAISED,bg='orange')
        self.buttoncalc.grid(row=6, column=0, padx=5, pady=3, columnspan=4)
        self.buttoncalc.config(font=("Arial", 20))
        

        #run the gui
        self.window.mainloop()
    
    
    #calculation functions
    def ins(self,val):
            self.resultpanel.insert(END,val)

    def delete(self):
        self.resultpanel.delete(0,'end')

    def backspace(self):
        x = self.resultpanel.get()
        self.resultpanel.delete(0,'end')
        y = x[:-1]
        self.resultpanel.insert(0,y)

    def execute(self):
        x = self.resultpanel.get()
        answer=eval(x)
        self.resultpanel.delete(0,'end')
        self.resultpanel.insert(0,answer)


if __name__=="__main__":
    Calculator()
