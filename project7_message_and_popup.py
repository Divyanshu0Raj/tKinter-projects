from tkinter import *
from tkinter import messagebox

def click():
 messagebox.showinfo(title='this is an info message box',message='you are a person')  
 while(TRUE):
    messagebox.showwarning(title='warning',message='you have a virus')
    messagebox.showerror(title='ERROR!!!!',message='you have a error')   

    if(messagebox.askokcancel(title='ask ok cancel',message='do you want to do the thing')):
      print("you did a thing")
    else:
      print("you cancel a thing")


    if(messagebox.askyesno(title='ask yes or no',message='do you like cake')):
      print("you like cakes")
    else:
      print("you don't like cake")
  
    answer=messagebox.askquestion(title='answer it',message='do you like pie')
    if answer== 'yes':
     print("good")
    else:
     print("not bad")

    answer=messagebox.askyesnocancel(title='ask yes no cancel',message='do you coding',)
    if(answer==True):
      print("you like oding")
    elif(answer==False):
     print("you dont like it")
    else:
      print("answer it")
window=Tk()

button=Button(window,command=click,text='click me')
button.pack()


window.mainloop()