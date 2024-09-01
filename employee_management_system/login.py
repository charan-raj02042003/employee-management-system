from customtkinter import *
from PIL import Image
from tkinter import messagebox

def loging():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "All fields are required")
        
    elif usernameEntry.get() == "charan" and passwordEntry.get() == "1234":
        messagebox.showinfo("Success", "Login is Successful")
        root.destroy()
        import ems
        
    else:
        messagebox.showerror("Error", "Wrong credentials")

root = CTk()
root.geometry('1000x686+100+100')
root.resizable(0,0)
root.title("Login Page")
image = CTkImage(Image.open('employee_management_system\\images\\background.jpg'), size=(1000,686))
imageLable = CTkLabel(root, image=image) 
imageLable.place(x=0, y=0)

boundaryFrame = CTkFrame(root, width=300, height=350, corner_radius=10, fg_color='#4A4A4A')
boundaryFrame.place(x=50, y=120)

mainFrame = CTkFrame(root, width=280, height= 330, corner_radius=10, fg_color='#F0F0F0')
mainFrame.place(x=60, y=130)  # Slightly offset to create the border effect

headingLable = CTkLabel(root, text="Employee Management System", bg_color='#F0F0F0', font=('Goudy Old Style', 20, 'bold'), text_color='dark blue')
headingLable.place(x=70, y=150)

usernameEntry = CTkEntry(root, placeholder_text="Enter Your Username", width=180)
usernameEntry.place(x=110, y=230)

passwordEntry = CTkEntry(root, placeholder_text="Enter Your Password", width=180, show='*')
passwordEntry.place(x=110, y=280)

loginButton = CTkButton(root, text="Login", cursor='hand2', command=loging)
loginButton.place(x=125, y=350)


root.mainloop() 