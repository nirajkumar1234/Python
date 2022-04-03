from tkinter import *

root = Tk()
canvas_width = 800
canvs_height = 400

root.geometry(f"{canvas_width}x{canvas_width}")
can_widget = Canvas(root, width=canvas_width, height=canvs_height)
can_widget.pack()
root.title("Canvas")

# The line goes from the point X1 , Y1 to X2, Y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="red")
'''Rectangle : specifying parameters in this order - coors of top left and
coors of bottom left'''
can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

can_widget.create_text(200, 200, text="python")

can_widget.create_oval(344, 233, 244, 355)

root.mainloop()
