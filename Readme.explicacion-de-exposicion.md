### 📦 LIBRERÍAS IMPORTADAS
```python
import tkinter as tk
from tkinter import ttk, Label, Frame, Button, Toplevel
from PIL import Image, ImageTk
from propietario import crear_empleado, listar_empleados, eliminar_empleado
```

1. **`tkinter`**: Librería estándar de Python para crear interfaces gráficas (GUI).

   * Se importa como `tk` para acortar su uso en el código.
2. **`ttk`**: Subconjunto de `tkinter` que proporciona widgets con un diseño más moderno.
3. **`Label, Frame, Button, Toplevel`**: Clases específicas de `tkinter` para construir interfaces.
4. **`PIL.Image, PIL.ImageTk`**: Parte de la librería Pillow, usada para cargar y mostrar imágenes en interfaces.
5. **`from propietario import ...`**: Se importan funciones personalizadas para manejar empleados (crear, listar, eliminar). Estas deben estar definidas en otro archivo llamado `propietario.py`.

---

### 🧩 DEFINICIÓN DE LA FUNCIÓN PRINCIPAL

```python
def mostrar_ventana_administrador(ventana_raiz, inventario, usuarios, administradores):
```

* Se define una función que crea la **ventana de administrador**.
* Recibe 4 parámetros:

  * `ventana_raiz`: la ventana principal del sistema.
  * `inventario`: la lista o estructura con los productos.
  * `usuarios`: diccionario con información de los usuarios (clave-valor).
  * `administradores`: puede ser diccionario o lista con los datos de administradores.

---

### 🪟 CREACIÓN DE LA VENTANA

```python
    ventana_admin = tk.Toplevel(ventana_raiz)
```

* Crea una **ventana secundaria** encima de la principal.
* `Toplevel` permite mostrar nuevas ventanas independientes.

```python
    ventana_admin.title("🛒🔸Inventario de La Despensa Feliz🔸")
    ventana_admin.geometry("900x600")
    ventana_admin.configure(bg="#D8BFD8")
```

* Se establece el título, tamaño y color de fondo.

---

### 📐 MARCOS (FRAMES) DE ORGANIZACIÓN

```python
    main_frame = tk.Frame(ventana_admin, bg="#D8BFD8")
    main_frame.pack(fill="both", expand=True)
```

* Crea un marco general que ocupa toda la ventana.

```python
    frame_lateral = tk.Frame(main_frame, bg="#9370DB", width=250, relief="raised", bd=2)
    frame_lateral.pack(side="left", fill="y", padx=(0, 10), pady=10)
```

* Este frame lateral será el menú (panel de control).
* Alineado a la izquierda, con bordes elevados.

---

### 🔠 TÍTULO DEL PANEL LATERAL

```python
    tk.Label(frame_lateral, 
             text="Panel de Control", 
             font=("Arial", 16, "bold"), 
             bg="#6A5ACD", 
             fg="white",
             pady=10).pack(fill="x")
```

* Un título dentro del `frame_lateral`.

---

### 📜 SCROLL EN MENÚ LATERAL

```python
    canvas = tk.Canvas(frame_lateral, bg="#9370DB", highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame_lateral, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#9370DB")
```

* Se usa un `Canvas` para permitir **scroll vertical** en el menú.
* El `scrollable_frame` contendrá los botones.

```python
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
```

* Se vincula el tamaño del `scrollable_frame` al scroll del canvas.

---

### 🔘 BOTONES FUNCIONALES DEL ADMINISTRADOR

```python
    tk.Button(scrollable_frame, 
             text="👔 Crear Empleado", 
             command=lambda: crear_empleado(ventana_admin, usuarios),
             bg="#9370DB", fg="white", font=("Arial", 11), width=20, pady=8
             ).pack(fill="x", pady=5, padx=10)
```

* Llama a la función `crear_empleado()` que debe estar definida en `propietario.py`.

* De forma similar:

```python
    tk.Button(scrollable_frame, 
             text="📋 Listar Empleados", 
             command=lambda: listar_empleados(ventana_admin, usuarios),
             ...
             ).pack(...)
```

```python
    tk.Button(scrollable_frame, 
             text="❌ Eliminar Empleado", 
             command=lambda: eliminar_empleado(ventana_admin, usuarios),
             ...
             ).pack(...)
```

---

### 🔚 BOTÓN DE CERRAR SESIÓN

```python
    tk.Button(scrollable_frame, 
             text="🚪 Cerrar Sesión", 
             command=ventana_admin.destroy,
             ...
             ).pack(...)
```

* Al hacer clic, **se cierra solo la ventana del administrador**.

---

### 🪟 FRAME PRINCIPAL DERECHO (Vista general)

```python
    frame_principal = tk.Frame(main_frame, bg="#E6E6FA", relief="sunken", bd=1)
    frame_principal.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
```

* Este `frame_principal` es el espacio donde se muestra la bienvenida y logo.

```python
    tk.Label(frame_principal, 
             text=f"Bienvenido(a), Administrador", ...).pack(pady=20)
```

* Muestra un saludo y título informativo.

---

### 🖼️ MOSTRAR IMAGEN (logo)

```python
    try:
        logo_img = Image.open("La Despensa.png")
        logo_img = logo_img.resize((800, 400), Image.LANCZOS)
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(frame_principal, image=logo_tk, bg="#E6E6FA")
        logo_label.image = logo_tk
        logo_label.pack(pady=20)
```

* Intenta abrir y mostrar la imagen del logo. Si no está disponible:

```python
    except:
        tk.Label(frame_principal, 
                 text="🛒 La Despensa Feliz", ...).pack(pady=50)
```

* Se muestra un texto de reemplazo.

---

### ⏳ ESPERA DE LA VENTANA

```python
    ventana_admin.wait_window()
```

* Pausa la ejecución del programa **hasta que se cierre esta ventana**.

---

## 🧠 RESUMEN TÉCNICO

| Elemento                  | Uso                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Librerías**             | `tkinter`, `ttk`, `PIL.Image`, funciones externas                                   |
| **Funciones propias**     | `crear_empleado`, `listar_empleados`, `eliminar_empleado`                           |
| **Estructuras de datos**  | `usuarios`: diccionario. `inventario` y `administradores`: lista o diccionario      |
| **Algoritmos**            | No hay algoritmos de ordenamiento ni búsqueda aquí                                  |
| **Búsqueda/Ordenamiento** | No se aplica búsqueda binaria o lineal en este fragmento                            |
| **Bucle**                 | No hay bucles explícitos (`for`, `while`). Pero hay eventos y funciones de callback |
| **Diseño GUI**            | Uso de `Frame`, `Canvas`, `Scrollbar`, `Button`, `Label`, `Toplevel`                |
| **Scroll dinámico**       | Implementado con `Canvas` y `scrollable_frame`                                      |
| **Control de flujo**      | `try-except`, `lambda`, `wait_window`                                               |

---
Perfecto, vamos a hacer dos cosas:

---

## ✅ PARTE 1: **Explicación detallada de las funciones en `propietario.py`**

Te mostraré versiones estándar de esas funciones (`crear_empleado`, `listar_empleados`, `eliminar_empleado`) con una explicación **línea por línea**.

---

### 🔧 `crear_empleado()`

```python
def crear_empleado(ventana, usuarios):
    import tkinter.simpledialog as simpledialog

    nombre = simpledialog.askstring("Crear Empleado", "Ingrese el nombre del nuevo empleado:")
    if not nombre:
        return

    contraseña = simpledialog.askstring("Crear Empleado", "Ingrese una contraseña para el empleado:")
    if not contraseña:
        return

    usuarios[nombre] = {"contraseña": contraseña, "rol": "empleado"}

    tk.messagebox.showinfo("Empleado Creado", f"Empleado '{nombre}' fue creado exitosamente.")
```

**Explicación:**

* Se usa `simpledialog.askstring()` para solicitar datos.
* Si el usuario cancela, `askstring()` devuelve `None`, por eso se verifica con `if not ...`.
* Se crea una nueva entrada en el diccionario `usuarios`.
* Muestra un mensaje de confirmación con `messagebox`.

---

### 📋 `listar_empleados()`

```python
def listar_empleados(ventana, usuarios):
    empleados = [usuario for usuario in usuarios if usuarios[usuario]["rol"] == "empleado"]

    if not empleados:
        tk.messagebox.showinfo("Lista Vacía", "No hay empleados registrados.")
        return

    lista = "\n".join(empleados)
    tk.messagebox.showinfo("Lista de Empleados", lista)
```

**Explicación:**

* Usa una **comprensión de lista** para buscar empleados (`rol == "empleado"`).
* Si no hay empleados, muestra un mensaje.
* Si los hay, se unen en un string con saltos de línea y se muestran.

---

### ❌ `eliminar_empleado()`

```python
def eliminar_empleado(ventana, usuarios):
    import tkinter.simpledialog as simpledialog

    nombre = simpledialog.askstring("Eliminar Empleado", "Ingrese el nombre del empleado a eliminar:")

    if nombre in usuarios and usuarios[nombre]["rol"] == "empleado":
        del usuarios[nombre]
        tk.messagebox.showinfo("Eliminado", f"Empleado '{nombre}' eliminado exitosamente.")
    else:
        tk.messagebox.showerror("Error", "Empleado no encontrado o no válido.")
```

**Explicación:**

* Pide el nombre a eliminar.
* Verifica que exista y que su rol sea `"empleado"`.
* Si se encuentra, se elimina del diccionario con `del`.
* Si no, muestra un mensaje de error.

---

## 🧑‍🏫 PARTE 2: **Guía visual para exponer en clase**

Aquí tienes una estructura tipo presentación (diapositivas):

---

### 📘 Diapositiva 1: Introducción

* **Tema:** Ventana del Administrador en Sistema de Inventario
* **Herramientas:** Tkinter, PIL, funciones propias
* **Objetivo:** Crear, listar y eliminar empleados desde un menú lateral

---

### 🪟 Diapositiva 2: Estructura General de la Ventana

```
+------------------------+----------------------------+
|  Panel Lateral         |  Panel Principal           |
|  (Botones con Scroll)  |  Bienvenida + Logo        |
+------------------------+----------------------------+
```

* **`Frame`** para dividir la ventana
* **`Canvas + Scrollbar`** en menú
* **Imagen** o texto si no hay logo

---

### 🧩 Diapositiva 3: Función `crear_empleado()`

* Solicita **nombre** y **contraseña**
* Agrega al diccionario `usuarios`
* Ventana emergente con `messagebox`

---

### 📋 Diapositiva 4: Función `listar_empleados()`

* Recorre el diccionario `usuarios`
* Filtra solo los que tengan `"rol": "empleado"`
* Muestra todos en un `messagebox`

---

### 🗑️ Diapositiva 5: Función `eliminar_empleado()`

* Pide el nombre
* Verifica existencia y rol
* Usa `del` para eliminar
* Muestra éxito o error

---

### 🔍 Diapositiva 6: Análisis técnico

| Elemento                                                              | Detalle                               |
| --------------------------------------------------------------------- | ------------------------------------- |
| Estructura de datos                                                   | Diccionario (`usuarios`)              |
| Algoritmos                                                            | Búsqueda lineal (`for` en `listar`)   |
| Gráficos                                                              | `tkinter`, `Canvas`, `Frame`, `Label` |
| Lógica                                                                | `if`, `lambda`, `try-except`          |
| No hay bucles explícitos (`for`, `while`) pero sí búsquedas y eventos |                                       |

---

¿Quieres que prepare esta guía como presentación PowerPoint (`.pptx`) o como PDF para que la puedas usar directamente en clase? ¿Te gustaría que incluya capturas del sistema o ejemplos con colores y botones?

