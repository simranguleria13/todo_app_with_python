import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Initialize an empty list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to update the task list on the UI
def update_tasks():
    listbox_tasks.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        listbox_tasks.insert(tk.END, task)  # Insert tasks into the listbox

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        tasks.pop(selected_task_index)
        update_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create and place the widgets
frame = tk.Frame(root)
frame.pack(pady=10)

# Entry widget to add a task
entry_task = tk.Entry(frame, width=30)
entry_task.pack(side=tk.LEFT, padx=5)

# Button to add a task
button_add_task = tk.Button(frame, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Button to delete a task
button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(pady=5)

# Start the GUI event loop
root.mainloop()
