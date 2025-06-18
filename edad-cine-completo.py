    # Verificador de Edad para Películas completo
    # Autor: Fabrizzio Lora (FaXx0)
    # Descripción: Este programa solicita la edad del usuario y le recomienda películas según su clasificación.  

# Función para obtener la clasificación de películas según la edad
def obtener_clasificacion(edad): # Función principal
    if edad < 0 or edad > 120: # Validación de edad
        return "Edad no válida." # Mensaje de error
    elif edad < 13: # Clasificación para menores de 13 años
        return "Te recomendamos películas clasificadas G o PG." # Mensaje de recomendación
    elif edad < 18: # Clasificación para mayores de 13 años y menores de 18 años
        return "Puedes ver películas clasificadas PG-13." # Mensaje de recomendación
    else: # Clasificación para mayores de 18 años    
        return "¡Puedes ver películas clasificadas R!" # Mensaje de recomendación

def pruebas(): # Función para pruebas de la función obtener_clasificacion (pruebas unitarias) 
    assert obtener_clasificacion(10) == "Te recomendamos películas clasificadas G o PG."
    "Prueba fallida: Niño de 10 años" 
    print("✅ Prueba 7 PASADA: Niño de 10 años") # Prueba 1
    assert obtener_clasificacion(13) == "Puedes ver películas clasificadas PG-13."
    "Prueba fallida: Límite Adolescente (13 años)"
    print("✅ Prueba 5 PASADA: Límite adolescente (13 años)") # Prueba 2
    assert obtener_clasificacion(17) == "Puedes ver películas clasificadas PG-13."
    "Prueba fallida: Adolescente de 17 años"
    print("✅ Prueba 6 PASADA: Adolescente de 17 años") # Prueba 3
    assert obtener_clasificacion(18) == "¡Puedes ver películas clasificadas R!"
    "Prueba fallida: Límite Adulto (18 años)"
    print("✅ Prueba 2 PASADA: Límite adulto (18 años)") # Prueba 4
    assert obtener_clasificacion(65) == "¡Puedes ver películas clasificadas R!"
    "Prueba fallida: Adulto mayor"
    print("✅ Prueba 3 PASADA: Adulto mayor de 65 años") # Prueba 5
    assert obtener_clasificacion(0) == "Te recomendamos películas clasificadas G o PG."
    "Prueba fallida: Edad 0 años"
    print("✅ Prueba 12 PASADA: Bebé de 0 años")# Prueba 6
    assert obtener_clasificacion(-1) == "Edad no válida."
    "Prueba fallida: Edad negativa"
    print("✅ Prueba 10 PASADA: Edad negativa (-1)") # Prueba 7
    assert obtener_clasificacion(150) == "Edad no válida."
    "Prueba fallida: Edad excesivamente alta"
    print("✅ Prueba 11 PASADA: Edad excesivamente alta (150)")# Prueba 8                     
    print("✅ Todas las pruebas pasaron.") # Mensaje de éxito
    print("🛡️  Nuestra función es robusta y maneja todos los casos correctamente.")
    # Fin de las pruebas

def pedir_edad(): # Función para pedir la edad del usuario y validarla (entrada de datos)
    while True: # Bucle hasta que el usuario ingrese un número válido (entrada de datos)
        try: # Intenta convertir la entrada del usuario a un número entero 
            return int(input("Ingresa tu edad: ")) # Retorna la edad ingresada por el usuario
        except ValueError: # Si la entrada no es un número válido, muestra un mensaje de error
            print("❌ Ingresa un número válido.") # Mensaje de error

def main(): # Función principal del programa (menú principal)
    print("🎬 Verificador de Edad para Películas 🎬") # Mensaje de bienvenida
    pruebas() # Ejecuta las pruebas unitarias
    edad = pedir_edad() # Pide la edad del usuario y la valida
    mensaje = obtener_clasificacion(edad) # Obtiene la clasificación de películas según la edad del usuario
    print("\n🎭 Clasificación:", mensaje) # Muestra la clasificación de películas según la edad del usuario
    print("🍿 ¡Disfrutina tu película!")# Mensaje de despedida
    print("Fabrizzio Lora (FaXx0)")

if __name__ == "__main__": # Si el archivo se ejecuta directamente, ejecuta la función main() (entrada al programa)
    main() # Ejecuta la función main() (entrada al programa)    # Fin del programa


##################################################################################################################################################################

