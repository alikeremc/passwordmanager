from tkinter import *


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
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200)

logo_img=PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)


#Labels

website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)




center_window(500, 400)
window.mainloop()

