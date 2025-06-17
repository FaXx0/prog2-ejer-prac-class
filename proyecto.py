inventario = []

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    # Verificar si el código ya existe
    if any(p['codigo'] == codigo for p in inventario):
        print("❌ Error: El código ya existe. Use un código único.\n")
        return

    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            stock = int(input("Ingrese el stock inicial: "))
            if stock < 0:
                print("⚠ El stock no puede ser negativo\n")
                continue
            break
        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido\n")

    inventario.append({"codigo": codigo, "nombre": nombre, "stock": stock})
    print("✅ Producto agregado con éxito.\n")

def listar_productos():
    if not inventario:
        print("⚠ No hay productos en el inventario.\n")
        return

    print("\n📦 Lista de productos:")
    print("-" * 40)
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. Código: {producto['codigo']}")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Stock: {producto['stock']}")
    print("-" * 40 + "\n")

def buscar_producto():
    criterio = input("Buscar por código o nombre: ").strip().lower()
    if not criterio:
        print("❌ Ingrese un criterio de búsqueda\n")
        return

    encontrados = [
        p for p in inventario 
        if criterio in p['codigo'].lower() or criterio in p['nombre'].lower()
    ]

    if not encontrados:
        print("❌ Producto no encontrado.\n")
        return

    print("\n🔍 Resultados de búsqueda:")
    for p in encontrados:
        print(f"• Código: {p['codigo']} | Nombre: {p['nombre']} | Stock: {p['stock']}")
    print()

def actualizar_stock():
    codigo = input("Ingrese el código del producto: ")
    for producto in inventario:
        if producto["codigo"] == codigo:
            while True:
                try:
                    nuevo_stock = int(input(f"Stock actual ({producto['stock']}). Nuevo stock: "))
                    if nuevo_stock < 0:
                        print("⚠ El stock no puede ser negativo\n")
                        continue
                    producto["stock"] = nuevo_stock
                    print("🔁 Stock actualizado.\n")
                    return
                except ValueError:
                    print("❌ Error: Ingrese un número válido\n")
    print("❌ Producto no encontrado.\n")

# --- NUEVAS FUNCIONALIDADES ---

def borrar_producto():
    codigo = input("Ingrese el código del producto a borrar: ")
    for i, producto in enumerate(inventario):
        if producto["codigo"] == codigo:
            confirmacion = input(f"¿Borrar {producto['nombre']}? (s/n): ").lower()
            if confirmacion == 's':
                del inventario[i]
                print("🗑️ Producto borrado con éxito.\n")
            else:
                print("❌ Operación cancelada\n")
            return
    print("❌ Producto no encontrado.\n")

def devolver_producto():
    codigo = input("Ingrese el código del producto: ")
    for producto in inventario:
        if producto["codigo"] == codigo:
            while True:
                try:
                    cantidad = int(input("Cantidad a devolver: "))
                    if cantidad <= 0:
                        print("❌ La cantidad debe ser positiva\n")
                        continue
                    producto["stock"] += cantidad
                    print(f"📥 Devolución exitosa. Nuevo stock: {producto['stock']}\n")
                    return
                except ValueError:
                    print("❌ Error: Ingrese un número válido\n")
    print("❌ Producto no encontrado.\n")

# --- MENÚ MEJORADO ---

def menu():
    while True:
        print("\n" + "=" * 30)
        print("📋 SISTEMA DE INVENTARIO")
        print("=" * 30)
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar stock")
        print("5. Borrar producto")
        print("6. Devolver productos")
        print("7. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            borrar_producto()
        elif opcion == "6":
            devolver_producto()
        elif opcion == "7":
            print("\n👋 ¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\n❌ Opción inválida. Por favor intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu()