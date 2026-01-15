from tkinter import *
from time import strftime

def update():
    time_string = strftime("%H:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()
window.title("Digital Clock")
window.configure(bg="black")

time_label = Label(
    window,
    font=("Arial", 50),
    fg="#00FF00",
    bg="black"
)
time_label.pack(pady=10)

day_label = Label(
    window,
    font=("Ink Free", 30),
    fg="white",
    bg="black"
)
day_label.pack()

date_label = Label(
    window,
    font=("Ink Free", 30),
    fg="white",
    bg="black"
)
date_label.pack()

update()
window.mainloop()
