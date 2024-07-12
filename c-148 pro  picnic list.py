# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:29:14 2024

@author: occup
"""

from tkinter import *
import random
root = Tk()
root.title("Picnic List")
root.geometry("550x625")

picnic = [ "items", "are:","blanket,", "food,", "umbrella,", "basket,", "water,"]

label1 = Label(root, text=picnic)
label2 = Label(root,)


def randomlist():
    print()
    picnic = random.sample(range(2,7),1)
    label2["text"] = "get item : number " + str(picnic)
    




btn = Button(root, text = "Pick Item ", command = randomlist)

label1.place(relx= 0.5, rely = 0.4 , anchor=CENTER)
label2.place(relx= 0.5, rely = 0.45,  anchor=CENTER)
btn.place(relx= 0.5, rely = 0.33,  anchor=CENTER)


root.mainloop()