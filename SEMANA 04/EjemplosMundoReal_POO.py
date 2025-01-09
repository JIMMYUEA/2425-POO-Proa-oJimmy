class Habitacion:
    """Clase que representa una habitación en el hotel."""

    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (simple, doble, suite)
        self.precio = precio  # Precio por noche

    def __str__(self):
        return f'Habitación {self.numero}: {self.tipo} - ${self.precio} por noche'


class Reserva:
    """Clase que representa una reserva en el hotel."""

    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente  # Nombre del cliente
        self.habitacion = habitacion  # Objeto de la clase Habitacion
        self.noches = noches  # Número de noches de la reserva

    def costo_total(self):
        """Calcula el costo total de la reserva."""
        return self.habitacion.precio * self.noches

    def __str__(self):
        return f'Reserva de {self.cliente} en {self.habitacion} por {self.noches} noches. Costo total: ${self.costo_total()}'


class Hotel:
    """Clase que representa un hotel."""

    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del hotel
        self.habitaciones = []  # Lista de habitaciones

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones disponibles en el hotel."""
        for habitacion in self.habitaciones:
            print(habitacion)


# Ejemplo de uso
hotel = Hotel("Hotel Paraíso")
hotel.agregar_habitacion(Habitacion(101, "Doble", 100))
hotel.agregar_habitacion(Habitacion(102, "Suite", 200))

print("Habitaciones disponibles:")
hotel.mostrar_habitaciones()

reserva1 = Reserva("Juan Pérez", hotel.habitaciones[0], 3)
print(reserva1)