import json

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn  # ISBN como un atributo inmutable
        self.titulo = titulo  # Título como atributo inmutable
        self.autor = autor  # Autor como atributo inmutable
        self.categoria = categoria  # Categoría como atributo inmutable
        self.prestado = prestado  # Estado de préstamo

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Usuario:
    def __init__(self, id, nombre):
        self.id = id  # El ID del usuario, asegurado único por conjunto
        self.nombre = nombre  # Nombre del usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def agregar_libro_prestado(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def devolver_todos_libros(self):
        """Devuelve todos los libros prestados al usuario"""
        for libro in self.libros_prestados:
            libro.prestado = False
        self.libros_prestados.clear()

class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json', archivo_usuarios_json='usuarios.json'):
        self.archivo_json = archivo_json
        self.archivo_usuarios_json = archivo_usuarios_json
        self.libros = self.cargar_libros()  # Diccionario para acceder a libros por ISBN
        self.usuarios = self.cargar_usuarios()  # Conjunto para IDs de usuario únicos

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios_json, 'r') as archivo:
                datos_usuarios = json.load(archivo)
                return {usuario['id']: Usuario(**usuario) for usuario in datos_usuarios.values()}  # Diccionario de usuarios
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def guardar_usuarios(self):
        with open(self.archivo_usuarios_json, 'w') as archivo:
            json.dump({id: {"id": id, "nombre": usuario.nombre, "libros_prestados": [libro.isbn for libro in usuario.libros_prestados]} for id, usuario in self.usuarios.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def añadir_usuario(self, id_usuario, nombre_usuario):
        if id_usuario in self.usuarios:
            print("El ID de usuario ya está registrado.")
        else:
            usuario = Usuario(id_usuario, nombre_usuario)
            self.usuarios[id_usuario] = usuario
            self.guardar_usuarios()
            print(f"Usuario {nombre_usuario} añadido con éxito.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            # Se devuelven todos los libros prestados antes de dar de baja al usuario
            usuario.devolver_todos_libros()
            del self.usuarios[id_usuario]
            self.guardar_usuarios()
            print(f"Usuario {id_usuario} dado de baja con éxito.")
        else:
            print(f"El usuario con ID {id_usuario} no existe.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if libro and id_usuario in self.usuarios and not libro.prestado:
            libro.prestado = True
            # Asumimos que cada usuario tiene una lista de libros prestados
            self.usuarios[id_usuario].agregar_libro_prestado(libro)
            self.guardar_libros()
            self.guardar_usuarios()
            print(f"Libro {isbn} prestado a {id_usuario} con éxito.")
        else:
            print("El libro no está disponible o el ID del usuario no es válido.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if libro and id_usuario in self.usuarios and libro.prestado:
            libro.prestado = False
            self.usuarios[id_usuario].devolver_libro(libro)
            self.guardar_libros()
            self.guardar_usuarios()
            print(f"Libro {isbn} devuelto por {id_usuario} con éxito.")
        else:
            print("Error al devolver el libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

    def mostrar_usuarios(self):
        for usuario in self.usuarios.values():
            libros = ', '.join([libro.titulo for libro in usuario.libros_prestados])
            print(f"ID: {usuario.id} - Nombre: {usuario.nombre} - Libros prestados: {libros}")

    def buscar_libro(self, busqueda):
        resultados = []
        for libro in self.libros.values():
            if busqueda.lower() in libro.titulo.lower() or busqueda.lower() in libro.autor.lower() or busqueda.lower() in libro.isbn.lower():
                resultados.append(libro)
        return resultados

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Prestar Libro\n4. Devolver Libro\n5. Añadir Usuario\n6. Mostrar Usuarios\n7. Buscar Libro\n8. Dar Baja Usuario\n9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            biblioteca.mostrar_libros()
        elif opcion == '3':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == '4':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == '5':
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            biblioteca.añadir_usuario(id_usuario, nombre)
        elif opcion == '6':
            biblioteca.mostrar_usuarios()
        elif opcion == '7':
            busqueda = input("Introduzca el título, autor o ISBN del libro: ")
            resultados = biblioteca.buscar_libro(busqueda)
            if resultados:
                print("\nLibros encontrados:")
                for libro in resultados:
                    estado = "Prestado" if libro.prestado else "Disponible"
                    print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")
            else:
                print("No se encontraron libros que coincidan con la búsqueda.")
        elif opcion == '8':
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()