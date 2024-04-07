# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#copy password to clipboard
def copyy():
    text = pass_entry.get()
    window.clipboard_clear()
    window.clipboard_append(text)

#generate random 8 character password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#disaply the genearted password in the password input field
def display_password():
    random_password = generate_password()
    pass_entry.delete(0, END)
    pass_entry.insert(0, random_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

#On click Add button add data into data.txt file
def adddata():
    submit = messagebox.askokcancel(message="Are you sure")
    if submit:
        web = web_entry.get()
        email = email_entry.get()
        pas = pass_entry.get()


        f = open("data.txt","a")
        f.write("\nWebsite: "+web+"\n")
        f.write("Email: "+email+"\n")
        f.write("Password "+pas+"\n")
        f.close()

        dis.config(text="✅added")


        encrypt()
        dis.after(2000,lambda:dis.config(text=""))

        web_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)


#delete the recently added data
def dell():
    dele = messagebox.askokcancel(message="Are you sure")
    if dele:
        filename = "data.txt"
        n=4
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Delete last n lines
        new_lines = lines[:-n]

        # Write new lines back to the file
        with open(filename, 'w') as file:
            file.writelines(new_lines)

        file.close()

        filename = "encrypted.txt"
        n=5

        with open(filename, 'r') as file:
            lines = file.readlines()

        # Delete last n lines
        new_lines = lines[:-n]

        # Write new lines back to the file
        with open(filename, 'w') as file:
            file.writelines(new_lines)

        file.close()

        dis.config(text="✅deleted")

        dis.after(2000, lambda: dis.config(text=""))

        web_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)

def encrypt():
    key = Fernet.generate_key()

    cipher_suite = Fernet(key)

    web = web_entry.get()
    email = email_entry.get()
    pas = pass_entry.get()

    web = cipher_suite.encrypt(web.encode())
    email = cipher_suite.encrypt(email.encode())
    pas = cipher_suite.encrypt(pas.encode())


    f = open("encrypted.txt", "a")
    f.write("\nEncryption key : "+str(key))
    f.write("Website: " + str(web) + "\n")
    f.write("Email: " + str(email) + "\n")
    f.write("Password " + str(pas) + "\n")
    f.close()







# ---------------------------- UI SETUP ------------------------------- #

#dependencies
from cryptography.fernet import Fernet
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import string



#window
window = Tk()
window.title("password manager")
window.size()
window.config(padx=30,pady=30)

#canva for logo
canva =  Canvas(height=250,width=250)
canva.grid(row=0 , column=3)


original_image = Image.open("logo1.png")
resized_image = original_image.resize((200, 200), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resized_image)
canva.create_image(100,100,image = logo)




#Labels
web = Label(text="Website")
web.grid(row=1,column=0)


email = Label(text="Email")
email.grid(row=2,column=0)

password = Label(text="password")
password.grid(row=3,column=0)

status = Label(text="Status",width=30)
status.grid(row=1,column=30)


#Entry

web_entry = Entry(width=36)
web_entry.grid(row=1,column=1,columnspan=2)

#focus your cursor
web_entry.focus()

email_entry = Entry(width=36)
email_entry.insert(0,"john@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

pass_entry = Entry(width=36)
pass_entry.grid(row=3,column=1,columnspan=2)



#buttons

gen_button = Button(text="Generate Pass",width=20,command=display_password)
gen_button.grid(row=2,column=3)

copy = Button(text="Copy",width=20,command=copyy)
copy.grid(row=3,column=3)

add = Button(text="Add",width=30,command=adddata)
add.grid(row=4,column=2)

delete = Button(text="del recent",width=20,command=dell)
delete.grid(row=3,column=30)


#display

dis = Label(text='Click on "add" to save',width=30)
dis.grid(row=2,column=30)



window.mainloop()






