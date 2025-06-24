producto = {'codigo' : 12345, 'nombre' : 'Laptop', 'precio' : 1500.00, 'cantidad' : 10} # Diccionario de producto
print ("\n--- Claves del producto ---")
for clave in producto: # Iteración sobre las claves del diccionario
    print(clave)
print("\n--- Clave y valor del producto ---")
for clave, valor in producto.items(): # Iteración sobre las claves y valores del diccionario
    valor = producto [clave] # Obtención del valor de la clave
    print(f"{clave.capitalize()}: {valor}")
    # Fin del programa  
print ("Fabrizzio Lora (FaXx0)")
#------------------------------------------#
#------------------------------------------#
# Diccionario de productos
inventario =[]
comida = {'codigo' : 123, 'nombre' : 'frutas', 'precio' : 15.00, 'cantidad' : 10}
producto = {'codigo' : 456, 'nombre' : 'Laptop', 'precio' : 1500.00, 'cantidad' : 10}
limpieza = {'codigo' : 789, 'nombre' : 'jabon', 'precio' : 15.00, 'cantidad' : 10}
ropa = {'codigo' : 101112, 'nombre' : 'camisa', 'precio' : 15.00, 'cantidad' : 10}

 # Diccionario de producto
inventario.append(comida) # Agrega el diccionario de comida al inventario
inventario.append(producto) # Agrega el diccionario de producto al inventario
inventario.append(limpieza)# Agrega el diccionario de limpieza al inventario
inventario.append(ropa) # Agrega el diccionario de ropa al inventario      
for producto in inventario: # Iteración sobre los productos del inventario
    print("\n--- Clave y valor del producto ---")
    for clave, valor in producto.items(): # Iteración sobre las claves y valores del diccionario
        valor = producto [clave] # Obtención del valor de la clave
        print(f"{clave.capitalize()}: {valor}")
        # Fin del programa
print ("Fabrizzio Lora (FaXx0)")

#------------------------------------------#
#------------------------------------------#

# Diccionario para una Canción
cancion = {
    "titulo": "Shape of You",
    "artista": "Ed Sheeran",
    "album": "Divide",
    "duracion_segundos": 233,
    "genero": "Pop",
    "fecha_lanzamiento": ["2017-01-06"], 
    "colaboradores": ["Johnny McDaid", "Steve Mac"]
}

# Diccionario para un Coche
coche = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Negro",
    "placa": "ABC-1234",
    "caracteristicas": {
        "tipo_motor": "Gasolina",
        "potencia_hp": 132,
        "transmision": "Automática"
    }
}

# Diccionario para un Post de Red Social
post_red_social = {
    "id_post": 987654321,
    "autor": "user.py",
    "contenido_texto": "¡Learning python!",
    "fecha_publicacion": "2025-06-23 15:30:00",
    "likes": 23,
}

# Imprimir 
print("Canción:")
print(cancion)
print("\nCoche:")
print(coche)
print("\nPost de Red Social:")
print(post_red_social)


