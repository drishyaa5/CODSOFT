from tkinter import *
import random

window = Tk()
window.title("Rock Paper Scissors")
window.resizable(False,False)
window.geometry("500x350")
window.config(bg='black')
user_score = 0
computer_score = 0

label = Label(window,text="Rock Paper Scissors Game!!", font=("consolas",20))
label.grid(row=0,column=0,columnspan=6)

user = Label(window,text="User:{}".format(user_score), font=("consolas",20),bg='green')
user.grid(row=1,column=0,padx=20,pady=(0,100))
computer = Label(window,text="Computer:{}".format(computer_score),font=("consolas",20),bg='red')
computer.grid(row=1,column=1,pady=(0,100),columnspan=4)

computer_options = ['rock','paper','scissors']

def rock():
    evaluation.delete(0,END)
    global computer_options,user_score,computer_score
    
    user_selection = 'rock'
    computer_selection = random.choice(computer_options)
    if user_selection == computer_selection:
        evaluation.insert(0,"Tie")

    if computer_selection == 'paper':
        lose_text = "You Lose! The computer chose " + computer_selection
        evaluation.insert(0,lose_text)
        computer_score += 1
        computer.config(text="Computer:{}".format(computer_score))
    
    if computer_selection == 'scissors':
        win_text = "You Win! The computer chose " +computer_selection
        evaluation.insert(0,win_text)
        user_score += 1
        user.config(text="User:{}".format(user_score))

def paper():
    evaluation.delete(0,END)
    global computer_options,user_score,computer_score
    
    user_selection = 'paper'
    computer_selection = random.choice(computer_options)
    if user_selection == computer_selection:
        evaluation.insert(0,"Tie")

    if computer_selection == 'scissors':
        lose_text = "You Lose! The computer chose " + computer_selection
        evaluation.insert(0,lose_text)
        computer_score += 1
        computer.config(text="Computer:{}".format(computer_score))
    
    if computer_selection == 'rock':
        win_text = "You Win! The computer chose " +computer_selection
        evaluation.insert(0,win_text)
        user_score += 1
        user.config(text="User:{}".format(user_score))\
            
def scissors():
    evaluation.delete(0,END)
    global computer_options,user_score,computer_score
    
    user_selection = 'scissors'
    computer_selection = random.choice(computer_options)
    if user_selection == computer_selection:
        evaluation.insert(0,"Tie")

    if computer_selection == 'rock':
        lose_text = "You Lose! The computer chose " + computer_selection
        evaluation.insert(0,lose_text)
        computer_score += 1
        computer.config(text="Computer:{}".format(computer_score))
    
    if computer_selection == 'paper':
        win_text = "You Win! The computer chose " +computer_selection
        evaluation.insert(0,win_text)
        user_score += 1
        user.config(text="User:{}".format(user_score))

#buttons
rockButton = Button(window,text="rock",bg='red',width=6,relief=RAISED,command=rock)
rockButton.grid(row=2,column=0)
rockButton.config(font=("Arial",20))

paperButton = Button(window,text="paper",bg='white',width=6,relief=RAISED, command=paper)
paperButton.grid(row=2,column=1)
paperButton.config(font=("Arial",20))

scissorsButton = Button(window,text="scissors",bg='blue',width=6,relief=RAISED, command=scissors)
scissorsButton.grid(row=2,column=2)
scissorsButton.config(font=("Arial",20))

evaluation = Entry(window,borderwidth=5,relief=SUNKEN,width=32)
evaluation.grid(row=3,column=0,columnspan=6,pady=(20,0))
evaluation.config(font=("Arial",20))


window.mainloop()