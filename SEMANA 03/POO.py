class Clima:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas diarias

    def ingresar_temperatura(self, temperatura):
        """Método para ingresar una temperatura diaria."""
        if isinstance(temperatura, (int, float)):
            self.temperaturas.append(temperatura)
        else:
            raise ValueError("La temperatura debe ser un número.")

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas."""
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_temperaturas(self):
        """Método para mostrar las temperaturas ingresadas."""
        return self.temperaturas


class ClimaSemanal(Clima):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base

    def ingresar_temperaturas_semanales(self):
        """Método para ingresar temperaturas para una semana (7 días)."""
        for dia in range(7):
            while True:
                try:
                    temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                    self.ingresar_temperatura(temperatura)  # Usa el método de la clase base
                    break  # Salir del bucle si la entrada es válida
                except ValueError as e:
                    print(e)

    def mostrar_promedio_semanal(self):
        """Método para mostrar el promedio semanal de temperaturas."""
        promedio = self.calcular_promedio()  # Usa el método de la clase base
        print(f"La temperatura promedio de la semana es: {promedio:.2f}°C")


# Función principal para ejecutar el programa
def main():
    clima_semanal = ClimaSemanal()  # Crear una instancia de ClimaSemanal
    print("Registro de temperaturas semanales")
    clima_semanal.ingresar_temperaturas_semanales()  # Ingresar temperaturas
    clima_semanal.mostrar_promedio_semanal()  # Mostrar promedio semanal

# Ejecutar la función principal
if __name__ == "__main__":
    main()