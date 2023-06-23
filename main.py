import json
from tkinter import *
from tkinter import messagebox
import random

import pyperclip
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def button_generate():
    PASSWORD=[]
    for x in range(4):
        PASSWORD.append(random.choice(LETTERS))
    for x in range(2):
        PASSWORD.append(random.choice(NUMBERS))
        PASSWORD.append(random.choice(SYMBOLS))
    random.shuffle(PASSWORD)
    PASSWORD="".join(PASSWORD)
    password_input.delete(0,END)
    password_input.insert(END,string=f"{PASSWORD}")
    return PASSWORD

def search_funct():
    dat=website_input.get()
    try:
        with open("data.json","r") as data_searched:
            s_data= json.load(data_searched)
    except FileNotFoundError:
        messagebox.showerror(title="File not found",message="No 'data.json' file exists")
    else:
        if dat in s_data:
            messagebox.showinfo(title="Data",message=f"Info\n\nWebsite: {dat}\nEmail: {s_data[dat]['email']}\nPassword:{s_data[dat]['password']}")
        else:
            messagebox.showinfo(title="Data",message="No Data Found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    global data
    web_data=website_input.get()
    email_data=email_input.get()
    pass_data=password_input.get()
    new_dict={
        web_data:{
            "email":email_data,
            "password":pass_data,
    }}
    if web_data=="" or email_data=="" or pass_data=="":
        messagebox.showerror(title="Fields Empty", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json","r") as data:
               new_data= json.load(data)
               
        except:
            with open("data.json","w") as data:
                json.dump(new_dict, data, indent=4)
        else:
            new_data.update(new_dict)

            with open("data.json","w") as data:
                json.dump(new_data, data,indent=4)  #json takes nested dict as input hence new_dict

        finally:
            pyperclip.copy(pass_data)
            website_input.delete(0,END)
            password_input.delete(0,END)        

        messagebox.showinfo(title="Confirm Data",message="Data added to file.")


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Generator")
# window.minsize(width=200,height=200)
window.config(padx=50,pady=50)

#logo
canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#website
website_label=Label(text="Website:",font=("Arial",10,"bold"))
website_label.grid(column=0,row=1)

website_input=Entry(width=32)
website_input.focus()
website_input.grid(column=1,row=1,)

#search button
search_button=Button(text="Search Website",command=search_funct)
search_button.grid(column=2,row=1)
#Email/Username
email_label=Label(text="Email/Username:",font=("Arial",10,"bold"))
email_label.grid(column=0,row=2,pady=10)

email_input=Entry(width=50)
email_input.insert(END,string="wardahk98@gmail.com")
email_input.grid(column=1,row=2,columnspan=2)

#password
password_label=Label(text="Password:",font=("Arial",10,"bold"))
password_label.grid(column=0,row=3)

password_input=Entry(width=32)
password_input.grid(column=1,row=3)

#generate password button
button=Button(text="Generate Password",command=button_generate)
button.grid(column=2,row=3)

#add button
add_button=Button(text="Add",width=43,command=add_data)
add_button.grid(column=1,row=4,columnspan=3)

window.mainloop()