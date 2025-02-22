import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            # Si el archivo no existe, lo crea
            with open(self.archivo, 'w') as f:
                pass
            print("Archivo de inventario creado.")
            return

        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Error: El archivo de inventario no se encontró.")
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        if nombre in self.productos:
            print("El producto ya existe. Actualizando cantidad.")
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
        self.guardar_inventario()

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza un producto existente en el inventario."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre].cantidad = cantidad
            if precio is not None:
                self.productos[nombre].precio = precio
            self.guardar_inventario()
        else:
            print("El producto no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    # Agregar productos
    inventario.agregar_producto("Manzana", 10, 0.5)
    inventario.agregar_producto("Banana", 5, 0.3)

    # Mostrar inventario
    inventario.mostrar_inventario()

    # Actualizar un producto
    inventario.actualizar_producto("Manzana", cantidad=15)

    # Eliminar un producto
    inventario.eliminar_producto("Banana")

    # Mostrar inventario final
    inventario.mostrar_inventario()