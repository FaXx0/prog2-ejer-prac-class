    # Autor: Fabrizzio Lora (FaXx0)
    # Descripción: Calcula el promedio de una lista de notas.    
Mis_notas = [10, 15, 13, 12, 14, 16, 17, 18, 19, 20] # Lista de notas
suma_total = 0 # Variable para almacenar la suma total de las notas

for nota in Mis_notas: # Bucle para sumar todas las notas de la lista
    suma_total += nota     # Suma de notas

promedio = suma_total / len(Mis_notas) # Cálculo del promedio
print(f"El promedio es: {promedio}")
print("Fabrizzio Lora (FaXx0)")
# Impresión del promedio
    # Fin del programa