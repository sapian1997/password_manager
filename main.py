from tkinter import *
from tkinter import messagebox
import random
import pandas
import pyperclip
import json
# ---------------------------- SEARCH ------------------------------- #
#TODO SEARCH
def search():
   search_website=str(website_entry.get()).lower()
   with open("data.json") as file:
        values=json.load(file)
        try:
            website_founded=values[search_website]
            password_founded = website_founded["password"]
            email_founded = website_founded["email"]
            messagebox.showinfo(title="Result", message=f"email :{email_founded}\n"
                                                        f"password :{password_founded}")
        except:
            messagebox.showinfo(title="Result", message=f"there is no {search_website} account saved so far")
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            pass_entry.delete(0,END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#TODO password genarate
def genarator():
    pass_entry.delete(0,END)
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char= [	"!","#","$","%"	,"&","@"]
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letters=[random.choice(letter)for _ in range(3)]
    char=[random.choice(special_char)for _ in range(3)]
    num=[random.choice(numbers)for _ in range(3)]

    passw=letters+char+num

    random.shuffle(passw)
    password_genarator="".join(passw)
    pyperclip.copy(password_genarator)
    pass_entry.insert(0,f"{password_genarator}")
    messagebox.showinfo(message="Password copied")
# TODO save password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=str(website_entry.get()).lower()
    email=email_entry.get()
    password=pass_entry.get()
    data_dict={website:
                   {"email":email,
                    "password":password}
               }
    if len(website)==0 or len(email)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="check again", message="Please enter credentials properly")
    else:
        try:
          with open("data.json") as file:
              datas=json.load(file)
        except:
             with open("data.json",mode="w") as file:
                 json.dump(data_dict,file,indent=4)
        else:
            with open("data.json",mode="w") as file:
                datas.update(data_dict)
                json.dump(datas,file,indent=4)
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    pass_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20,bg="#B1E693")

#TODO canvas
canvas=Canvas(width=200,height=200,bg="#B1E693",highlightthickness=0)
locker=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=locker)
canvas.grid(column=1,row=0)

#TODO labes
website_label=Label(text="Website         :",bg="#B1E693",font=("Courier",10))
website_label.grid(column=0,row=1)
email_label=Label(text="Email/User name :",bg="#B1E693",font=("Courier",10))
email_label.grid(column=0,row=2)
pass_label=Label(text="Password        :",bg="#B1E693",font=("Courier",10))
pass_label.grid(column=0,row=3)

#TODO entrys
website_entry=Entry(width=36,bg="#FBF4E9")
website_entry.focus()
website_entry.grid(column=1,row=1)

email_entry=Entry(width=55,bg="#FBF4E9")
email_entry.grid(column=1,row=2,columnspan=3)

pass_entry=Entry(width=36,bg="#FBF4E9")
pass_entry.grid(column=1,row=3)

#TODO buttons
gen_pass_butn=Button(text="Genarate Password",command=genarator,bg="#EC9CD3")
gen_pass_butn.grid(column=3,row=3)

add_butn = Button(text="Add",width=47,command=save,bg="#EC9CD3")
add_butn.grid(column=1,row=4,columnspan=3)

search_button=Button(text="Search",width=14,bg="#EC9CD3",command=search)
search_button.grid(column=3,row=1)

window.mainloop()