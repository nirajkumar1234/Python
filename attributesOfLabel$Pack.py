from tkinter import *

root = Tk()
root.geometry("444x233")
# Code here
root.title("My GUI with Harry")
# Important Label Option
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. comicsansms 19 bold
# padx - x padding
# pady- y padding
# relief - border styling - SUNKEN , RAISED , GROOVE , RIDGE

title_lable = Label(text="Hello world", bg="red", foreground="white", padx=113
                    , pady=94, font="comicsansms 19 bold", borderwidth=3,
                    relief=SUNKEN)
# Important Pack Options
# anchor = nw
# anchor = ne
# anchor = se
# anchor = sw
# side= top , bottom , left , right
# fill X Y
# padx
# pady
title_lable.pack(side=LEFT , fill=Y , padx=34 , pady= 34)

root.mainloop()

