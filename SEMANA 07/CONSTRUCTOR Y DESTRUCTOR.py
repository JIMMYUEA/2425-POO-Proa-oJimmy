class Archivo:
    def __init__(self, nombre_archivo):
        """Constructor que inicializa el nombre del archivo y lo abre en modo de escritura."""
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')  # Abre el archivo en modo escritura
        print(f"Archivo '{self.nombre_archivo}' abierto.")

    def escribir(self, contenido):
        """Método para escribir contenido en el archivo."""
        if self.archivo:
            self.archivo.write(contenido + '\n')  # Escribe el contenido en el archivo
            print(f"Escrito en '{self.nombre_archivo}': {contenido}")

    def cerrar(self):
        """Método para cerrar el archivo de forma manual."""
        if self.archivo:
            self.archivo.close()  # Cierra el archivo
            self.archivo = None  # Establece el atributo a None para evitar futuros accesos
            print(f"Archivo '{self.nombre_archivo}' cerrado manualmente.")

    def __del__(self):
        """Destructor que cierra el archivo si está abierto."""
        if self.archivo:
            self.archivo.close()  # Cierra el archivo
            print(f"Destructor: Archivo '{self.nombre_archivo}' cerrado automáticamente.")


# Función principal para demostrar el uso de la clase
def main():
    # Crear una instancia de Archivo
    archivo = Archivo("mi_archivo.txt")

    # Escribir contenido en el archivo
    archivo.escribir("Hola, mundo!")
    archivo.escribir("Este es un archivo de prueba.")

    # Cerrar el archivo manualmente
    archivo.cerrar()


# Ejecutar la función principal
if __name__ == "__main__":
    main()