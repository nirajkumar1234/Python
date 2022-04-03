from tkinter import *

# import frame1 as frame1

root = Tk()
root.geometry("655x333")


def hello():
    print("Hello tkinter buttons")
    a = 2
    b = 2
    print("sum of ", a, "&", b, "is", a + b)


def name():
    a=input("Enter your name:")
    print(a)


frame1 = Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame1.pack(side=LEFT, anchor="nw")
b1 = Button(frame1, fg="red", border=2, text="Print now", command=hello)
b1.pack(side='left', padx=23)

b2 = Button(frame1, fg="red", text="tell me my name now", command=name)
b2.pack(side='left', padx=23)

b3 = Button(frame1, fg="red", text="Print now")
b3.pack(side='left', padx=23)

b4 = Button(frame1, fg="red", text="Print now")
b4.pack(side='left', padx=23)

root.mainloop()
