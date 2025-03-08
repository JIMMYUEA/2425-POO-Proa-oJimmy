from datetime import datetime


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titulo_autor[0]} - {self.titulo_autor[1]} ({self.categoria}) - {'Disponible' if self.disponible else 'Prestado'}"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"{self.nombre} (ID: {self.usuario_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = set()  # Conjunto para IDs de usuario únicos
        self.historial_prestamos = []

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario.usuario_id)

    def dar_de_baja_usuario(self, usuario_id):
        self.usuarios.discard(usuario_id)

    def prestar_libro(self, usuario, isbn):
        if usuario.usuario_id in self.usuarios and isbn in self.libros and self.libros[isbn].disponible:
            libro = self.libros[isbn]
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            self.historial_prestamos.append({
                'usuario_id': usuario.usuario_id,
                'isbn': isbn,
                'fecha_prestamo': datetime.now()
            })
            return f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}."
        return "Préstamo no disponible."

    def devolver_libro(self, usuario, isbn):
        if isbn in self.libros and not self.libros[isbn].disponible:
            libro = self.libros[isbn]
            libro.disponible = True
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
            return f"Libro '{libro.titulo_autor[0]}' devuelto con éxito."
        return "Libro no encontrado o ya está disponible."

    def buscar_libro(self, criterio, valor):
        return [str(libro) for libro in self.libros.values() if getattr(libro, criterio, None) == valor]

    def listar_libros_prestados(self, usuario):
        return '\n'.join(str(libro) for libro in
                         usuario.libros_prestados) if usuario.libros_prestados else "No tiene libros prestados."

    def historial(self):
        return '\n'.join(f"Usuario ID {h['usuario_id']} prestó {h['isbn']} el {h['fecha_prestamo']}" for h in
                         self.historial_prestamos)


# Menú interactivo
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menú Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Mostrar historial de préstamos")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            usuario_id = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, usuario_id))
        elif opcion == "4":
            usuario_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(usuario_id)
        elif opcion == "5":
            usuario_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            usuario = Usuario("", usuario_id)
            print(biblioteca.prestar_libro(usuario, isbn))
        elif opcion == "6":
            usuario_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            usuario = Usuario("", usuario_id)
            print(biblioteca.devolver_libro(usuario, isbn))
        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input("Valor de búsqueda: ")
            print("\n".join(biblioteca.buscar_libro(criterio, valor)))
        elif opcion == "8":
            usuario_id = input("ID del usuario: ")
            usuario = Usuario("", usuario_id)
            print(biblioteca.listar_libros_prestados(usuario))
        elif opcion == "9":
            print(biblioteca.historial())
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
