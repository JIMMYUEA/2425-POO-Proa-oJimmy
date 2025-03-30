import tkinter as tk
from tkinter import messagebox, END

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Botón para marcar tarea como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Vincular la tecla Enter para añadir tareas
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Vincular doble clic para marcar tarea como completada
        self.task_listbox.bind("<Double-Button-1>", lambda event: self.complete_task())

    def add_task(self):
        """Añadir una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        """Marcar la tarea seleccionada como completada."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            # Cambiar el estado visual de la tarea completada
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{task} (Completada)")
            self.task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})  # Cambiar color de texto
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self):
        """Eliminar la tarea seleccionada de la lista."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()