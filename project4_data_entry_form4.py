from tkinter import *
from tkinter import ttk, messagebox
import os
# import openpyxl

def enter_data():
    if accept_var.get() != "accepted":
        messagebox.showwarning("Error", "Please accept the terms and conditions")
        return

    first_name = firstname_entry.get().strip()
    last_name = lastname_entry.get().strip()

    if not first_name or not last_name:
        messagebox.showerror("Error", "First and Last name are required")
        return

    title = title_combo.get()
    age = age_spinbox.get()
    nationality = nationality_combo.get()
    registered = reg_status_var.get()
    completed_courses = numcourses_spinbox.get()
    completed_semesters = numsemester_spinbox.get()

    filepath = os.path.join(os.getcwd(), "userdata.xlsx")

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append([
            "First Name", "Last Name", "Title", "Age",
            "Nationality", "Registered",
            "Completed Courses", "Completed Semesters"
        ])
        workbook.save(filepath)

    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([
        first_name, last_name, title, age,
        nationality, registered,
        completed_courses, completed_semesters
    ])
    workbook.save(filepath)

    messagebox.showinfo("Success", "Data entered successfully!")

# ---------------- GUI ---------------- #

window = Tk()
window.title("Data Entry Form")
window.geometry("700x500")

frame = Frame(window)
frame.pack(padx=10, pady=10)

# User Info
user_info = LabelFrame(frame, text="User Information", font=("Arial", 14))
user_info.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

Label(user_info, text="First Name").grid(row=0, column=0)
firstname_entry = Entry(user_info)
firstname_entry.grid(row=1, column=0)

Label(user_info, text="Last Name").grid(row=0, column=1)
lastname_entry = Entry(user_info)
lastname_entry.grid(row=1, column=1)

Label(user_info, text="Title").grid(row=0, column=2)
title_combo = ttk.Combobox(user_info, values=["Mr.", "Ms.", "Mrs.", "Dr."])
title_combo.grid(row=1, column=2)

Label(user_info, text="Age").grid(row=2, column=0)
age_spinbox = Spinbox(user_info, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

Label(user_info, text="Nationality").grid(row=2, column=1)
nationality_combo = ttk.Combobox(
    user_info,
    values=["Indian", "American", "Canadian", "Australian"]
)
nationality_combo.grid(row=3, column=1)

for widget in user_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Course Info
courses_frame = LabelFrame(frame, text="Course Information")
courses_frame.grid(row=1, column=0, padx=10, pady=10)

reg_status_var = StringVar(value="not registered")
Checkbutton(
    courses_frame,
    text="Currently Registered",
    variable=reg_status_var,
    onvalue="registered",
    offvalue="not registered"
).grid(row=0, column=0)

Label(courses_frame, text="# Completed Courses").grid(row=0, column=1)
numcourses_spinbox = Spinbox(courses_frame, from_=0, to=100)
numcourses_spinbox.grid(row=1, column=1)

Label(courses_frame, text="# Completed Semesters").grid(row=0, column=2)
numsemester_spinbox = Spinbox(courses_frame, from_=0, to=20)
numsemester_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Terms
terms_frame = LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, padx=10, pady=10)

accept_var = StringVar(value="not accepted")
Checkbutton(
    terms_frame,
    text="I agree to the terms and conditions",
    variable=accept_var,
    onvalue="accepted",
    offvalue="not accepted"
).grid(row=0, column=0)

# Submit
Button(frame, text="Enter Data", command=enter_data).grid(
    row=3, column=0, sticky="news", padx=10, pady=10
)

window.mainloop()
