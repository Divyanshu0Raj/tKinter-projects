from tkinter import *

def button_press(num):
    global equation_text
    equation_text += str(num)  # FIXED: use equation_text, not equation_label
    equation_label.set(equation_text)  # update the label
def equals():
  global equation_text
  try:
    total=str(eval(equation_text))
    equation_label.set(total)
    equation_text=total
  except ZeroDivisionError:
    equation_label.set("arithmetic error")
    equation_text=""
  except SyntaxError:
    equation_label.set("syntax error")
    equation_text=""
def clear():
  global equation_text
  equation_label.set("")
  equation_text=""

window=Tk()

window.title("caluctor")
window.geometry("500x500")

equation_text=""

equation_label=StringVar()

label=Label(window, textvariable=equation_label, font=("consolas",20), bg="white", width=24, height=2)
label.pack()

frame=Frame(window)
frame.pack()

button1=Button(frame,text=1,height=4,width=9,font=35,command=lambda:button_press(1))
button1.grid(row=0,column=0)

button2=Button(frame,text=2,height=4,width=9,font=35,command=lambda:button_press(2))  # FIXED
button2.grid(row=0,column=1)

button3=Button(frame,text=3,height=4,width=9,font=35,command=lambda:button_press(3))  # FIXED
button3.grid(row=0,column=2)

button4=Button(frame,text=4,height=4,width=9,font=35,command=lambda:button_press(4))  # FIXED
button4.grid(row=1,column=0)

button5=Button(frame,text=5,height=4,width=9,font=35,command=lambda:button_press(5))  # FIXED
button5.grid(row=1,column=1)

button6=Button(frame,text=6,height=4,width=9,font=35,command=lambda:button_press(6))  # FIXED
button6.grid(row=1,column=2)

button7=Button(frame,text=7,height=4,width=9,font=35,command=lambda:button_press(7))  # FIXED
button7.grid(row=2,column=0)

button8=Button(frame,text=8,height=4,width=9,font=35,command=lambda:button_press(8))  # FIXED
button8.grid(row=2,column=1)

button9=Button(frame,text=9,height=4,width=9,font=35,command=lambda:button_press(9))  # FIXED
button9.grid(row=2,column=2)

button0=Button(frame,text=0,height=4,width=9,font=35,command=lambda:button_press(0))  # FIXED
button0.grid(row=3,column=0)

buttonplus=Button(frame,text="+",height=4,width=9,font=35,command=lambda:button_press("+"))
buttonplus.grid(row=3,column=1)

buttonequals=Button(frame,text="=",height=4,width=9,font=35,command=equals)
buttonequals.grid(row=3,column=2)

buttonclear=Button(window,text="clear",height=4,width=19,font=35,command=clear)
buttonclear.pack()

buttonminus=Button(frame,text="-",height=4,width=9,font=35,command=lambda:button_press("-"))
buttonminus.grid(row=0,column=3)

buttonmultiply=Button(frame,text="*",height=4,width=9,font=35,command=lambda:button_press("*"))
buttonmultiply.grid(row=1,column=3)

buttondivide=Button(frame,text="/",height=4,width=9,font=35,command=lambda:button_press("/"))
buttondivide.grid(row=2,column=3)

buttondot=Button(frame,text=".",height=4,width=9,font=35,command=lambda:button_press("."))
buttondot.grid(row=3,column=3)

window.mainloop()