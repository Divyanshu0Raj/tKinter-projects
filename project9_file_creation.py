from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(
        defaultextension='.txt',
          filetypes=[
        ("text file", ".txt"),
        ("html", ".html"),
        ("all files", ".*"),
    ])
    if file is not None:
        filetext = str(text.get(1.0, END))
        file.write(filetext)
        file.close()

window = Tk()

text = Text(window)
text.pack()
button = Button(window, text='save', command=savefile)
button.pack()

window.mainloop()