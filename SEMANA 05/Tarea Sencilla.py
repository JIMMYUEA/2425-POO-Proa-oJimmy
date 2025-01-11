# Programa simple que utiliza diferentes tipos de datos en Python

# Definición de variables de diferentes tipos
numero_entero = 10  # Tipo de dato entero
numero_decimal = 3.14  # Tipo de dato flotante
cadena_texto = "Hola, mundo!"  # Tipo de dato cadena
booleano = True  # Tipo de dato booleano

# Imprimir los valores y sus tipos
print("Número entero:", numero_entero, "Tipo:", type(numero_entero))
print("Número decimal:", numero_decimal, "Tipo:", type(numero_decimal))
print("Cadena de texto:", cadena_texto, "Tipo:", type(cadena_texto))
print("Booleano:", booleano, "Tipo:", type(booleano))

# Lista que contiene diferentes tipos de datos
lista_varios_tipos = [numero_entero, numero_decimal, cadena_texto, booleano]
print("\nLista de varios tipos:", lista_varios_tipos)

# Agregar un nuevo elemento a la lista
lista_varios_tipos.append("Nuevo elemento")  # Agregando una cadena
print("Lista después de agregar un elemento:", lista_varios_tipos)

# Calcular la suma de los números en la lista
suma_numeros = numero_entero + numero_decimal
print("\nLa suma de", numero_entero, "y", numero_decimal, "es:", suma_numeros)

# Función para mostrar un mensaje
def mostrar_mensaje(mensaje):
    """Función que imprime un mensaje en la consola."""
    print(mensaje)

# Llamar a la función con un mensaje
mostrar_mensaje("Este es un mensaje desde una función.")

# Final del programa
print("\nFin del programa.")