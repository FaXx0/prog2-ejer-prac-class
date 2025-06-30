import tkinter as tk # Importamos la biblioteca tkinter para crear la interfaz gráfica
from tkinter import messagebox, simpledialog, ttk # Importamos messagebox y simpledialog para mostrar mensajes y dialogos
from PIL import Image, ImageTk # Importamos Image y ImageTk de PIL para manejar imágenes
import json # Importamos json para manejar archivos JSON
import os # Importamos os para manejar rutas de archivos
import sys # Importamos sys para manejar la salida del programa

ARCHIVO_INVENTARIO = "inventario.json" # Definimos el nombre del archivo JSON para el inventario
ARCHIVO_USUARIOS = "usuarios.json" # Definimos el nombre del archivo JSON para los usuarios
ARCHIVO_ADMINISTRADORES = "administradores.json" # Definimos el nombre del archivo JSON para los administradores
inventario = [] # Inicializamos el inventario como una lista vacía
usuarios = {} # Inicializamos el diccionario de usuarios
administradores = {} # Inicializamos el diccionario de administradores
usuario_actual = None # Inicializamos el usuario actual como None
carrito = [] # Inicializamos el carrito de compras como una lista vacía

CATEGORIAS_VALIDAS = ["lacteos", "carnes", "panaderia", "frutas y verduras"] # Definimos las categorías válidas para los productos

def cargar_inventario(): # Función para cargar el inventario desde el archivo JSON
    global inventario # Declaramos que vamos a usar la variable global inventario
    if os.path.exists(ARCHIVO_INVENTARIO): # Si el archivo existe, lo abrimos y cargamos el inventario
        with open(ARCHIVO_INVENTARIO, "r") as f: # Abrimos el archivo en modo lectura
            try: # Intentamos cargar el inventario desde el archivo JSON
                inventario = json.load(f) # Cargamos el inventario desde el archivo JSON
            except json.JSONDecodeError: # Si hay un error al decodificar el JSON, inicializamos el inventario como una lista vacía
                inventario = [] # Inicializamos el inventario como una lista vacía

def guardar_inventario(): # Función para guardar el inventario en el archivo JSON
    with open(ARCHIVO_INVENTARIO, "w") as f: # Abrimos el archivo en modo escritura
        json.dump(inventario, f, indent=4) # Guardamos el inventario en el archivo JSON con indentación de 4 espacios

def cargar_usuarios(): # Función para cargar los usuarios desde el archivo JSON
    global usuarios # Declaramos que vamos a usar la variable global usuarios
    if os.path.exists(ARCHIVO_USUARIOS): # Si el archivo existe, lo abrimos y cargamos los usuarios
        with open(ARCHIVO_USUARIOS, "r") as f: # Abrimos el archivo en modo lectura
            try: # Intentamos cargar los usuarios desde el archivo JSON
                usuarios = json.load(f) # Cargamos los usuarios desde el archivo JSON
            except json.JSONDecodeError: # Si hay un error al decodificar el JSON, inicializamos el diccionario de usuarios
                usuarios = {} # Inicializamos el diccionario de usuarios
    else: # Si el archivo no existe, creamos un usuario propietario por defecto
        usuarios["propietario"] = {"password": "super123", "rol": "propietario"} # Creamos un usuario propietario por defecto
        guardar_usuarios() # Guardamos los usuarios en el archivo JSON

def guardar_usuarios(): # Función para guardar los usuarios en el archivo JSON
    with open(ARCHIVO_USUARIOS, "w") as f: # Abrimos el archivo en modo escritura
        json.dump(usuarios, f, indent=4) # Guardamos los usuarios en el archivo JSON con indentación de 4 espacios

def cargar_administradores(): # Función para cargar los administradores desde el archivo JSON
    global administradores # Declaramos que vamos a usar la variable global administradores
    if os.path.exists(ARCHIVO_ADMINISTRADORES): # Si el archivo existe, lo abrimos y cargamos los administradores
        with open(ARCHIVO_ADMINISTRADORES, "r") as f: # Abrimos el archivo en modo lectura
            try: # Intentamos cargar los administradores desde el archivo JSON
                administradores = json.load(f) # Cargamos los administradores desde el archivo JSON
            except json.JSONDecodeError: # Si hay un error al decodificar el JSON, inicializamos el diccionario de administradores
                administradores = {} # Inicializamos el diccionario de administradores
    else: # Si el archivo no existe, inicializamos el diccionario de administradores
        administradores = {} # Inicializamos el diccionario de administradores
        guardar_administradores() # Guardamos los administradores en el archivo JSON

def guardar_administradores(): # Función para guardar los administradores en el archivo JSON
    with open(ARCHIVO_ADMINISTRADORES, "w") as f: # Abrimos el archivo en modo escritura
        json.dump(administradores, f, indent=4) # Guardamos los administradores en el archivo JSON con indentación de 4 espacios
 
def login(ventana_raiz): # Función para mostrar la ventana de login
    global usuario_actual # Declaramos que vamos a usar la variable global usuario_actual

    ventana_login = tk.Toplevel(ventana_raiz) # Creamos una nueva ventana
    ventana_login.title("🔸 Inicio de sesión 🔸") # Establecemos el título de la ventana
    ventana_login.geometry("600x500") # Establecemos el tamaño de la ventana
    ventana_login.resizable(False, False) # Deshabilitamos el redimensionamiento de la ventana
    ventana_login.grab_set()    # Hacer modal (ventana_login no se puede interactuar hasta que se cierre)      

    # Fondo
    try: # Intentamos cargar la imagen de fondo
        fondo = Image.open("fondoLD.png") # Cargamos la imagen de fondo
        fondo = fondo.resize((600, 500)) # Redimensionamos la imagen de fondo
        fondo_tk = ImageTk.PhotoImage(fondo) # Convertimos la imagen de fondo a un objeto PhotoImage
        fondo_label = tk.Label(ventana_login, image=fondo_tk) # Creamos un Label con la imagen de fondo
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1) # Colocamos el Label en la ventana
        fondo_label.image = fondo_tk  # Mantener referencia a la imagen para evitar que sea eliminada por el recolector de basura
    except Exception as e: # Si hay un error al cargar la imagen de fondo, mostramos un mensaje de error
        print(f"Error cargando imagen: {e}") # Imprimimos el error en la consola
        ventana_login.configure(bg="#A176A7") # Establecemos el color de fondo de la ventana

    # Contenedor principal
    frame = tk.Frame(ventana_login, bg="#ffffff", padx=20, pady=20) # Creamos un Frame con fondo blanco y padding
    frame.place(relx=0.5, rely=0.5, anchor="center") # Colocamos el Frame en el centro de la ventana

    tk.Label(frame, text="🛒 La Despensa Feliz", font=("Comic Sans MS", 18, "bold"), bg="#ffffff", fg="#006400").pack(pady=(0, 5)) # Creamos un Label con el título de la aplicación (La Despensa Feliz) en color verde oscuro
    tk.Label(frame, text="Inicio de sesión", font=("Arial", 13), bg="#ffffff").pack(pady=(0, 15)) # Creamos un Label con el subtítulo de la aplicación (Inicio de sesión)

    tk.Label(frame, text="Usuario:", bg="#ffffff").pack(anchor="w") # Creamos un Label con el texto "Usuario:"
    entry_usuario = tk.Entry(frame, width=30) # Creamos un Entry para ingresar el nombre de usuario
    entry_usuario.pack(pady=(0, 10)) # Colocamos el Entry en el Frame con padding vertical de 10

    tk.Label(frame, text="Contraseña:", bg="#ffffff").pack(anchor="w") # Creamos un Label con el texto "Contraseña:" (Contraseña) en color blanco
    entry_contraseña = tk.Entry(frame, show="*", width=30) # Creamos un Entry para ingresar la contraseña (Contraseña) en color blanco
    entry_contraseña.pack(pady=(0, 15))  # Colocamos el Entry en el Frame con padding vertical de 15 (Contraseña)

    # Acción de login (Contraseña)
    def intentar_login(event=None): # Definimos la función intentar_login que se ejecuta al presionar el botón "Ingresar" o al presionar la tecla Enter
        global usuario_actual # Declaramos que vamos a usar la variable global usuario_actual
        usuario = entry_usuario.get() # Obtenemos el nombre de usuario ingresado
        contraseña = entry_contraseña.get() # Obtenemos la contraseña ingresada

        if usuario in administradores and contraseña == administradores[usuario]["password"]: # Si el usuario es un administrador y la contraseña es correcta, establecemos el usuario actual como administrador
            usuario_actual = {"nombre": usuario, "rol": "admin"} # Establecemos el usuario actual como administrador
            messagebox.showinfo("Acceso", f"Bienvenido administrador {usuario}", parent=ventana_login) # Mostramos un mensaje de bienvenida 
            ventana_login.destroy() # Cerramos la ventana de login
        elif usuario in usuarios and contraseña == usuarios[usuario]["password"]: # Si el usuario es un empleado y la contraseña es correcta, establecemos el usuario actual como empleado
            usuario_actual = {"nombre": usuario, "rol": usuarios[usuario]["rol"]} # Establecemos el usuario actual como empleado
            messagebox.showinfo("Acceso", f"Bienvenido {usuario}", parent=ventana_login) # Mostramos un mensaje de bienvenida 
            ventana_login.destroy() # Cerramos la ventana de login 
        else: # Si el usuario o la contraseña son incorrectos, mostramos un mensaje de error
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.", parent=ventana_login) # Mostramos un mensaje de error 

    def acceder_como_cliente(): # Definimos la función acceder_como_cliente que se ejecuta al presionar el botón "Soy Cliente"
        global usuario_actual # Declaramos que vamos a usar la variable global usuario_actual
        usuario_actual = {"nombre": "cliente", "rol": "cliente"} # Establecemos el usuario actual como cliente
        messagebox.showinfo("Bienvenido", "Has ingresado como cliente.", parent=ventana_login) # Mostramos un mensaje de bienvenida
        ventana_login.destroy() # Cerramos la ventana de login

    # Botones
    btn_ingresar = tk.Button(frame, text="Ingresar", command=intentar_login, bg="#28a745", fg="white", width=25) # Creamos un botón "Ingresar" que ejecuta la función intentar_login al ser presionado
    btn_ingresar.pack(pady=(0, 10)) # Colocamos el botón en el Frame con padding vertical de 10

    btn_cliente = tk.Button(frame, text="👤 Soy Cliente", command=acceder_como_cliente, bg="#E0BBE4", fg="black", font=("Arial", 11), width=25) # Creamos un botón "Soy Cliente" que ejecuta la función acceder_como_cliente al ser presionado
    btn_cliente.pack() # Colocamos el botón en el Frame

    ventana_login.bind("<Return>", intentar_login) # Asociamos la tecla Enter con la función intentar_login
    ventana_login.wait_window() # Esperamos a que la ventana de login se cierre para continuar con el programa 
 
def mostrar_vista_cliente(ventana_raiz): # Función para mostrar la vista del cliente 
    global carrito # Declaramos que vamos a usar la variable global carrito
    carrito.clear() # Limpiamos el carrito al iniciar la vista del cliente
    ventana_cliente = tk.Toplevel(ventana_raiz) # Creamos una nueva ventana para la vista del cliente
    ventana_cliente.title("🛍️ Tienda - Cliente") # Establecemos el título de la ventana
    ventana_cliente.geometry("850x550") # Establecemos el tamaño de la ventana
    ventana_cliente.grab_set()  # Hacer modal (ventana_cliente no se puede interactuar hasta que se cierre)

    tk.Label(ventana_cliente, text="🛒 Productos Disponibles", font=("Helvetica", 16, "bold")).pack(pady=10) # Creamos un Label con el título de la sección de productos disponibles

    frame_tree = tk.Frame(ventana_cliente) # Creamos un Frame para el Treeview de productos disponibles (Arbol de productos disponibles)    # Creamos un Treeview para mostrar los productos disponibles
    frame_tree.pack(fill="both", expand=True, padx=20) # Colocamos el Frame en la ventana con padding horizontal de 20

    tree = ttk.Treeview(frame_tree, columns=("nombre", "precio", "categoria", "stock"), show="headings", height=12) # Creamos un Treeview con las columnas nombre, precio, categoria y stock
    tree.heading("nombre", text="Nombre")     # Establecemos el texto de la columna nombre
    tree.heading("precio", text="Precio")     # Establecemos el texto de la columna precio
    tree.heading("categoria", text="Categoría")     # Establecemos el texto de la columna categoria
    tree.heading("stock", text="Stock")     # Establecemos el texto de la columna stock
    tree.column("nombre", width=200)     # Establecemos el ancho de la columna nombre
    tree.column("precio", width=100)     # Establecemos el ancho de la columna precio
    tree.column("categoria", width=150)     # Establecemos el ancho de la columna categoria
    tree.column("stock", width=100)     # Establecemos el ancho de la columna stock
    tree.pack(fill="both", expand=True)     # Colocamos el Treeview en el Frame

    for producto in inventario: # Recorremos el inventario y agregamos los productos al Treeview
        if all(k in producto for k in ("nombre", "precio", "categoria", "stock")):
            tree.insert("", "end", values=(producto["nombre"], producto["precio"], producto["categoria"], producto["stock"])) # Agregamos el producto al Treeview con los valores correspondientes (Arbol de productos disponibles)    # Función para agregar un producto al carrito (Carrito de compras)    # Función para agregar un producto al carrito (Carrito de compras)

    def agregar_al_carrito(): # Definimos la función agregar_al_carrito que se ejecuta al presionar el botón "Agregar al Carrito"
        item = tree.focus() # Obtenemos el item seleccionado en el Treeview (Arbol de productos disponibles)
        if not item: # Si no hay item seleccionado, mostramos un mensaje de error
            messagebox.showwarning("⚠️", "Selecciona un producto.", parent=ventana_cliente) # Mostramos un mensaje de error (Carrito de compras)    # Si hay item seleccionado, obtenemos los valores del producto seleccionado
            return # Salimos de la función
        producto = tree.item(item, "values") # Obtenemos los valores del producto seleccionado (Arbol de productos disponibles)    # Obtenemos los valores del producto seleccionado
        nombre = producto[0] # Obtenemos el nombre del producto seleccionado
        precio = float(producto[1]) # Obtenemos el precio del producto seleccionado
        stock = int(producto[3]) # Obtenemos el stock del producto seleccionado

        if stock <= 0: # Si el stock es menor o igual a 0, mostramos un mensaje de error
            messagebox.showerror("Sin stock", "Este producto está agotado.", parent=ventana_cliente)  # Mostramos un mensaje de error (Carrito de compras)    # Si el stock es mayor a 0, mostramos un dialogo para ingresar la cantidad a agregar al carrito
            return # Salimos de la función

        cantidad = simpledialog.askinteger("Cantidad", f"¿Cuántas unidades de '{nombre}' deseas?", 
                                          minvalue=1, maxvalue=stock, parent=ventana_cliente) # Mostramos un dialogo para ingresar la cantidad a agregar al carrito (Carrito de compras)    # Si no se ingresa una cantidad, salimos de la función
        if cantidad is None: # Si no se ingresa una cantidad, salimos de la función
            return # Salimos de la función # Agregamos el producto al carrito con la cantidad ingresada

        carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad}) # Agregamos el producto al carrito con la cantidad ingresada
        messagebox.showinfo("Agregado", f"✅ {cantidad} x '{nombre}' agregado al carrito.", parent=ventana_cliente) # Mostramos un mensaje de éxito (Carrito de compras)    # Función para ver el carrito de compras

    def ver_carrito(): # Definimos la función ver_carrito que se ejecuta al presionar el botón "Ver Carrito"
        if not carrito: # Si el carrito está vacío, mostramos un mensaje de información    # Si el carrito está vacío, mostramos un mensaje de información
            messagebox.showinfo("Carrito", "Tu carrito está vacío.", parent=ventana_cliente) # Mostramos un mensaje de información (Carrito de compras)    # Si el carrito no está vacío, mostramos una ventana con los productos del carrito
            return # Salimos de la función

        ventana_carrito = tk.Toplevel(ventana_cliente)  # Creamos una nueva ventana para el carrito de compras
        ventana_carrito.title("🧺 Carrito de Compras")  # Establecemos el título de la ventana
        ventana_carrito.geometry("500x400")  # Establecemos el tamaño de la ventana
        ventana_carrito.transient(ventana_cliente)  # Hacerla hija de la ventana cliente
        ventana_carrito.grab_set()  # Hacer modal (ventana_carrito no se puede interactuar hasta que se cierre)

        tk.Label(ventana_carrito, text="🧺 Tu Carrito", font=("Arial", 14, "bold")).pack(pady=10) # Creamos un Label con el título de la sección del carrito de compras

        texto_carrito = tk.Text(ventana_carrito, height=15, width=60)     # Creamos un Text para mostrar los productos del carrito
        texto_carrito.pack(padx=10) # Colocamos el Text en la ventana con padding horizontal de 10 (Carrito de compras)    # Mostramos los productos del carrito en el Text

        total = 0 # Inicializamos el total en 0 (Carrito de compras)    # Mostramos los productos del carrito en el Text
        for item in carrito: # Recorremos el carrito y mostramos los productos en el Text
            subtotal = item['cantidad'] * item['precio'] # Calculamos el subtotal del producto (Carrito de compras)    # Calculamos el subtotal del producto
            linea = f"{item['cantidad']} x {item['nombre']} @ {item['precio']:.2f} Bs = {subtotal:.2f} Bs\n" # Creamos una línea con la información del producto (Carrito de compras)    # Creamos una línea con la información del producto
            texto_carrito.insert("end", linea)  # Insertamos la línea en el Text (Carrito de compras)    # Insertamos la línea en el Text    # Insertamos la línea en el Text
            total += subtotal  # Sumamos el subtotal al total (Carrito de compras)    # Sumamos el subtotal al total

        texto_carrito.insert("end", f"\n💵 Total: {total:.2f} Bs") # Insertamos el total en el Text (Carrito de compras)    # Insertamos el total en el Text
        texto_carrito.config(state="disabled") # Deshabilitamos el Text para que no se pueda modificar (Carrito de compras)    # Deshabilitamos el Text para que no se pueda modificar

    def finalizar_compra(): # Definimos la función finalizar_compra que se ejecuta al presionar el botón "Finalizar Compra"
        if not carrito: # Si el carrito está vacío, mostramos un mensaje de información
            messagebox.showinfo("Carrito vacío", "Agrega productos antes de finalizar la compra.", parent=ventana_cliente) # Mostramos un mensaje de información (Carrito de compras)    # Si el carrito está vacío, mostramos un mensaje de información
            return # Salimos de la función

        confirmacion = messagebox.askyesno("Confirmar", "¿Deseas finalizar tu compra?", parent=ventana_cliente) # Mostramos un mensaje de confirmación (Carrito de compras)    # Mostramos un mensaje de confirmación (Carrito de compras)    # Mostramos un mensaje de confirmación
        if not confirmacion: # Si el usuario no confirma, salimos de la función
            return # Salimos de la función

        for item in carrito: # Recorremos el carrito y actualizamos el stock de los productos en el inventario
            for producto in inventario: # Recorremos el inventario y actualizamos el stock de los productos en el inventario
                if producto["nombre"] == item["nombre"]: # Si el nombre del producto en el inventario coincide con el nombre del producto en el carrito, actualizamos el stock
                    producto["stock"] -= item["cantidad"] # Actualizamos el stock del producto en el inventario
                    break # Salimos del bucle interno
        guardar_inventario() # Guardamos el inventario actualizado en el archivo JSON
        total = sum(p["precio"] * p["cantidad"] for p in carrito) # Calculamos el total de la compra
        carrito.clear() # Limpiamos el carrito después de la compra
        messagebox.showinfo("✅ Compra Exitosa", f"Gracias por tu compra.\nTotal pagado: {total:.2f} Bs", parent=ventana_cliente) # Mostramos un mensaje de éxito (Carrito de compras)    # Mostramos un mensaje de éxito
        ventana_cliente.destroy() # Cerramos la ventana del cliente después de finalizar la compra

    frame_botones = tk.Frame(ventana_cliente) # Creamos un Frame para los botones de acción (Carrito de compras)
    frame_botones.pack(pady=10) # Colocamos el Frame en la ventana con padding vertical de 10

    tk.Button(frame_botones, text="➕ Agregar al Carrito", command=agregar_al_carrito, bg="#D9F0E5").grid(row=0, column=0, padx=10) # Creamos un botón "Agregar al Carrito" que ejecuta la función agregar_al_carrito al ser presionado
    tk.Button(frame_botones, text="🧺 Ver Carrito", command=ver_carrito, bg="#FFD6A5").grid(row=0, column=1, padx=10) # Creamos un botón "Ver Carrito" que ejecuta la función ver_carrito al ser presionado
    tk.Button(frame_botones, text="✅ Finalizar Compra", command=finalizar_compra, bg="#C0E8D5").grid(row=0, column=2, padx=10) # Creamos un botón "Finalizar Compra" que ejecuta la función finalizar_compra al ser presionado

    ventana_cliente.wait_window() # Esperamos a que la ventana del cliente se cierre para continuar con el programa

def crear_administrador(parent): # Función para crear un nuevo administrador (Crear administrador)
    if usuario_actual["rol"] != "propietario": # Si el usuario actual no es el propietario, mostramos un mensaje de error (Crear administrador)    # Si el usuario actual no es el propietario, mostramos un mensaje de error
        messagebox.showerror("Acceso denegado", "Solo el propietario puede crear administradores.", parent=parent) # Mostramos un mensaje de error (Crear administrador)    # Mostramos un mensaje de error
        return # Salimos de la función
    nuevo_admin = simpledialog.askstring("Crear administrador", "Nombre del nuevo administrador:", parent=parent) # Mostramos un dialogo para ingresar el nombre del nuevo administrador (Crear administrador)    # Mostramos un dialogo para ingresar el nombre del nuevo administrador
    if not nuevo_admin or nuevo_admin in administradores: # Si el nombre del nuevo administrador no es válido o ya existe, mostramos un mensaje de error (Crear administrador)    # Si el nombre del nuevo administrador no es válido o ya existe, mostramos un
        messagebox.showerror("Error", "Nombre inválido o ya existe.", parent=parent) # Mostramos un mensaje de error (Crear administrador)    # Mostramos un mensaje de error
        return # Salimos de la función
    nueva_contraseña = simpledialog.askstring("Crear administrador", "Contraseña para el administrador:", parent=parent) # Mostramos un dialogo para ingresar la contraseña del nuevo administrador (Crear administrador)    # Mostramos un dialogo para ingresar la contraseña del nuevo administrador
    if not nueva_contraseña: # Si la contraseña no es válida, mostramos un mensaje de error (Crear administrador)    # Si la contraseña no es válida, mostramos un mensaje de error
        messagebox.showerror("Error", "Contraseña no válida.", parent=parent) # Mostramos un mensaje de error (Crear administrador)    # Mostramos un mensaje de error
        return # Salimos de la función
    administradores[nuevo_admin] = {"password": nueva_contraseña}  
    guardar_administradores()  # Guardamos los administradores actualizados en el archivo JSON
    messagebox.showinfo("Éxito", f"Administrador '{nuevo_admin}' creado correctamente.", parent=parent) # Mostramos un mensaje de éxito (Crear administrador)    # Mostramos un mensaje de éxito

def crear_empleado(parent): # Función para crear un nuevo empleado (Crear empleado)
    if usuario_actual["rol"] not in ["propietario", "admin"]: # Si el usuario actual no es el propietario o un administrador, mostramos un mensaje de error (Crear empleado)    # Si el usuario actual no es el propietario o un administrador, mostramos un mensaje de error
        messagebox.showerror("Acceso denegado", "Solo propietarios o administradores pueden crear empleados.", parent=parent) # Mostramos un mensaje de error (Crear empleado)    # Mostramos un mensaje de error
        return # Salimos de la función
    nuevo_emp = simpledialog.askstring("Crear empleado", "Nombre del nuevo empleado:", parent=parent) # Mostramos un dialogo para ingresar el nombre del nuevo empleado (Crear empleado)    # Mostramos un dialogo para ingresar el nombre del nuevo empleado
    if not nuevo_emp or nuevo_emp in usuarios: # Si el nombre del nuevo empleado no es válido o ya existe, mostramos un mensaje de error (Crear empleado)    # Si el nombre del nuevo empleado no es válido o ya existe, mostramos un mensaje de error
        messagebox.showerror("Error", "Nombre inválido o ya existe.", parent=parent) # Mostramos un mensaje de error (Crear empleado)    # Mostramos un mensaje de error
        return # Salimos de la función
    nueva_contraseña = simpledialog.askstring("Crear empleado", "Contraseña para el empleado:", parent=parent) # Mostramos un dialogo para ingresar la contraseña del nuevo empleado (Crear empleado)    # Mostramos un dialogo para ingresar la contraseña del nuevo empleado
    if not nueva_contraseña:
        messagebox.showerror("Error", "Contraseña no válida.", parent=parent)
        return
    usuarios[nuevo_emp] = {"password": nueva_contraseña, "rol": "empleado"}
    guardar_usuarios()
    messagebox.showinfo("Éxito", f"Empleado '{nuevo_emp}' creado correctamente.", parent=parent)

def listar_administradores(parent):
    if not administradores:
        messagebox.showinfo("Administradores", "No hay administradores registrados.", parent=parent)
        return
    lista = "\n".join(administradores.keys())
    messagebox.showinfo("Administradores", lista, parent=parent)

def listar_empleados(parent):
    empleados = {u: d for u, d in usuarios.items() if d["rol"] == "empleado"}
    if not empleados:
        messagebox.showinfo("Empleados", "No hay empleados registrados.", parent=parent)
        return
    lista = "\n".join(empleados.keys())
    messagebox.showinfo("Empleados", lista, parent=parent)

def eliminar_administrador(parent):
    if usuario_actual["rol"] != "propietario":
        messagebox.showerror("Acceso denegado", "Solo el propietario puede eliminar administradores.", parent=parent)
        return
    admin = simpledialog.askstring("Eliminar administrador", "Nombre del administrador a eliminar:", parent=parent)
    if not admin or admin not in administradores:
        messagebox.showerror("Error", "Administrador no encontrado.", parent=parent)
        return
    if messagebox.askyesno("Confirmar", f"¿Eliminar administrador '{admin}'?", parent=parent):
        del administradores[admin]
        guardar_administradores()
        messagebox.showinfo("Éxito", f"Administrador '{admin}' eliminado.", parent=parent)

def eliminar_empleado(parent):
    if usuario_actual["rol"] not in ["propietario", "admin"]:
        messagebox.showerror("Acceso denegado", "Solo permitido para propietario o administradores.", parent=parent)
        return
    emp = simpledialog.askstring("Eliminar empleado", "Nombre del empleado a eliminar:", parent=parent)
    if not emp or emp not in usuarios or usuarios[emp]["rol"] != "empleado":
        messagebox.showerror("Error", "Empleado no encontrado.", parent=parent)
        return
    if messagebox.askyesno("Confirmar", f"¿Eliminar empleado '{emp}'?", parent=parent):
        del usuarios[emp]
        guardar_usuarios()
        messagebox.showinfo("Éxito", f"Empleado '{emp}' eliminado.", parent=parent)

def agregar_producto(parent):
    codigo = simpledialog.askstring("Agregar producto", "Código del producto:", parent=parent)
    if not codigo: return
    nombre = simpledialog.askstring("Agregar producto", "Nombre del producto:", parent=parent)
    if not nombre: return
    categoria = simpledialog.askstring(
        "Agregar producto",
        f"Categoría del producto (elige una):\n{', '.join(CATEGORIAS_VALIDAS)}",
        parent=parent
    )
    if not categoria: return
    categoria = categoria.lower()
    if categoria not in CATEGORIAS_VALIDAS:
        messagebox.showerror("Error", "Categoría inválida.", parent=parent)
        return
    try:
        stock = int(simpledialog.askstring("Agregar producto", "Stock inicial:", parent=parent))
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Stock inválido.", parent=parent)
        return
    try:
        precio = float(simpledialog.askstring("Agregar producto", "Precio del producto:", parent=parent))
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Precio inválido.", parent=parent)
        return
    producto = {"codigo": codigo, "nombre": nombre, "categoria": categoria, "stock": stock, "precio": precio}
    inventario.append(producto)
    guardar_inventario()
    messagebox.showinfo("Éxito", "Producto agregado.", parent=parent)

def buscar_producto(parent):
    criterio = simpledialog.askstring("Buscar producto", "Código o nombre:", parent=parent)
    if not criterio: return
    encontrados = [
        p for p in inventario
        if p["codigo"] == criterio or p["nombre"].lower() == criterio.lower()
    ]
    if encontrados:
        resultado = "\n".join(
            f"{p['codigo']} - {p['nombre']} - Stock: {p['stock']} - Precio: {p['precio']} - Categoría: {p['categoria']}"
            for p in encontrados
        )
        messagebox.showinfo("Encontrado", resultado, parent=parent)
    else:
        messagebox.showinfo("No encontrado", "Producto no encontrado.", parent=parent)

def actualizar_stock(parent):
    codigo = simpledialog.askstring("Actualizar stock", "Código del producto:", parent=parent)
    if not codigo: return
    for producto in inventario:
        if producto["codigo"] == codigo:
            try:
                nuevo_stock = int(simpledialog.askstring("Nuevo stock", f"Stock actual: {producto['stock']}", parent=parent))
                producto["stock"] = nuevo_stock
                guardar_inventario()
                messagebox.showinfo("Éxito", "Stock actualizado.", parent=parent)
                return
            except (ValueError, TypeError):
                messagebox.showerror("Error", "Stock inválido.", parent=parent)
                return
    messagebox.showinfo("No encontrado", "Producto no encontrado.", parent=parent)

def borrar_producto(parent):
    criterio = simpledialog.askstring("Eliminar producto", "Código o nombre:", parent=parent)
    if not criterio: return
    for producto in inventario:
        if producto["codigo"] == criterio or producto["nombre"].lower() == criterio.lower():
            if messagebox.askyesno("Confirmar", f"¿Eliminar '{producto['nombre']}'?", parent=parent):
                inventario.remove(producto)
                guardar_inventario()
                messagebox.showinfo("Éxito", "Producto eliminado.", parent=parent)
            return
    messagebox.showinfo("No encontrado", "Producto no encontrado.", parent=parent)

def mostrar_productos_por_categoria(parent):
    if not inventario:
        messagebox.showinfo("Inventario vacío", "No hay productos registrados.", parent=parent)
        return

    categorias = {cat: [] for cat in CATEGORIAS_VALIDAS}
    for producto in inventario:
        cat = producto.get("categoria", "").lower()
        if cat in categorias:
            categorias[cat].append(producto)

    ventana_categoria = tk.Toplevel(parent)  # Hacerla hija de la ventana principal
    ventana_categoria.title("Productos por Categoría")
    ventana_categoria.geometry("600x500")
    ventana_categoria.transient(parent)  # Aparecerá encima de la ventana principal
    ventana_categoria.grab_set()  # Hacerla modal

    texto = tk.Text(ventana_categoria, wrap="word", font=("Arial", 11))
    texto.pack(fill="both", expand=True, padx=10, pady=10)

    for cat in CATEGORIAS_VALIDAS:
        texto.insert("end", f"🗂 Categoría: {cat.capitalize()}\n", "titulo")
        if categorias[cat]:
            for p in categorias[cat]:
                texto.insert("end", f" - Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}\n")
        else:
            texto.insert("end", "   (No hay productos en esta categoría)\n")
        texto.insert("end", "\n")

    texto.tag_config("titulo", font=("Arial", 12, "bold"))
    texto.config(state="disabled")

def mostrar_ventana_principal(ventana_raiz):
    ventana_admin = tk.Toplevel(ventana_raiz)
    ventana_admin.title("🛒🔸Inventario de La Despensa Feliz🔸")
    ventana_admin.geometry("900x600")
    ventana_admin.configure(bg="#D8BFD8")  # Color lila claro para el fondo

    # Frame principal con fondo degradado
    main_frame = tk.Frame(ventana_admin, bg="#D8BFD8")
    main_frame.pack(fill="both", expand=True)

    # Frame lateral para botones (costado izquierdo)
    frame_lateral = tk.Frame(main_frame, bg="#9370DB", width=250, relief="raised", bd=2)
    frame_lateral.pack(side="left", fill="y", padx=(0, 10), pady=10)

    # Título del panel lateral
    tk.Label(frame_lateral, 
             text="Panel de Control", 
             font=("Arial", 16, "bold"), 
             bg="#6A5ACD", 
             fg="white",
             pady=10).pack(fill="x")

    rol = usuario_actual["rol"]

    # Contenedor para botones con scroll si es necesario
    canvas = tk.Canvas(frame_lateral, bg="#9370DB", highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame_lateral, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#9370DB")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Botones para propietario
    if rol == "propietario":
        tk.Button(scrollable_frame, 
                 text="👑 Crear Administrador", 
                 command=lambda: crear_administrador(ventana_admin),  # Pasamos ventana_admin como parent
                 bg="#9370DB",
                 fg="white",
                 font=("Arial", 11),
                 width=20,
                 pady=8).pack(fill="x", pady=5, padx=10)

        tk.Button(scrollable_frame, 
                 text="👥 Listar Administradores", 
                 command=lambda: listar_administradores(ventana_admin),  # Pasamos ventana_admin como parent
                 bg="#9370DB",
                 fg="white",
                 font=("Arial", 11),
                 width=20,
                 pady=8).pack(fill="x", pady=5, padx=10)

        tk.Button(scrollable_frame, 
                 text="🗑️ Eliminar Administrador", 
                 command=lambda: eliminar_administrador(ventana_admin),  # Pasamos ventana_admin como parent
                 bg="#9370DB",
                 fg="white",
                 font=("Arial", 11),
                 width=20,
                 pady=8).pack(fill="x", pady=5, padx=10)

    # Botones para admin y propietario
    if rol in ["propietario", "admin"]:
        tk.Button(scrollable_frame, 
                 text="👔 Crear Empleado", 
                 command=lambda: crear_empleado(ventana_admin),  # Pasamos ventana_admin como parent
                 bg="#9370DB",
                 fg="white",
                 font=("Arial", 11),
                 width=20,
                 pady=8).pack(fill="x", pady=5, padx=10)

        tk.Button(scrollable_frame, 
                 text="📋 Listar Empleados", 
                 command=lambda: listar_empleados(ventana_admin),  # Pasamos ventana_admin como parent
                 bg="#9370DB",
                 fg="white",
                 font=("Arial", 11),
                 width=20,
                 pady=8).pack(fill="x", pady=5, padx=10)

        tk.Button(scrollable_frame, 
                 text="❌ Eliminar Empleado", 
                 command=lambda: eliminar_empleado(ventana_admin),  # Pasamos ventana_admin como parent
                 bg="#9370DB",
                 fg="white",
                 font=("Arial", 11),
                 width=20,
                 pady=8).pack(fill="x", pady=5, padx=10)

    # Botones para gestión de productos
    tk.Button(scrollable_frame, 
             text="➕ Agregar Producto", 
             command=lambda: agregar_producto(ventana_admin),  # Pasamos ventana_admin como parent
             bg="#9370DB",
             fg="white",
             font=("Arial", 11),
             width=20,
             pady=8).pack(fill="x", pady=5, padx=10)

    tk.Button(scrollable_frame, 
             text="🔍 Buscar Producto", 
             command=lambda: buscar_producto(ventana_admin),  # Pasamos ventana_admin como parent
             bg="#9370DB",
             fg="white",
             font=("Arial", 11),
             width=20,
             pady=8).pack(fill="x", pady=5, padx=10)

    tk.Button(scrollable_frame, 
             text="🔄 Actualizar Stock", 
             command=lambda: actualizar_stock(ventana_admin),  # Pasamos ventana_admin como parent
             bg="#9370DB",
             fg="white",
             font=("Arial", 11),
             width=20,
             pady=8).pack(fill="x", pady=5, padx=10)

    tk.Button(scrollable_frame, 
             text="🗑️ Borrar Producto", 
             command=lambda: borrar_producto(ventana_admin),  # Pasamos ventana_admin como parent
             bg="#9370DB",
             fg="white",
             font=("Arial", 11),
             width=20,
             pady=8).pack(fill="x", pady=5, padx=10)

    tk.Button(scrollable_frame, 
             text="📂 Ver por Categoría", 
             command=lambda: mostrar_productos_por_categoria(ventana_admin),  # Pasamos ventana_admin como parent
             bg="#9370DB",
             fg="white",
             font=("Arial", 11),
             width=20,
             pady=8).pack(fill="x", pady=5, padx=10)

    # Botón para cerrar sesión
    tk.Button(scrollable_frame, 
             text="🚪 Cerrar Sesión", 
             command=ventana_admin.destroy,
             bg="#FF6B6B",
             fg="white",
             font=("Arial", 11, "bold"),
             width=20,
             pady=10).pack(fill="x", pady=15, padx=10)

    # Área principal derecha (espacio para contenido futuro)
    frame_principal = tk.Frame(main_frame, bg="#E6E6FA", relief="sunken", bd=1)
    frame_principal.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)

    # Mensaje de bienvenida en el área principal
    tk.Label(frame_principal, 
             text=f"Bienvenido(a), {usuario_actual['nombre']}",
             font=("Arial", 18, "bold"),
             bg="#E6E6FA",
             fg="#4B0082").pack(pady=20)

    tk.Label(frame_principal, 
             text="Sistema de Gestión de Inventario",
             font=("Arial", 14),
             bg="#E6E6FA",
             fg="#6A5ACD").pack(pady=5)

    tk.Label(frame_principal, 
             text="Seleccione una opción del menú lateral",
             font=("Arial", 12),
             bg="#E6E6FA",
             fg="#9370DB").pack(pady=20)

    # Logo o imagen decorativa
    try:
        # Intenta cargar una imagen si está disponible
        logo_img = Image.open("La Despensa.png")
        logo_img = logo_img.resize((800, 400), Image.LANCZOS)
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(frame_principal, image=logo_tk, bg="#E6E6FA")
        logo_label.image = logo_tk  # Mantener referencia
        logo_label.pack(pady=20)
    except:
        # Si no hay imagen, mostrar texto alternativo
        tk.Label(frame_principal, 
                 text="🛒 La Despensa Feliz",
                 font=("Arial", 24, "bold"),
                 bg="#E6E6FA",
                 fg="#4B0082").pack(pady=50)

    ventana_admin.wait_window()

def iniciar_sistema():
    global usuario_actual

    # Cargar datos
    cargar_usuarios()
    cargar_administradores()
    cargar_inventario()

    # Crear ventana raíz
    ventana_raiz = tk.Tk()
    ventana_raiz.withdraw()  # Ocultar la ventana raíz

    # Bucle principal
    while True:
        # Mostrar login
        login(ventana_raiz)

        # Si no hay usuario actual, salir
        if usuario_actual is None:
            break

        # Si es cliente, mostrar vista cliente
        if usuario_actual["rol"] == "cliente":
            mostrar_vista_cliente(ventana_raiz)
        else:
            # Mostrar ventana principal para administradores/propietario/empleados
            mostrar_ventana_principal(ventana_raiz)

        # Al cerrar la ventana de administrador o cliente, volvemos al login
        # Reiniciamos el usuario actual
        usuario_actual = None

    # Salir
    ventana_raiz.destroy()

# Iniciar el sistema
iniciar_sistema()