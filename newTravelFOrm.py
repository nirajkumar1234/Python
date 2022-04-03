from tkinter import *


def getvals():
    print(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), payments_Method_value.get(), food_service_value.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), payments_Method_value.get(), food_service_value.get()}\n")


root = Tk()
root.geometry("644x344")
# Heading
Label(root, bg="red", text="Welcome to Nira's Travel", pady=15, font="comicsansms 14 bold").grid()
# Text for form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency contact")
paymentsMethod = Label(root, text="Payment mode")
# Pack with grid
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentsMethod.grid(row=5, column=2)
# Tkinter variable for storing
name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payments_Method_value = StringVar()
food_service_value = IntVar()
# Entries for our form
name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
emergency_entry = Entry(root, textvariable=emergency_value)
payments_Method_entry = Entry(root, textvariable=payments_Method_value)

# Packing the entries
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payments_Method_entry.grid(row=5, column=3)
# Checkbox
food_service = Checkbutton(text="Want to prebook your meals?", variable=food_service_value)
food_service.grid(row=6, column=3)
Button(text="Submit to Nira's Travels", command=getvals).grid(row=7, column=3)
root.mainloop()
