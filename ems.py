from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

#Function part


def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to detele all the records?')
    if result:
        database.deleteall_record()
    else:
        pass

def show_all():
    treeview_data()
    search_entry.delete(0,END)
    search_box.set('Search By')

def search_employee():
    if search_entry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif search_box.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    else:
        selected_data=database.search(search_box.get(),search_entry.get())
        tree.delete(*tree.get_children())
        for employee in selected_data:
            tree.insert('',END,values=employee)

def delete_data():
    selected_item=tree.selection()
    if not selected_item:
         messagebox.showerror('Error','Select data to Delete')
    else:
        database.delete(id_entry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is deleted')


def update_data():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(id_entry.get(),name_entry.get(),phone_entry.get(),role_box.get(),gender_box.get(),salary_entry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is updated")

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        clear()
        row=tree.item(selected_item)['values']
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        phone_entry.insert(0,row[2])
        role_box.set(row[3])
        gender_box.set(row[4])
        salary_entry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    role_box.set('Java Developer')
    gender_box.set('Male')
    salary_entry.delete(0,END)

def treeview_data():
    employees=database.fetch_employee()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)


def add_employee():
    if id_entry.get()=='' or name_entry.get()=='' or phone_entry.get()=='' or salary_entry.get()=='':
        messagebox.showerror("ERROR","All fields are required")
    elif database.id_exists(id_entry.get()):
        messagebox.showerror("ERROR","Id already exists")
    else:
        database.insert(id_entry.get(),name_entry.get(),phone_entry.get(),role_box.get(),gender_box.get(),salary_entry.get())
        clear()
        treeview_data()
        messagebox.showinfo("Success","Data is added")



#GUI part
window=CTk()
window.geometry("930x580+100+100")
window.configure(fg_color="#161C30")
window.resizable(0,0)
window.title("Employee Management System")


logo=CTkImage(Image.open('bg.jpg'),size=(930,158))
logo_label=CTkLabel(window,image=logo,text='')
logo_label.grid(row=0,column=0,columnspan=2)


left_frame= CTkFrame(window,fg_color="#161C30")
left_frame.grid(row=1,column=0)

id_label=CTkLabel(left_frame,text="ID",font=('Arial',18,'bold'),text_color="white")
id_label.grid(row=0,column=0,padx=20,pady=15,sticky='w')
id_entry=CTkEntry(left_frame,font=('Arial',15,'bold'),width=180)
id_entry.grid(row=0,column=1)

name_label=CTkLabel(left_frame,text="Name",font=('Arial',18,'bold'),text_color="white")
name_label.grid(row=1,column=0,padx=20,pady=15,sticky='w')
name_entry=CTkEntry(left_frame,font=('Arial',15,'bold'),width=180)
name_entry.grid(row=1,column=1)

phone_label=CTkLabel(left_frame,text="Phone no",font=('Arial',18,'bold'),text_color="white")
phone_label.grid(row=2,column=0,padx=20,pady=15,sticky='w')
phone_entry=CTkEntry(left_frame,font=('Arial',15,'bold'),width=180)
phone_entry.grid(row=2,column=1)

role_label=CTkLabel(left_frame,text="Role",font=('Arial',18,'bold'),text_color="white")
role_label.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=["Java Developer","Python Developer","Network Engineer","Devops Engineer","Technical support","Frontend Developer","Mern Stack"]
role_box=CTkComboBox(left_frame,values=role_options,width=180,font=('Arial',15,'bold'),state="readonly")
role_box.grid(row=3,column=1)
role_box.set(role_options[0])

gender_label=CTkLabel(left_frame,text="Gender",font=('Arial',18,'bold'),text_color="white")
gender_label.grid(row=4,column=0,padx=20,pady=15,sticky='w')
gender_options=["Male","Female"]
gender_box=CTkComboBox(left_frame,values=gender_options,width=180,font=('Arial',15,'bold'),state="readonly")
gender_box.grid(row=4,column=1)
gender_box.set('Male')

salary_label=CTkLabel(left_frame,text="Salary",font=('Arial',18,'bold'),text_color="white")
salary_label.grid(row=5,column=0,padx=20,pady=15,sticky='w')
salary_entry=CTkEntry(left_frame,font=('Arial',15,'bold'),width=180)
salary_entry.grid(row=5,column=1)

rigth_frame= CTkFrame(window)
rigth_frame.grid(row=1,column=1)

search_options=["ID","Name","Phone no","Role","Gender","Salary"]
search_box=CTkComboBox(rigth_frame,values=search_options,state="readonly")
search_box.grid(row=0,column=0)
search_box.set("Search By")

search_entry=CTkEntry(rigth_frame)
search_entry.grid(row=0,column=1)

search_Button=CTkButton(rigth_frame,text="Search",width=100,command=search_employee)
search_Button.grid(row=0,column=2)

showall_Button=CTkButton(rigth_frame,text="Showall",width=100,command=show_all)
showall_Button.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rigth_frame,height=13)
tree.grid(row=1,column=0,columnspan=4)
tree['column']=('ID','Name','Phone','Role','Gender','Salary')
tree.heading('ID',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('ID',width=80)
tree.column('Name',width=100)
tree.column('Phone',width=120)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=90)

style=ttk.Style()
style.configure('Treeview.Heading',font=('Arial',18,'bold'))
style.configure('Treeview',font=('Arial',14,'bold'),rowheight=30,background='#161C30',foreground='white')

Scrollbar=ttk.Scrollbar(rigth_frame,orient=VERTICAL,command=tree.yview)
Scrollbar.grid(row=1,column=4,sticky='ns')

button_frame=CTkFrame(window,fg_color="#161C30")
button_frame.grid(row=2,column=0,columnspan=2)

new_Button=CTkButton(button_frame,text='New Employee',font=('Arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
new_Button.grid(row=0,column=0,pady=5,padx=5)

add_Button=CTkButton(button_frame,text='Add Employee',font=('Arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
add_Button.grid(row=0,column=1,pady=5,padx=5)

update_Button=CTkButton(button_frame,text='Update Employee',font=('Arial',15,'bold'),width=160,corner_radius=15,command=update_data)
update_Button.grid(row=0,column=2,pady=5,padx=5)

delete_Button=CTkButton(button_frame,text='Delete Employee',font=('Arial',15,'bold'),width=160,corner_radius=15,command=delete_data)
delete_Button.grid(row=0,column=3,pady=5,padx=5)

Delete_All=CTkButton(button_frame,text='Delete All',font=('Arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
Delete_All.grid(row=0,column=4,pady=5,padx=5)

treeview_data()
window.bind('<ButtonRelease>',selection)

window.mainloop()