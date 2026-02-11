from tkinter import *
from tkinter import filedialog
import PyPDF2

def open_pdf():
    filename = filedialog.askopenfilename(title="select a PDF file", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    outputfile_text.delete(1.0,END)
    if not filename:
        return
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current = reader.pages[i].extract_text()
        outputfile_text.insert(END, current)

window=Tk()
window.title("PDF Text Extrator")

filename=Label(window,text="no file selected")
outputfile_text=Text(window)
openfile=Button(window,text="open PDF file",command=open_pdf)


filename.pack()
outputfile_text.pack()
openfile.pack()
window.mainloop()