import tkinter as tk
from tkinter import ttk

def register():
    print("Registration button clicked")

root = tk.Tk()
root.title("Event Registration Form")

root.geometry("500x500")
root.configure(bg='#5B26CB')

frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.pack(pady=20)

title_label = tk.Label(frame, text="EVENT REGISTRATION FORM", font=('Montserrat', 14, 'bold'), fg='white', bg='black')
title_label.grid(row=0, columnspan=2, pady=10)

first_name_label = tk.Label(frame, text="First Name", bg='white')
first_name_label.grid(row=1, column=0, sticky='w')
first_name_entry = tk.Entry(frame)
first_name_entry.grid(row=1, column=1)

last_name_label = tk.Label(frame, text="Last Name", bg='white')
last_name_label.grid(row=2, column=0, sticky='w')
last_name_entry = tk.Entry(frame)
last_name_entry.grid(row=2, column=1)

company_label = tk.Label(frame, text="Company", bg='white')
company_label.grid(row=3, column=0, sticky='w')
company_entry = tk.Entry(frame)
company_entry.grid(row=3, column=1)

email_label = tk.Label(frame, text="Email", bg='white')
email_label.grid(row=4, column=0, sticky='w')
email_entry = tk.Entry(frame)
email_entry.grid(row=4, column=1)

phone_label = tk.Label(frame, text="Phone", bg='white')
phone_label.grid(row=5, column=0, sticky='w')
area_code_entry = tk.Entry(frame, width=5)
area_code_entry.grid(row=5, column=1, sticky='w')
phone_number_entry = tk.Entry(frame)
phone_number_entry.grid(row=5, column=1, padx=(45, 0))

subject_label = tk.Label(frame, text="Subject", bg='white')
subject_label.grid(row=6, column=0, sticky='w')
subject_combobox = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"])
subject_combobox.grid(row=6, column=1)

existing_customer_label = tk.Label(frame, text="Are you an existing customer?", bg='white')
existing_customer_label.grid(row=7, columnspan=2, pady=10, sticky='w')

customer_var = tk.StringVar(value="Yes")
yes_radiobutton = tk.Radiobutton(frame, text="Yes", variable=customer_var, value="Yes", bg='white')
yes_radiobutton.grid(row=8, column=0, sticky='w')
no_radiobutton = tk.Radiobutton(frame, text="No", variable=customer_var, value="No", bg='white')
no_radiobutton.grid(row=8, column=1, sticky='w')

register_button = tk.Button(frame, text="REGISTER", command=register, bg='red', fg='white', font=('Arial', 12, 'bold'))
register_button.grid(row=9, columnspan=2, pady=20)

root.mainloop()
