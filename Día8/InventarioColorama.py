# ==================================================
# Práctica: Librería Colorama - Inventario de tienda
# Objetivo: Crear un programa que le permita al dueño
# de una tienda revisar su inventario, vender y surtir
# productos, usando la librería Colorama para mostrar
# con colores el estado de cada producto:
# verde si hay suficiente, amarillo si queda poco y
# rojo si está agotado, para saber de un vistazo qué
# hay que volver a comprar.
# ==================================================


# --------------------------------------------------
# Importar la librería Colorama
# Colorama es una librería externa (se instala con
# pip install colorama) que permite cambiar el color
# del texto en la consola, también en Windows.
# Fore: cambia el color del texto (Fore.RED, Fore.GREEN).
# Back: cambia el color del fondo (Back.RED, Back.BLUE).
# Style: cambia el brillo (Style.BRIGHT) y RESET_ALL
# regresa todo a la normalidad.
# init(autoreset=True) activa los colores y hace que,
# al terminar cada print(), el color se reinicie solo,
# para no tener que escribir Style.RESET_ALL cada vez
# --------------------------------------------------
from colorama import init, Fore, Back, Style

init(autoreset=True)


# --------------------------------------------------
# Definir las constantes del programa
# Una constante no cambia su valor;
# por convención, su nombre se escribe en mayúsculas.
# STOCK_MINIMO: si un producto tiene menos piezas que
# este número, se considera que queda poco.
# --------------------------------------------------
STOCK_MINIMO = 5


# --------------------------------------------------
# Definir el inventario inicial
# Es un diccionario: cada clave es el nombre del
# producto (texto) y su valor es otro diccionario con
# el precio (decimal) y las piezas disponibles (entero)
# --------------------------------------------------
inventario = {
    "Leche": {"precio": 28.50, "piezas": 12},
    "Pan de caja": {"precio": 45.00, "piezas": 3},
    "Huevo (kg)": {"precio": 52.00, "piezas": 0},
    "Café": {"precio": 98.00, "piezas": 7},
    "Refresco": {"precio": 22.00, "piezas": 4},
}


# --------------------------------------------------
# Definir la función que da el estado de un producto
# Recibe las piezas y devuelve un texto ya coloreado:
# - Si hay 0 piezas: fondo rojo con "AGOTADO".
# - Si hay menos de STOCK_MINIMO: amarillo con "BAJO".
# - En otro caso: verde con "OK".
# Se suman los códigos de color al texto con +, por
# ejemplo: Fore.GREEN + "OK" se ve como OK en verde
# --------------------------------------------------
def estado_producto(piezas):
    """Devuelve el estado del producto con su color.

    Parámetros:
        piezas: piezas disponibles del producto (entero).

    Devuelve:
        El estado coloreado: AGOTADO, BAJO u OK (texto).
    """
    if piezas == 0:
        return Back.RED + Fore.WHITE + Style.BRIGHT + " AGOTADO " + Style.RESET_ALL
    elif piezas < STOCK_MINIMO:
        return Fore.YELLOW + Style.BRIGHT + "BAJO" + Style.RESET_ALL
    else:
        return Fore.GREEN + "OK" + Style.RESET_ALL


# --------------------------------------------------
# Definir la función para mostrar el inventario
# Imprime un encabezado en cian y después, con for,
# recorre el diccionario con items(), que entrega cada
# producto (clave) y sus datos (valor).
# Las f-strings con :<15 alinean el texto a la
# izquierda en 15 espacios, y :>8.2f alinea el número
# a la derecha con 2 decimales, para formar columnas.
# Por ejemplo, imprime:
# Producto        Precio  Piezas  Estado
# Leche           $28.50      12  OK
# Huevo (kg)      $52.00       0   AGOTADO
# --------------------------------------------------
def mostrar_inventario():
    """Muestra todos los productos con su estado en colores."""
    print(Fore.CYAN + Style.BRIGHT + "\n========== INVENTARIO ==========")
    print(Style.BRIGHT + f"{'Producto':<15} {'Precio':>8} {'Piezas':>7}  Estado")

    for producto, datos in inventario.items():
        print(f"{producto:<15} ${datos['precio']:>7.2f} {datos['piezas']:>7}  "
              f"{estado_producto(datos['piezas'])}")

    print(Fore.CYAN + "================================")


# --------------------------------------------------
# Definir la función para elegir un producto
# Muestra los productos numerados, empezando en 1,
# gracias a enumerate(..., start=1); el usuario
# escribe el número y se devuelve el nombre del
# producto. list() convierte las claves del diccionario
# en una lista para poder tomar un producto por su
# posición (se resta 1 porque las listas empiezan en 0).
# Si el número no es válido, imprime en rojo:
# Opción no válida
# y devuelve None, que significa "ningún producto"
# --------------------------------------------------
def elegir_producto():
    """Pide al usuario que elija un producto del inventario.

    Devuelve:
        El nombre del producto elegido (texto) o None si la
        opción no es válida.
    """
    productos = list(inventario.keys())

    for numero, producto in enumerate(productos, start=1):
        print(f"  {numero}. {producto}")

    opcion = input("Número del producto: ")

    if opcion.isdigit() and 1 <= int(opcion) <= len(productos):  # Verifica que sea un número de la lista
        return productos[int(opcion) - 1]

    print(Fore.RED + "Opción no válida")
    return None


# --------------------------------------------------
# Definir la función para vender
# Pide el producto y la cantidad; si hay piezas
# suficientes, las resta del inventario y muestra en
# verde el total de la venta. Si no alcanzan, muestra
# en rojo cuántas piezas hay. Por ejemplo, al vender 2
# leches, imprime:
# Venta realizada: 2 x Leche = $57.00
# Y si después quedan menos de STOCK_MINIMO piezas,
# avisa en amarillo que hay que surtir
# --------------------------------------------------
def vender():
    """Registra la venta de un producto."""
    producto = elegir_producto()
    if producto is None:
        return

    cantidad = int(input("Cantidad a vender: "))
    datos = inventario[producto]

    if cantidad <= datos["piezas"]:  # Verifica que haya piezas suficientes
        datos["piezas"] -= cantidad
        total = cantidad * datos["precio"]
        print(Fore.GREEN + Style.BRIGHT + f"Venta realizada: {cantidad} x {producto} = ${total:.2f}")

        if datos["piezas"] < STOCK_MINIMO:
            print(Fore.YELLOW + f"Aviso: quedan solo {datos['piezas']} piezas de {producto}, hay que surtir")
    else:
        print(Fore.RED + f"No hay suficiente {producto}: solo quedan {datos['piezas']} piezas")


# --------------------------------------------------
# Definir la función para surtir
# Pide el producto y la cantidad que llegó del
# proveedor, y la suma a las piezas del inventario.
# Por ejemplo, al surtir 10 huevos, imprime en verde:
# Se agregaron 10 piezas de Huevo (kg). Ahora hay 10
# --------------------------------------------------
def surtir():
    """Agrega piezas de un producto al inventario."""
    producto = elegir_producto()
    if producto is None:
        return

    cantidad = int(input("Cantidad que llegó: "))
    inventario[producto]["piezas"] += cantidad
    print(Fore.GREEN + f"Se agregaron {cantidad} piezas de {producto}. "
                       f"Ahora hay {inventario[producto]['piezas']}")


# --------------------------------------------------
# Definir la función que organiza el programa
# La variable opcion comienza vacía; while repite el
# menú hasta que el usuario elija "S" para salir.
# upper() convierte la opción a mayúscula para aceptar
# mayúsculas y minúsculas.
# Con "I" se muestra el inventario, con "V" se vende
# y con "A" se surte (abastece). Cualquier otra letra
# muestra en rojo: Opción no válida.
# try/except atrapa el error ValueError, que ocurre si
# el usuario escribe letras donde se esperaba un número
# --------------------------------------------------
def inicio():
    """Organiza la ejecución de todo el programa."""
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + " Bienvenido a Abarrotes Python ")
    mostrar_inventario()
    opcion = ""

    while opcion != "S":
        print(Fore.MAGENTA + "\nElija: Inventario (I), Vender (V), Surtir (A) o Salir (S)")
        opcion = input().upper()

        try:
            if opcion == "I":
                mostrar_inventario()
            elif opcion == "V":
                vender()
            elif opcion == "A":
                surtir()
            elif opcion != "S":
                print(Fore.RED + "Opción no válida")
        except ValueError:
            print(Fore.RED + "Error: la cantidad debe ser un número entero")

    print(Fore.CYAN + Style.BRIGHT + "Gracias por usar el sistema de inventario")


# --------------------------------------------------
# Iniciar el programa
# Se llama a la función inicio() para ejecutar todo.
# Si el usuario vende 2 de Leche (opción V, 1, 2) y
# sale, imprime:
# Venta realizada: 2 x Leche = $57.00   (en verde)
# Gracias por usar el sistema de inventario
# --------------------------------------------------
inicio()
