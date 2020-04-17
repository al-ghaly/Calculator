import tkinter as tk
from tkinter import ttk, messagebox
calculator = tk.Tk()  # the application
calculator.title(' ' * 40 + 'Calculator')  # make the title at the center
frame = tk.Frame(calculator, bd=4, highlightthickness=10, highlightbackground='dark slate gray')  # the calculatoe frame
frame.pack()
input_text = tk.StringVar()  # the user input value
entry = tk.Entry(frame, font=('Arial', 20, 'bold'), textvariable=input_text,  # the user input widget
                 bg='powder blue', justify='right', bd=30, insertwidth=4)
entry.grid(columnspan=4, ipady=15)
entry.focus_set()  # set the focus to the entry widget
# the calculator buttons 
tk.Button(frame, text='1', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black' 
          , command=lambda: input_text.set(input_text.get()+'1')).grid(row=1, column=0)
tk.Button(frame, text='2', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'2')).grid(row=1, column=1)
tk.Button(frame, text='3', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'3')).grid(row=1, column=2)
tk.Button(frame, text='4', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'4')).grid(row=2, column=0)
tk.Button(frame, text='5', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'5')).grid(row=2, column=1)
tk.Button(frame, text='6', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'6')).grid(row=2, column=2)
tk.Button(frame, text='7', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'7')).grid(row=3, column=0)
tk.Button(frame, text='8', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'8')).grid(row=3, column=1)
tk.Button(frame, text='9', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'9')).grid(row=3, column=2)
tk.Button(frame, text='0', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'0')).grid(row=4, column=0)
tk.Button(frame, text='.', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'.')).grid(row=4, column=1)
tk.Button(frame, text='+', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'+')).grid(row=1, column=3)
tk.Button(frame, text='-', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'-')).grid(row=2, column=3)
tk.Button(frame, text='*', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'*')).grid(row=3, column=3)
tk.Button(frame, text='/', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set(input_text.get()+'/')).grid(row=4, column=3)

# the actual calculating
def evaluate(event=None):
    try:
        input_text.set(str(eval(input_text.get())))
    except:
        messagebox.showerror('Error', 'Invalid Input')


equal = tk.Button(frame, text='=', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
                  , command=evaluate)
equal.grid(row=4, column=2)
entry.bind('<Return>', evaluate)
tk.Button(frame, text='clear', font=('Arial', 20, 'bold'), bg='powder blue', bd=8, padx=16, pady=16, fg='black'
          , command=lambda: input_text.set('')).grid(row=5, columnspan=4, sticky=tk.E+tk.W)
calculator.resizable(False, False)
calculator.mainloop()
