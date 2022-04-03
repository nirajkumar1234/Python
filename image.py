from tkinter import *
from PIL import Image , ImageTk

abc = Tk()
abc.geometry("855x844")
# For PNG image
# photon = PhotoImage(file="R.jpg")
# niraj_label = Label(image=photon)

# For JPG image
image = Image.open("R.jpg")

photo = ImageTk.PhotoImage(image)
niraj_label = Label(image=photo)

niraj_label.pack()

abc.mainloop()
