from tkinter import *


def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of username is {passvalue.get()}")


root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
user.grid()
password = Label(root, text="Password")
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar , doubleVar , IntVar , StringVar
uservalue = StringVar()
passvalue = StringVar()
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="Submit", command=getvals).grid()
root.mainloop()
