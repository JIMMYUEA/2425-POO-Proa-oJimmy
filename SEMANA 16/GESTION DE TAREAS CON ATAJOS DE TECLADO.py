import tkinter as tk
from tkinter import messagebox, Listbox, END, SINGLE

class ListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        # Lista de tareas
        self.tareas = []

        # Campo de entrada para nuevas tareas
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.pack(pady=10)

        # Botones
        self.boton_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista para mostrar las tareas
        self.lista_tareas = Listbox(root, selectmode=SINGLE, width=50, height=10)
        self.lista_tareas.pack(pady=10)

        # Vincular atajos de teclado
        self.root.bind("<Return>", self.agregar_tarea_event)
        self.root.bind("<C>", self.marcar_completada_event)
        self.root.bind("<D>", self.eliminar_tarea_event)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(END, tarea)
            self.entry_tarea.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def agregar_tarea_event(self, event):
        self.agregar_tarea()

    def marcar_completada(self, event=None):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(seleccion)
            self.lista_tareas.delete(seleccion)
            self.lista_tareas.insert(seleccion, tarea + " (Completada)")
            self.lista_tareas.itemconfig(seleccion, {'fg': 'gray'})  # Cambiar color a gris
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def marcar_completada_event(self, event):
        self.marcar_completada()

    def eliminar_tarea(self, event=None):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(seleccion)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

    def eliminar_tarea_event(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
