from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.configure(bg="white")
root.title("TODO")
root.geometry("200x370")
tasks = []


# Create functions

def update_listbox():
    # Clear the current list
    clear_listbox()
    # Populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)


def clear_listbox():
    lb_tasks.delete(0, "end")


def add_task():
    # Get the task to add
    task = txt_input.get()
    # Make sure the task is not empty
    if task != "":
        # Append to the list
        tasks.append(task)
        # Update the listbox
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You need to enter a task.")
    txt_input.delete(0, "end")

def del_one():
    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    # Update the listbox
    update_listbox()

    # Update the listbox
    update_listbox()


lbl_title = Label(root, text="Sammy To-Do-List", bg="white", font=("Agency FB", 12), padx=15, pady=10)
lbl_title.grid(row=0, column=0)

txt_input = Entry(root, width=25, font=("Agency FB", 11))
txt_input.grid(row=1, column=0, padx=15)

btn_add_task = Button(root, text="Add task", fg="green", bg="white", command=add_task, font=("Agency FB", 11))
btn_add_task.grid(row=9, column=0)

btn_del_one = Button(root, text="Delete", fg="green", bg="white", command=del_one, font=("Agency FB", 11))
btn_del_one.grid(row=10, column=0)

btn_exit = Button(root, text="Exit", fg="green", bg="white", command=exit, font=("Agency FB", 11))
btn_exit.grid(row=11, column=0)

lb_tasks = Listbox(root, font=("Agency FB", 11))
lb_tasks.grid(row=2, column=0, rowspan=7)

# Start the main events loop
root.mainloop()
