Claro, aquí tienes una **explicación breve y clara paso a paso** como si estuvieras **exponiendo en clase** esta parte del código `mostrar_ventana_administrador`, que crea la interfaz del **Administrador** usando `Tkinter`:

---

## 🎤 **Exposición: Ventana del Administrador**

### 1. **Importaciones necesarias**

```python
import tkinter as tk
from tkinter import ttk, Label, Frame, Button, Toplevel
from PIL import Image, ImageTk
from propietario import crear_empleado, listar_empleados, eliminar_empleado
```

* Importamos módulos de **Tkinter** para crear interfaces gráficas.
* También usamos `PIL` para mostrar una imagen.
* Finalmente importamos tres funciones desde el archivo `propietario.py`.

---

### 2. **Definición de la función principal**

```python
def mostrar_ventana_administrador(ventana_raiz, inventario, usuarios, administradores):
```

* Esta función crea y muestra la ventana exclusiva para el **rol de administrador**.
* Recibe como parámetros la **ventana raíz**, el **inventario**, los **usuarios** y los **administradores**.

---

### 3. **Creación de la ventana Toplevel**

```python
ventana_admin = tk.Toplevel(ventana_raiz)
ventana_admin.title(...)
ventana_admin.geometry(...)
ventana_admin.configure(bg=...)
```

* Creamos una **ventana secundaria (Toplevel)** para el administrador.
* Le damos título, tamaño y color de fondo lila claro.

---

### 4. **Marco principal y lateral**

```python
main_frame = tk.Frame(ventana_admin, ...)
frame_lateral = tk.Frame(main_frame, ...)
```

* `main_frame`: contiene todo el contenido de la ventana.
* `frame_lateral`: sirve como **menú lateral de navegación**.

---

### 5. **Título del panel y Scrollbar**

```python
tk.Label(frame_lateral, ...)
canvas = tk.Canvas(frame_lateral)
scrollbar = ttk.Scrollbar(...)
scrollable_frame = tk.Frame(canvas, ...)
```

* Se muestra un **título visual** en el menú.
* Usamos un `Canvas` con `Scrollbar` para hacer **scroll** en el panel si hay muchos botones.

---

### 6. **Botones del panel lateral**

```python
tk.Button(scrollable_frame, text="👔 Crear Empleado", command=...)
tk.Button(scrollable_frame, text="📋 Listar Empleados", command=...)
tk.Button(scrollable_frame, text="❌ Eliminar Empleado", command=...)
```

* Cada botón llama a funciones para:

  * Crear un nuevo empleado.
  * Ver la lista de empleados.
  * Eliminar un empleado existente.

---

### 7. **Botón para cerrar sesión**

```python
tk.Button(scrollable_frame, text="🚪 Cerrar Sesión", command=ventana_admin.destroy, ...)
```

* Este botón **cierra la ventana** del administrador y vuelve a la principal.

---

### 8. **Panel principal del contenido**

```python
frame_principal = tk.Frame(main_frame, ...)
tk.Label(frame_principal, text="Bienvenido(a)...")
```

* Aquí se muestra un **mensaje de bienvenida** y guía al usuario.
* Este panel es el espacio central de trabajo para el administrador.

---

### 9. **Mostrar el logo (si existe)**

```python
try:
    logo_img = Image.open(...)
    ...
except:
    tk.Label(..., text="🛒 La Despensa Feliz")
```

* Si existe la imagen `"La Despensa.png"`, se muestra como logo.
* Si no existe, se muestra un texto con el nombre del negocio.

---

### 10. **Espera hasta que se cierre la ventana**

```python
ventana_admin.wait_window()
```

* El sistema **espera** hasta que el usuario cierre esta ventana antes de continuar.

---

## ✅ **Resumen Final**

* Esta interfaz permite al **Administrador** manejar empleados.
* Tiene diseño con **menú lateral**, **logo** y **botones funcionales**.
* Usa buenas prácticas como `Scrollbar`, `Toplevel` y `PIL`.

¿Quieres ahora una versión en PowerPoint o PDF para presentar esto?
