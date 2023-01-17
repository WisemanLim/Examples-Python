#-*- coding:utf-8 -*-
#!/usr/bin/python
import tkinter as tk

root = tk.Tk()
root.title('Tkinter - Button')
root.geometry('200x200')

def say_hello():
    print('Hello')

helloButton = tk.Button(root, text='HELLO', fg='red', font=('koverwatch', 30), padx=10, pady=30, command=say_hello)
helloButton.pack()

root.mainloop()