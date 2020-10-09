from tkinter import *
import tkinter


window = Tk()
window.geometry("200x250")
window.configure(background="grey")

#Dictionary to store everything

fields = {}

#Name
name_label = Label(window, text="Name")
name_field = Entry(window,)#Entry level to input your name

name_label.grid(row=0, column=0)
name_field.grid(row=0, column=1)
fields['name'] = name_field

#Surname
surname_label = Label(window, text="Surname")
surname_field = Entry(window)

surname_label.grid(row=1, column=0)
surname_field.grid(row=1, column=1)
fields['surname'] = surname_field

#Email
email_label = Label(window, text="Email")
email_field = Entry(window)

email_label.grid(row=2, column=0)
email_field.grid(row=2, column=1)
fields['email'] = email_field

#Number
contact_label = Label(window, text="Contact Number")
contact_field = Entry(window)

contact_label.grid(row=3, column=0)
contact_field.grid(row=3, column=1)
fields['contact'] = contact_field

#Submit
def submit_command():
    output = "User data:\n"
    for key in fields.keys():
        output += f"{key}: {fields[key].get()}\n"#dictionary to handle information
    print(output)

submit = Button(window, text="Submit", command=submit_command)
submit.grid(row=4, column=0)

window.mainloop()