import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Información")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=10)

        # Campo de texto
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botón "Agregar"
        self.add_button = tk.Button(root, text="Agregar", command=self.add_info)
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Botón "Limpiar"
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_info)
        self.clear_button.pack(pady=5)

    def add_info(self):
        info = self.entry.get()
        if info:
            self.listbox.insert(tk.END, info)
            self.entry.delete(0, tk.END)  # Limpiar el campo de texto
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

    def clear_info(self):
        self.entry.delete(0, tk.END)  # Limpiar el campo de texto
        self.listbox.delete(0, tk.END)  # Limpiar la lista

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()