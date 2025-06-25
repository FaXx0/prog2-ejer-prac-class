import json    # Importa el módulo json para manejar archivos JSON
import os      # Importa el módulo os para manejar rutas de archivos
import tkinter as tk # Importa el módulo tkinter para la interfaz gráfica
from tkinter import messagebox, simpledialog # Importa los módulos messagebox y simpledialog para mostrar mensajes y dialogos
ARCHIVO = "contactos.json" # Define la ruta del archivo JSON donde se guardarán los contactos
# ------------------ Clase Contacto ------------------ #
class Contacto: # Define la clase Contacto con sus atributos y métodos
    def __init__(self, id, nombre, telefonos, email): # Define el constructor de la clase Contacto
        self.id = id # Define el atributo id
        self.nombre = nombre # Define el atributo nombre
        self.telefonos = telefonos # Define el atributo telefonos
        self.email = email  # Define el atributo email
    def mostrar(self): # Define el método mostrar para mostrar los datos del contacto
        return f"{self.id} - {self.nombre} | Tels: {', '.join(self.telefonos)} | Email: {self.email}" # Retorna una cadena con los datos del contacto
    def agregar_telefono(self, nuevo): # Define el método agregar_telefono para agregar un nuevo teléfono al contacto
        self.telefonos.append(nuevo) # Agrega el nuevo teléfono a la lista de telefonos
    def to_dict(self): # Define el método to_dict para convertir el objeto Contacto a un diccionario
        return { 
            "id": self.id,
            "nombre": self.nombre,
            "telefonos": self.telefonos,
            "email": self.email
        } # Retorna un diccionario con los datos del contacto

# ------------------ Clase Gestor ------------------ #
class GestorContactos: # Define la clase GestorContactos con sus atributos y métodos
    def __init__(self): # Define el constructor de la clase GestorContactos
        self.contactos = [] # Define el atributo contactos como una lista vacía
        self.proximo_id = 1 # Define el atributo proximo_id como 1
        self.cargar() # Carga los contactos desde el archivo JSON
    def agregar(self, nombre, telefonos, email): # Define el método agregar para agregar un nuevo contacto
        c = Contacto(self.proximo_id, nombre, telefonos, email) # Crea un nuevo objeto Contacto con los datos ingresados
        self.contactos.append(c) # Agrega el nuevo contacto a la lista de contactos
        self.proximo_id += 1 # Incrementa el atributo proximo_id en 1
        self.guardar() # Guarda los contactos en el archivo JSON
    def eliminar(self, id): # Define el método eliminar para eliminar un contacto por su id
        self.contactos = [c for c in self.contactos if c.id != id] #Elimina el contacto de la lista de contactos
        self.guardar() # Guarda los contactos en el archivo JSON
    def editar(self, id, nombre, telefonos, email): # Define el método editar para editar un contacto por su id
        for c in self.contactos: # Recorre la lista de contactos
            if c.id == id: # Si el id del contacto es igual al id ingresado
                c.nombre = nombre # Edita el atributo nombre
                c.telefonos = telefonos # Edita el atributo telefonos
                c.email = email  # Edita el atributo email
                break  # Sale del bucle
        self.guardar() # Guarda los contactos en el archivo JSON
    def buscar_por_id(self, id): # Define el método buscar_por_id para buscar un contacto por su id
        for c in self.contactos:
            if c.id == id:
                return c
        return None

    def guardar(self):
        datos = [c.to_dict() for c in self.contactos]
        with open(ARCHIVO, "w") as f:
            json.dump(datos, f, indent=2)

    def cargar(self):
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                datos = json.load(f)
                for d in datos:
                    c = Contacto(d["id"], d["nombre"], d["telefonos"], d["email"])
                    self.contactos.append(c)
                if self.contactos:
                    self.proximo_id = max(c.id for c in self.contactos) + 1

# ------------------ Interfaz Gráfica ------------------ #
gestor = GestorContactos() # Crea un objeto GestorContactos
def actualizar_lista(): # Define la función actualizar_lista para actualizar la lista de contactos en la interfaz gráfica
    lista.delete(0, tk.END) # Elimina todos los elementos de la lista
    for c in gestor.contactos: # Recorre la lista de contactos
        lista.insert(tk.END, c.mostrar()) # Inserta el contacto en la lista
def agregar_contacto_gui(): # Define la función agregar_contacto_gui para agregar un nuevo contacto desde la interfaz gráfica
    nombre = entry_nombre.get() # Obtiene el nombre ingresado en el campo de entrada
    email = entry_email.get() # Obtiene el email ingresado en el campo de entrada
    telefonos = entry_telefonos.get().split(",") # Obtiene los telefonos ingresados en el campo de entrada y los separa por comas
    if nombre and telefonos: # Si el nombre y los telefonos no están vacíos
        gestor.agregar(nombre, telefonos, email) # Agrega el nuevo contacto al gestor
        entry_nombre.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefonos.delete(0, tk.END)
        actualizar_lista()

def eliminar_contacto_gui():
    sel = lista.curselection()
    if sel:
        id_str = lista.get(sel[0]).split(" ")[0]
        gestor.eliminar(int(id_str))
        actualizar_lista()

def editar_contacto_gui():
    sel = lista.curselection()
    if sel:
        id_str = lista.get(sel[0]).split(" ")[0]
        contacto = gestor.buscar_por_id(int(id_str))
        if contacto:
            nuevo_nombre = simpledialog.askstring("Editar nombre", "Nuevo nombre:", initialvalue=contacto.nombre)
            nuevo_email = simpledialog.askstring("Editar email", "Nuevo email:", initialvalue=contacto.email)
            nuevos_tel = simpledialog.askstring("Editar teléfonos", "Nuevos números separados por coma:", initialvalue=", ".join(contacto.telefonos))
            if nuevo_nombre and nuevos_tel:
                gestor.editar(contacto.id, nuevo_nombre, nuevos_tel.split(","), nuevo_email)
                actualizar_lista()

# ------------------ Ventana ------------------ #
root = tk.Tk() # Crea la ventana principal
root.title("Gestor de Contactos 2.0") # Define el título de la ventana
tk.Label(root, text="Nombre").pack() # Crea una etiqueta para el nombre
entry_nombre = tk.Entry(root) # Crea un campo de entrada para el nombre
entry_nombre.pack() # Empaqueta el campo de entrada para el nombre
tk.Label(root, text="Email").pack() # Crea una etiqueta para el email
entry_email = tk.Entry(root) # Crea un campo de entrada para el email
entry_email.pack() # Empaqueta el campo de entrada para el email
tk.Label(root, text="Teléfonos (separados por coma)").pack() # Crea una etiqueta para los teléfonos
entry_telefonos = tk.Entry(root) # Crea un campo de entrada para los teléfonos
entry_telefonos.pack() # Empaqueta el campo de entrada para los teléfonos
tk.Button(root, text="Agregar", command=agregar_contacto_gui, bg="lightgreen").pack(pady=5)
lista = tk.Listbox(root, width=60)
lista.pack()
tk.Button(root, text="✏️ Editar", command=editar_contacto_gui, bg="lightblue").pack(pady=2)
tk.Button(root, text="🗑️ Eliminar", command=eliminar_contacto_gui, bg="salmon").pack(pady=2)
actualizar_lista()
root.mainloop()