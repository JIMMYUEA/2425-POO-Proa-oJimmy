# Clase base que representa un vehículo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca  # Atributo privado (encapsulación)
        self.__modelo = modelo  # Atributo privado (encapsulación)
        self.__año = año  # Atributo privado (encapsulación)

    def obtener_info(self):
        """Método que devuelve la información básica del vehículo."""
        return f"{self.__año} {self.__marca} {self.__modelo}"

    def sonido(self):
        """Método que debe ser sobrescrito en las clases derivadas."""
        raise NotImplementedError("Este método debe ser sobrescrito en la clase derivada.")


# Clase derivada que representa un coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Llama al constructor de la clase base
        self.puertas = puertas  # Atributo específico de Coche

    def obtener_info(self):
        """Sobrescribe el método de la clase base para incluir el número de puertas."""
        return f"{super().obtener_info()} - Puertas: {self.puertas}"

    def sonido(self):
        """Implementa el método sonido para el coche."""
        return "Vroom Vroom!"


# Clase derivada que representa una moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)  # Llama al constructor de la clase base
        self.tipo = tipo  # Atributo específico de Moto

    def obtener_info(self):
        """Sobrescribe el método de la clase base para incluir el tipo de moto."""
        return f"{super().obtener_info()} - Tipo: {self.tipo}"

    def sonido(self):
        """Implementa el método sonido para la moto."""
        return "Brrr Brrr!"


# Función principal para demostrar la funcionalidad del programa
def main():
    # Crear instancias de Coche y Moto
    coche1 = Coche("Toyota", "Corolla", 2020, 4)
    moto1 = Moto("Yamaha", "MT-07", 2021, "Deportiva")

    # Mostrar información de los vehículos
    print(coche1.obtener_info())  # Llama al método de Coche
    print(coche1.sonido())  # Llama al método de sonido de Coche

    print(moto1.obtener_info())  # Llama al método de Moto
    print(moto1.sonido())  # Llama al método de sonido de Moto

    # Ejemplo de polimorfismo
    vehiculos = [coche1, moto1]
    for vehiculo in vehiculos:
        print(vehiculo.obtener_info())  # Llama al método sobrescrito
        print(vehiculo.sonido())  # Llama al método sonido

# Ejecutar la función principal
if __name__ == "__main__":
    main()