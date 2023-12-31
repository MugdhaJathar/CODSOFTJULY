import tkinter as tk
from tkinter import messagebox

def add_task(task_list, task_entry):
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task(task_list):
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")
        
def update_task(task_list, task_entry):
    try:
        index = task_list.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_list.delete(index)
            task_list.insert(index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")       

def clear_tasks(task_list):
    task_list.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("600x550")
    root.config(bg="#E3F4F4")
    root.title("To-Do List")
    
    heading = tk.Label(root, text="TO-DO LIST", fg="#0B2447", bg="#E3F4F4" ,font=("Times New Roman", 25, "bold"))
    heading.pack(pady=30)
    
    enter_task = tk.Entry(root, font=("Times New Roman", 18), bg="#3C84AB" ,fg="#ECF9FF", width=40)
    enter_task.pack(pady=20)

    buttons = tk.Frame(root)
    buttons.pack(pady=10)
    add = tk.Button(buttons, text="Add Task",fg="#0B2447", font=("Times New Roman", 15),bg="#E3F4F4",borderwidth=0 , command=lambda: add_task(list_of_tasks, enter_task))
    add.pack(side=tk.LEFT,padx=5)
    
    update = tk.Button(buttons, text="Update Task",fg="#0B2447", font=("Times New Roman", 15),bg="#E3F4F4" , borderwidth=0 ,command=lambda: update_task(list_of_tasks, enter_task))
    update.pack(side=tk.LEFT,padx=5)

    delete = tk.Button(buttons, text="Delete Task", fg="#0B2447",font=("Times New Roman", 15),bg="#E3F4F4" , borderwidth=0 ,command=lambda: delete_task(list_of_tasks))
    delete.pack(side=tk.LEFT,padx=5)

    clear = tk.Button(buttons, text="Clear All",fg="#0B2447", font=("Times New Roman", 15),bg="#E3F4F4" , borderwidth=0 ,command=lambda: clear_tasks(list_of_tasks))
    clear.pack(side=tk.LEFT,padx=5)

    list_of_tasks = tk.Listbox(root, font=("Times New Roman", 18),bg="#3C84AB" ,fg="#ECF9FF", width=100, height=10)
    list_of_tasks.pack(side=tk.LEFT,padx=80,pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()