#! /usr/bin/python3

import tkinter as tk

def cute():
    name = box.get()
    if name == "Regan":
        resp = tk.Label(master = window, bg = "red", fg = "white", text = "I LOVE YOU " + name)
        resp.grid(row = 2)
    return


#main
window = tk.Tk()

prompt = tk.Label(master = window, text = "Name: ")
prompt.grid(row = 1, column = 1)

box = tk.Entry(master = window, bg = "yellow")
box.grid(row = 1, column = 2)

butt = tk.Button(master = window, bg = "green", text = "Enter", command = cute)
butt.grid(row = 1, column = 3)

window.mainloop()
