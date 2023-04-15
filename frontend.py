import tkinter as tk
from tkinter import ttk

<<<<<<< HEAD


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
=======
# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font='Ubuntu 14 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button()

#run 
window.mainloop()
>>>>>>> 17e2c1cf769ec6583ada6eb63e80f6cb6831ec71
