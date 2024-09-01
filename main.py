from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if (len(website) or len(email) or len(password)) == 0:
        messagebox.showwarning(title="oops", message="dont leave any field empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading the json file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data i.e now data contain old+new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # writing/dumping new data in json file i,e updated data is gonna be written
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pass_entry.delete(0, END)


def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="file not found")
    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"email : {data[website]['email']}\n password : {data[website]['password']}")
        else:
            messagebox.showinfo(message="no details for entered website exist")


# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

website_text_label = Label(text="Website:")
website_text_label.grid(row=1, column=0, )
email_label = Label(text="Email/Username:", )
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", )
password_label.grid(row=3, column=0)

website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "adarsha@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="ADD", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="search", command=find_password)
search_button.grid(row=1, column=2)

my_window.mainloop()
