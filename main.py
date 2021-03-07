from tkinter import *
from tkinter import messagebox

def save():
    website=website_text.get()
    email=email_text.get()
    password=password_text.get()

    with open('data.txt','a') as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

    messagebox.showinfo(title=website,message="Your info is saved succesfully")

    clear()

def clear():
    website_text.set("")
    email_text.set("")
    password_text.set("")


def center_window(w=300, h=300):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))





#---------- UI BÖLÜMÜ ---------

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg="grey")

canvas=Canvas(width=200, height=200)

logo_img=PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)


#Labels

website_label=Label(text="Website:",bg="grey")
website_label.grid(row=1, column=0,sticky=E)
email_label=Label(text="Email/Username:",bg="grey")
email_label.grid(row=2, column=0,sticky=E)
password_label=Label(text="Password:",bg="grey")
password_label.grid(row=3, column=0,sticky=E)


#Entrys Oluşturalım

website_text=StringVar();
website_entry=Entry(width=52, textvariable=website_text,bd=4)
website_entry.grid(row=1,column=1, columnspan=2,ipadx=0, ipady=0)
website_entry.focus() #cursorun açık olmasını sağlar
email_text=StringVar();
email_entry=Entry(width=52, textvariable=email_text,selectborderwidth=0,bd=4)
email_entry.grid(row=2,column=1,columnspan=2,ipadx=0, ipady=0)
email_text.set("cevikali83@yahoo.com")
password_text=StringVar();
password_entry=Entry(width=38, textvariable=password_text, show='*',selectborderwidth=0,bd=4)
password_entry.grid(row=3,column=1,sticky=E,ipadx=0, ipady=0)


#Buttons

generate_password_button=Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=4, column=1)



center_window(700, 400)
window.mainloop()

