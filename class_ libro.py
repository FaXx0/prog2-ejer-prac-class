"""producto_A = {"nombre": "Café", "precio_bs": 35.50}
 producto_B = {"name": "Azúcar", "price": 5.20, "stock_actual": 100} # Claves"""
#-----------------------------------------------------------------------#
"""Las acciones (funciones) que operan sobre los datos están definidas por fuera.
 # Los datos están en el diccionario
 un_producto = {"nombre": "Leche", "stock": 10}
 # La acción está en una función separada
 def vender_producto(producto_a_vender, cantidad):
 producto_a_vender["stock"] -= cantidad
 vender_producto(un_producto, 2)"""
#-----------------------------------------------------------------------#
"""# Por convención, los nombres de las clases usan CamelCase o PascalCase
 class Estudiante:
    
    # El Método Constructor: se ejecuta AUTOMÁTICAMENTE al crear un nuevo objeto
    def __init__(self, nombre_ingresado, edad_ingresada, carrera_ingresada):
      
        #El constructor inicializa los atributos del objeto.
        
        print(f"¡Creando un nuevo estudiante llamado {nombre_ingresado}!")
        
        # self: se refiere A LA INSTANCIA ESPECÍFICA del objeto que se está creando.
        # Creamos los ATRIBUTOS del objeto y les asignamos los valores recibidos.
        self.nombre = nombre_ingresado
        self.edad = edad_ingresada
        self.carrera = carrera_ingresada
        self.materias = [] # Podemos inicializar atributos con valores por defecto"""
#-----------------------------------------------------------------------#
""" # Al llamar a la clase como una función, se ejecuta __init__
 estudiante1 = Estudiante("Ana Soliz", 20, "Ing. de Sistemas")
 # El objeto 'estudiante1' se pasa automáticamente como el argumento 'self'
 # "Ana Soliz" se pasa a 'nombre_ingresado'
 # 20 se pasa a 'edad_ingresada'
 # "Ing. de Sistemas" se pasa a 'carrera_ingresada'
 # Accediendo a los atributos del objeto
 print(estudiante1.nombre)   # Salida: Ana Soliz
 print(estudiante1.edad)     # Salida: 20
"""
#-----------------------------------------------------------------------#
"""    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.materias = []
    # Un método de instancia
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")
    # Otro método que modifica el estado del objeto
    def inscribir_materia(self, nombre_materia):
        self.materias.append(nombre_materia)
        print(f"¡{self.nombre} se ha inscrito exitosamente en {nombre_materia}!")
 # Llamando a los métodos
 estudiante1 = Estudiante("Ana Soliz", 20, "Ing. de Sistemas")
 estudiante1.presentarse() # Llama al método del objeto estudiante1
 estudiante1.inscribir_materia("Programación II")
 estudiante1.inscribir_materia("Álgebra Lineal")
 print(f"Materias de Ana: {estudiante1.materias}")
"""
#-----------------------------------------------------------------------#
