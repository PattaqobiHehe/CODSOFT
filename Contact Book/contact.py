from future.moves import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

master=tk.Tk()
master.geometry("800x680")
master.title("Contacts")
master.config(bg="#101010")




contacts=[]



#Functions to Add contact
def add_contact():
    name=name_entry.get().strip()
    phone=phone_entry.get()
    email=email_entry.get()
    address=address_entry.get()
    if name!="":
        contacts.append((name,phone,email,address))   
        messagebox.showinfo("Save!","You have Saved the Contact Successfully✅")

    else:
        messagebox.showwarning("Warning", "Name cannot be empty")
    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    update_contacts() 

def delete_contact():
    selected=contacts_listbox.curselection()
    if selected:
        index=selected[0]
        del contacts[index]
        update_contacts()
        messagebox.showinfo("Deleted", "You have Deleted the Contact Successfully")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete")

def view_contacts():
    selected = contacts_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]        
        messagebox.showinfo("Details", " Name : " +contact[0]+
                            '\n'+"Phone : " +contact[1]+
                            '\n'+"Email : " +contact[2]+
                            '\n'+"Address : " +contact[3])
    else:
        messagebox.showwarning("Warning", "Please select a contact to view")
   
def update_contacts(filtered_contacts=None):
    contacts_listbox.delete(0,tk.END)
    display_contacts = filtered_contacts if filtered_contacts else contacts
    for contact in display_contacts:
        contacts_listbox.insert(tk.END,contact[0])


def search_contacts():
    query = search_entry.get().strip().lower()
    filtered_contacts = [contact for contact in contacts if query in contact[0].lower() or query in contact[1].lower()]
    update_contacts(filtered_contacts)

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    add_button.config(text="Add Contact", command=add_contact)

def edit_contact():
    selected = contacts_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        
        # Pre-fill entries with current contact details
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact[0])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact[1])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact[2])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact[3])
        
        # Update button to save changes
        add_button.config(text="Update Contact", command=lambda: save_edit(index))
    else:
        messagebox.showwarning("Warning", "Please select a contact to edit")

def save_edit(index):
    name = name_entry.get().strip()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name != "":
        contacts[index] = (name, phone, email, address)
        messagebox.showinfo("Update", "Contact updated successfully✅")
        clear_entries()
        update_contacts()
    else:
        messagebox.showwarning("Warning", "Name cannot be empty")

font_title = ("Garamond", 50, "bold")
font_label = ("Century Gothic", 18, "bold")
font_entry = ("Trebuchet MS", 18)
font_button = ("Bookman Old Style", 14, "bold")
font_listbox = ("Helvetica", 14)


#Heading 'Contact book'
heading_label=tk.Label(master,
                       text="Contact Book",
                       font=font_title,
                       foreground="white" ,
                       bg="#101010")
heading_label.place(x=150,y=3)

#Name label and entry
name_label=tk.Label(master,
                    text="Name:",
                    font=font_label,
                    foreground="white" ,
                    bg="#101010")
name_label.place(x=50, y=100)

name_entry=tk.Entry(master,
                font=font_entry,
                bg="#404040",
                fg="white",
                insertbackground="white",
                width=40)

name_entry.place(x=165, y=100)

#Phone label and entry

phone_label=tk.Label(master,
                    text="Phone:",
                    font=font_label,
                    foreground="white" ,
                    bg="#101010")
phone_label.place(x=50, y=150)

phone_entry=tk.Entry(master,
                font=font_entry,
                bg="#404040",
                fg="white",
                insertbackground="white",
                width=40)
phone_entry.place(x=165, y=150)

#Email label and entry
email_label=tk.Label(master,
                    text="Email:",
                    font=font_label,
                    foreground="white" ,
                    bg="#101010")
email_label.place(x=50, y=200)

email_entry=tk.Entry(master,
                font=font_entry,
                bg="#404040",
                fg="white",
                insertbackground="white",
                width=40)
email_entry.place(x=165, y=200)


#Address label and entry
address_label=tk.Label(master,
                    text="Address:",
                    font=font_label,
                    foreground="white" ,
                    bg="#101010")
address_label.place(x=50, y=250)

address_entry=tk.Entry(master,
                font=font_entry,
                bg="#404040",
                fg="white",
                insertbackground="white",
                width=40)
address_entry.place(x=165, y=250)


#Search Bar
search_label = tk.Label(master, text="Search:", font=font_label, foreground="white", bg="#101010")
search_label.place(x=50, y=320)
search_entry = tk.Entry(master, font=font_entry, width=30, bg="#404040", fg="white", insertbackground="white")
search_entry.place(x=165, y=320)

search_button = tk.Button(master, text="Search", font=font_button, relief="raised", borderwidth=4, width=14, bg="#505050", fg="white", activebackground="#104E8B", command=search_contacts)
search_button.place(x=600, y=315)


#Buttons for adding contacts,removing and details of them

add_button=tk.Button(master,
                     text="Add Contact",
                     command=add_contact,
                     font=font_button,
                     relief="raised",
                     borderwidth=4,
                     width=14,
                     bg="#228B22",
                     fg="white",
                     activebackground="#006400")

add_button.place(x=50, y=370)

#delete button
delete_button=tk.Button(master,
                     text="Delete",
                     command=delete_contact,
                     font=font_button,
                     relief="raised",
                     borderwidth=4,
                     width=8,
                     bg="#B22222",
                     fg="white",
                     activebackground="#8B0000")

delete_button.place(x=250, y=370)

view_button=tk.Button(master,
                     text="View Details",
                     command=view_contacts,
                     font=font_button,
                     relief="raised",
                     borderwidth=4,
                     width=14,
                     bg="#1E90FF",
                     fg="white",
                     activebackground="#104E8B")
view_button.place(x=400, y=370)

edit_button = tk.Button(master,
                        text="Edit Contact",
                        command=edit_contact,
                        font=font_button,
                        relief="raised",
                        borderwidth=4,
                        width=14,
                        bg="#FFA500",
                        fg="white",
                        activebackground="#FF8C00")
edit_button.place(x=600, y=370)

contacts_listbox=tk.Listbox(master,
                            font=font_listbox,
                            width=50, 
                            height=10, 
                            bg="#303030", 
                            fg="white", 
                            selectbackground="#505050", 
                            selectforeground="white")
contacts_listbox.place(x=50,y=430)



master.mainloop()
