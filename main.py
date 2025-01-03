from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    entry_password.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email= entry_username.get()
    password = entry_password.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(tile="oops",messagebox="fill the empty field")
    else:
        is_ok=messagebox.askokcancel(title="title",message=f"Email:{email}\nPassword:{password}\n is it ok to save")
        if is_ok:
            with open("data.txt","a") as data_file:
               data_file.write(f"{website}|{email}|{password}\n")
               entry_website.delete(0,END)
               entry_password.delete(0,END)



#  --------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
image=canvas.create_image(100,100,image=logo_img)
canvas.pack()
canvas.grid(column=1,row=0)
website_label = Label(text="Website")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)
password_label = Label(text="Password")
password_label.grid(column=0,row=3)
password_button=Button(text="Generate password",width=15,command=generate_password)
password_button.grid(column=2,row=3,columnspan=2)
entry_website=Entry(width=35)
entry_website.grid(row=1,column=1,columnspan=2)
entry_username=Entry(width=35)
entry_username.grid(row=2,column=1,columnspan=2)
entry_username.insert(0,"anuragoa2005@gmail.com")
entry_password=Entry(width=30)
entry_password.grid(row=3,column=1)
add_button=Button(text="add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
