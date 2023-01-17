# Ref : https://github.com/GrgBls/noty, https://www.pysimplegui.org/en/latest/
#-*- coding:utf-8 -*-
#!/usr/bin/python
import tkinter as tk # 1.1
from tkinter import * # 1.2
import PySimpleGUI as sg
from datetime import datetime as dt

def cli():
    import time
    current_time = time.strftime("%H:%M")
    # gets the current time.
    print("Welcome to Noty.You can now create sticky notes, easily.")
    time.sleep(2)
    note_input = input("Type your notes here: ")
    note = ("*%s") % note_input
    time.sleep(1)
    # time.sleep prevents GUI from popping up before it receives input.
    root = tk.Tk() # 1.1 import 사용
    root.title("Noty")
    root.geometry("300x300")
    # changes the width and height of the GUI.
    tk.Label(root, text=current_time).pack()
    # prints the current time.
    tk.Label(root, text=note).pack()
    # prints the input.
    root.mainloop()
    # keeps showing the note, until the user closes it.

def sg_():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])
    window.close()

def what_time(btn = None):
    _now = dt.now()
    btn.config(text=_now)

def simple():
    win = Tk() # 1.2 import 사용
    win.geometry("700x350")
    # win.option_add("*Font", "궁서 20")
    frame = Frame(win)

    # Create two buttons
    save_btn = Button(frame, text="Save", default="active")
    save_btn.pack(side="right")
    cancel_btn = Button(frame, text="Cancel", default="normal")
    cancel_btn.pack(side="left")

    frame.pack(pady=50)

    win.mainloop()

if __name__ == '__main__':
    # cli()
    # sg_()
    simple()