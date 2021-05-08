from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    input3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = input1.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")

    else:
        try:
            with open("data.json") as data_file:
                dat = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found!")
        else:
            if website in dat:
                email = dat[website]["email"]
                password = dat[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"{website} is not saved!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = input1.get()
    email = input2.get()
    password = input3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old dat
                dat = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Create new json file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the dat
            dat.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(dat, data_file, indent=4)
                # print(dat)

        finally:
            input1.delete(0, END)
            input3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
key_imag = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_imag)
canvas.grid(column=1, row=0)

# Label
my_label1 = Label(text="Website:")
my_label1.grid(row=1, column=0)
my_label2 = Label(text="Email/Username:")
my_label2.grid(row=2, column=0)
my_label3 = Label(text="Password:")
my_label3.grid(row=3, column=0)


# # Input
input1 = Entry(width=35)
input1.grid(row=1, column=1, columnspan=2, sticky="EW")
input1.focus()
input2 = Entry(width=35)
input2.grid(row=2,column=1,  columnspan=2, sticky="EW")
input2.insert(0, "ayubamonnietahiru@gmail.com")
input3 = Entry(width=21)

input3.grid(row=3, column=1, sticky="EW")

# # Button
generate_password = Button(width=21, text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
search_password = Button(width=21, text="Search", command=search_password)
search_password.grid(row=1, column=2)
Add_password = Button(width=36, text="Add", command=add_data)
Add_password.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()