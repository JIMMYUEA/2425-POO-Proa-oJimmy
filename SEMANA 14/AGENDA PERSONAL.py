import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear un Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # Crear un TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Crear un Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        # Botones
        self.boton_agregar = ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(pady=5)

        self.boton_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.boton_salir.pack(pady=5)

    def agregar_evento(self):
        """Agregar un nuevo evento a la lista."""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        """Eliminar el evento seleccionado de la lista."""
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
            if confirmacion:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")

    def limpiar_campos(self):
        """Limpiar los campos de entrada."""
        self.fecha_entry.set_date('')
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()