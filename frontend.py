import tkinter as tk
from tkinter import ttk



root = tk.Tk()

root.title('Bible Tools')
root.geometry('400x300')

sel_ge = tk.BooleanVar()
sel_ex = tk.BooleanVar()
sel_le = tk.BooleanVar()
sel_nu = tk.BooleanVar()
sel_dt = tk.BooleanVar()

book_vars = {"Gen" : sel_ge, "Exo" : sel_ex, "Lev" : sel_le, "Num" : sel_nu, "Deut" : sel_dt}

#Check boxes
for book_var in book_vars:

    ttk.Checkbutton(root,
                    text=f'Process {book_var}?',
                    variable=book_vars[book_var]).pack()


# Process button
proc_btn=tk.Button(root, text="Process Books")
proc_btn.pack()

# Status bar
status_var = tk.StringVar()
status_bar = tk.Label(root, text='Message Area')
status_bar.pack()

def save():
    message=''
    for book_var in book_vars:
        if book_vars[book_var].get():
            message += book_var

    status_bar.configure(text=message)        
    
proc_btn.configure(command = save)

# run
root.mainloop()
