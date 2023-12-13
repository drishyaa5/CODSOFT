#import
from tkinter import *
import random

#setup tkinter
window = Tk()
window.title('password generator')
window.geometry('400x350')
window.resizable(False,False)


#password generation
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
symbols="()[],.!@#$%^&*/\<>"



all  = ""


#asking the user to input the length of their password
ask_label=Label(window,text="Set the length of your password",font=("Arial",20))
ask_label.pack()

ask_input=Entry(window,borderwidth=5,relief=SUNKEN)
ask_input.config(font=("Arial",20))
ask_input.pack()


#functions for generating passwords
#only lowercase letters will be shown
def easy_pw():
    global all
    upper, lower, nums, syms = False,True,False,False
    display_pw.delete(0,END)
    if upper:
        all += uppercase_letters

    if lower:
        all += lowercase_letters

    if nums:
        all+=digits

    if syms:
        all+=symbols

    length=int(ask_input.get())
    password = "".join(random.sample(all,length))
    display_pw.insert(END,password)

#only uppercase and lowercase pw will be shown
def medium_pw():
    global all
    upper, lower, nums, syms = True,True,False,False
    display_pw.delete(0,END)
    nums,syms = False, False
    if upper:
        all += uppercase_letters

    if lower:
        all += lowercase_letters

    if nums:
        all+=digits

    if syms:
        all+=symbols

    length=int(ask_input.get())
    password = "".join(random.sample(all,length))
    display_pw.insert(END,password)

#all numbers uppercase lowercase and symbols will be shown
def complex_pw():
    global all
    upper, lower, nums, syms = True,True,True,True
    display_pw.delete(0,END)
    if upper:
        all += uppercase_letters

    if lower:
        all += lowercase_letters

    if nums:
        all+=digits

    if syms:
        all+=symbols

    length=int(ask_input.get())
    password = "".join(random.sample(all,length))
    display_pw.insert(END,password)


#three buttons for the complexity of the password
easybutton = Button(window,text='easy', width=7, relief=RAISED,command=easy_pw,bg='pink',font=("Arial",20))
easybutton.pack(pady=5)

mediumbutton = Button(window,text='medium', width=7, relief=RAISED,command=medium_pw,bg='pink',font=("Arial",20))
mediumbutton.pack(pady=5)

hardbutton = Button(window,text='complex', width=7, relief=RAISED,command=complex_pw,bg='pink',font=("Arial",20))
hardbutton.pack(pady=5)

#display password
display_pw = Entry(window,borderwidth=5,relief=SUNKEN)
display_pw.config(font=("Arial",20))
display_pw.pack(pady=15)




#main gui loop
window.mainloop()