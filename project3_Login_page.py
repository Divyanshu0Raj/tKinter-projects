from tkinter import *
from tkinter import messagebox



def login():
    username = "divyanshu"
    password = "12345"
    if entry.get() == username and passentry.get() == password:
        messagebox.showinfo(title="login successfullly", message="you successfully logged in")
    else:
        messagebox.showerror(title="login deined", message="wrong password or username")
window=Tk()
window.title("login form")
window.geometry('340x440')
window.config(bg='#333333')

frame=Frame(bg='#333333')

label=Label(frame,text="Login",fg="#FF3399",bg="#333333",font=("Arial",30))
label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)

usernamelabel=Label(frame,text="Username",bg="#333333",fg="white",font=("Arial",15))
usernamelabel.grid(row=1,column=0)

entry=Entry(frame,width=30,font=("Arial",15))
entry.grid(row=1,column=1,pady=10)

passlabel=Label(frame,text="Password",bg="#333333",fg="white",font=("Arial",15))
passlabel.grid(row=2,column=0)

passentry=Entry(frame,width=30,show="*",font=("Arial",15))
passentry.grid(row=2,column=1,pady=10)

loginbutton=Button(frame,text="Login",width=10,bg="#FF3399",fg="white",font=("Arial",10),command=login)
loginbutton.grid(row=3,column=1,columnspan=2,pady=30)



frame.pack()
window.mainloop()