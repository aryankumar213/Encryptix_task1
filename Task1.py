import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    description = entry.get()
    if description:
        task_id = len(tasks) + 1
        task = {'id': task_id, 'description': description, 'status': 'pending'}
        tasks.append(task)
        listbox.insert(tk.END, f"{task['id']}: {task['description']} (Status: {task['status']})")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

def update_task():
    selected = listbox.curselection()
    if selected:
        task_id = int(listbox.get(selected).split(':')[0])
        for task in tasks:
            if task['id'] == task_id:
                description = entry.get()
                if description:
                    task['description'] = description
                listbox.delete(selected)
                listbox.insert(selected, f"{task['id']}: {task['description']} (Status: {task['status']})")
                entry.delete(0, tk.END)
                return
    else:
        messagebox.showwarning("Warning", "Select a task to update.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task_id = int(listbox.get(selected).split(':')[0])
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_task_completed():
    selected = listbox.curselection()
    if selected:
        task_id = int(listbox.get(selected).split(':')[0])
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
                listbox.delete(selected)
                listbox.insert(selected, f"{task['id']}: {task['description']} (Status: {task['status']})")
                return
    else:
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(frame, text="Mark Completed", command=mark_task_completed)
complete_button.pack(side=tk.LEFT, padx=10)

listbox = tk.Listbox(root, width=80)
listbox.pack(pady=20)

root.mainloop()