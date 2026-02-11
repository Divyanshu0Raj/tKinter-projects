from tkinter import *

window=Tk()
def submit():

  food=[]

  for index in listbox.curselection():
    food.insert(index,listbox.get(index))
  print("You have ordered :-")
  for index in food:
    print(index)
  #print(listbox.get(listbox.curselection()))

def add():
  listbox.insert(listbox.size(),entrybox.get())
  listbox.config(height=listbox.size())

def delete():
  #listbox.delete(listbox.curselection())
  for index in reversed(listbox.curselection):
    listbox.delete(index)
  listbox.config(height=listbox.size())

listbox=Listbox(window,
                bg="#c8f309",
                font=("constantia",35),
                width=35,
                selectmode=MULTIPLE
                )
listbox.pack()

listbox.insert(1,"PIZZA")
listbox.insert(2,"PASTA")
listbox.insert(3,"BREAD")
listbox.insert(4,"SOUP")
listbox.insert(5,"SALAD")

listbox.config(height=listbox.size())

entrybox=Entry(window)
entrybox.pack()

submitbutton=Button(window,text='submit',command=submit)
submitbutton.pack()

addbutton=Button(window,text='add',command=add)
addbutton.pack()

deletebutton=Button(window,text='delete',command=delete)
deletebutton.pack()

window.mainloop()