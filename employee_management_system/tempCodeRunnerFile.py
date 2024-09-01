
        messagebox.showerror('Error', 'Select data to update')
    else:
        database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is successfully updated')

def add_employee():
    if idEntry.get() == "" or phoneEntry.get() == "" or nameEntry.get() == "" or salaryEntry.get() == "":
        messagebox.showerror('Error', 'All fields are required')
    elif database.id_exists(idEntry.get()):