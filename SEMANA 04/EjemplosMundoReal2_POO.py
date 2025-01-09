class Libro:
    """Clase que representa un libro en la tienda."""

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.precio = precio  # Precio del libro

    def __str__(self):
        return f'{self.titulo} de {self.autor} - ${self.precio}'


class Cliente:
    """Clase que representa un cliente de la tienda."""

    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del cliente
        self.pedidos = []  # Lista de pedidos del cliente

    def hacer_pedido(self, libro, cantidad):
        """Crea un pedido para el cliente."""
        pedido = Pedido(self, libro, cantidad)
        self.pedidos.append(pedido)
        return pedido


class Pedido:
    """Clase que representa un pedido de un cliente."""

    def __init__(self, cliente, libro, cantidad):
        self.cliente = cliente  # Objeto de la clase Cliente
        self.libro = libro  # Objeto de la clase Libro
        self.cantidad = cantidad  # Cantidad de libros en el pedido

    def costo_total(self):
        """Calcula el costo total del pedido."""
        return self.libro.precio * self.cantidad

    def __str__(self):
        return f'Pedido de {self.cliente.nombre}: {self.cantidad} x {self.libro} - Costo total: ${self.costo_total()}'


# Ejemplo de uso
libro1 = Libro("El Quijote", "Miguel de Cervantes", 15)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 20)

cliente1 = Cliente("Ana Gómez")
pedido1 = cliente1.hacer_pedido(libro1, 2)
pedido2 = cliente1.hacer_pedido(libro2, 1)

print(pedido1)
print(pedido2)