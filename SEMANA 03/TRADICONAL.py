# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):  # Para una semana (7 días)
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                temperaturas.append(temperatura)
                break  # Salir del bucle si la entrada es válida
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    print("Registro de temperaturas semanales")
    temperaturas = ingresar_temperaturas()  # Ingresar temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcular promedio
    print(f"La temperatura promedio de la semana es: {promedio:.2f}°C")

# Ejecutar la función principal
if __name__ == "__main__":
    main()