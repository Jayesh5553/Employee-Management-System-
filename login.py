from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if username_Entry.get()=='' or password_Entry.get()=='':
        messagebox.showerror("Error","Please entry all the fields")
    elif username_Entry.get()=="jayesh" and password_Entry.get()=="12345":
        messagebox.showinfo("Success","Login is sucessful") 
        root.destroy()
        import ems
    else:
        messagebox.showerror("Error","Wrong Credentials")


root=CTk()
root.geometry("930x478")
root.resizable(0,0)
root.title("Login page")
image=CTkImage(Image.open('cover.jpg'),size=(930,478))
image_label=CTkLabel(root,image=image,text='')
image_label.place(x=0,y=0)

heading_label=CTkLabel(root,text="Employee Management System",bg_color="#FAFAFA",font=("Arial",20,"bold"),text_color="dark blue")
heading_label.place(x=20,y=100)

username_Entry=CTkEntry(root,placeholder_text="Enter your Username",width=180)
username_Entry.place(x=50,y=150)

password_Entry=CTkEntry(root,placeholder_text="Enter your Password",width=180,show="*")
password_Entry.place(x=50,y=200)

login_button=CTkButton(root,text="Login",cursor="hand2",command=login)
login_button.place(x=70,y=250)

root.mainloop()