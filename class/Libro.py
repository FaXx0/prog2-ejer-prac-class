def __init__(self, titulo, autor, isbn, paginas):
    self.titulo = titulo
    self.autor = autor
    self.isbn = isbn
    self.paginas = paginas
    self.disponible = True  # atributo extra por defecto

    def mostrar_info(self):
        print("📚 Información del Libro 📚")
        print(f"Título     : {self.titulo}")
        print(f"Autor      : {self.autor}")
        print(f"ISBN       : {self.isbn}")
        print(f"Páginas    : {self.paginas}")
        print(f"Disponible : {'Sí' if self.disponible else 'No'}")

# Ejemplo de uso (no te preocupes por crear objetos todavía, ¡solo define la clase!)
if __name__ == "__main__":
    # Creación de ejemplo para demostrar el funcionamiento
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
    libro1.mostrar_info()

    # Cambiar disponibilidad
    libro1.disponible = False
    print("\nDespués de cambiar disponibilidad:")
    libro1.mostrar_info()

print("¡Clase Libro definida correctamente!")
print("Fin del Ejercicio#1 Sarai Vidaurre")


print("-----------------------------------------------------------")

# Ejercicio 2

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.disponible = True  # Por defecto está disponible

    def mostrar_info(self):
        print("📚 Información del Libro 📚")
        print(f"Título     : {self.titulo}")
        print(f"Autor      : {self.autor}")
        print(f"ISBN       : {self.isbn}")
        print(f"Páginas    : {self.paginas}")
        print(f"Disponible : {'Sí' if self.disponible else 'No'}")

    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            print(f"✅ El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"⚠️ El libro '{self.titulo}' ya está prestado.")

    def devolver_libro(self):
        if not self.disponible:
            self.disponible = True
            print(f"✅ El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"ℹ️ El libro '{self.titulo}' ya estaba disponible.")


# Creación de instancias (objetos)

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)
libro2 = Libro("Raza de Bronce", "Alcides Arguedas", "978-99905-2-213-9", 250)

# Accediendo a atributos directamente
print(f"\nEl autor del primer libro es: {libro1.autor}")
print(f"El ISBN del segundo libro es: {libro2.isbn}")

# Mostrando información completa
print("\n--- Mostrando información completa ---")
libro1.mostrar_info()
libro2.mostrar_info()

# Usando los métodos de comportamiento
print("\n--- Préstamos y devoluciones ---")
libro1.prestar_libro()
libro1.prestar_libro()     # Intento de prestarlo otra vez

libro1.devolver_libro()
libro1.devolver_libro()    # Intento de devolverlo otra vez

libro2.prestar_libro()
libro2.devolver_libro()

print("¡Clase Libro con métodos definida correctamente!")
 print("FaXX0")