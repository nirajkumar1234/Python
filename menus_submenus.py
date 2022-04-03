from tkinter import *

root = Tk()
root.geometry("733x566")
root.title("Pycharm")


def myFunc():
    print("Hello world")


# my_menu = Menu(root)
# my_menu.add_command(label="file", command=myFunc)
# my_menu.add_command(label="Exit", command=quit)
#
# root.config(menu=my_menu)

your_menu_bar = Menu(root)

m1 = Menu(your_menu_bar, tearoff=0 )
m1.add_command(label="Project 1", command=myFunc)
m1.add_command(label="Save", command=myFunc)
m1.add_command(label="Save as", command=myFunc)
m1.add_separator()
m1.add_command(label="Print", command=myFunc)
root.config(menu=your_menu_bar)
your_menu_bar.add_cascade(label="file", menu=m1)

m2 = Menu(your_menu_bar, tearoff=0 )
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Copy", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
m2.add_separator()
m2.add_command(label="find", command=myFunc)
root.config(menu=your_menu_bar)
your_menu_bar.add_cascade(label="Edit", menu=m2)


root.mainloop()