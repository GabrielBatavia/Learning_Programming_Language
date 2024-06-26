from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    
    password_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = webiste_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    
    if len(website) > 0 and len(email) > 0 and len(password) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email : {email} \n Password: {password} \n Are you sure to save?")
        
        if is_ok:
            try:
                with open("./Password_Manager_Project/data.json", mode="r") as saved_password:
                    # Reading old data
                    data = json.load(saved_password)
                    
            except FileNotFoundError:
                with open("./Password_Manager_Project/data.json", mode="w") as saved_password:
                    json.dump(new_data, saved_password, indent=4)
                    
            else:
                
                # Update data
                data.update(new_data)
                    
                with open("./Password_Manager_Project/data.json", mode="w") as saved_password:    
                    #Saving updated data
                    json.dump(data, saved_password, indent=4)
            
            finally:
                webiste_entry.delete(0, END)
                password_entry.delete(0, END)
                
    else:
        messagebox.showwarning(title="WARNING", message="Please fill all of the fields")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = webiste_entry.get()
    
    try:
        with open("./Password_Manager_Project/data.json", mode="r") as web:
            # Reading old data
            data = json.load(web)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"You dont have email or password saved for {website} website")  
            
             
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='./Password_Manager_Project/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=0)


# labels
webiste_label = Label(text="Website:")
webiste_label.grid(row=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2)

password_label = Label(text="Password:")
password_label.grid(row=3)


# Entries
webiste_entry = Entry(width=35)
webiste_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "gabrielbatavia7@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)


# button
generate_password_button = Button(text="Generate Password", command=generate_password, width=15)
generate_password_button.grid(row=3, column=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()