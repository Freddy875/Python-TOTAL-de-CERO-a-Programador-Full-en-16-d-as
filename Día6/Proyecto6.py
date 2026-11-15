# ============================================================
# Proyecto del Día 6: Administrador de recetas
# Objetivo: Crear un programa que permita leer, crear y
# eliminar recetas, así como crear y eliminar categorías.
# Se utiliza una ruta relativa para acceder a la carpeta
# "Recetas", ubicada dentro de la carpeta del proyecto.
# ============================================================

import os
from pathlib import Path

# ------------------------------------------------------------
# Configurar la ruta relativa de la carpeta de recetas
# ------------------------------------------------------------
RUTA_BASE = Path("Recetas")

# ------------------------------------------------------------
# Mostrar la cantidad total de recetas disponibles
# ------------------------------------------------------------
def contar_recetas():
    recetas = list(RUTA_BASE.glob("*/*.txt"))
    return len(recetas)


# ------------------------------------------------------------
# Mostrar las categorías disponibles
# ------------------------------------------------------------
def mostrar_categorias():
    categorias = [carpeta for carpeta in RUTA_BASE.iterdir()
                  if carpeta.is_dir()]

    if not categorias:
        print("No hay categorías disponibles.")
        return []

    for categoria in categorias:
        print(f"- {categoria.name}")

    return categorias


# ------------------------------------------------------------
# Seleccionar una categoría existente
# ------------------------------------------------------------
def seleccionar_categoria():
    print("\nCategorías disponibles:")
    categorias = mostrar_categorias()

    if not categorias:
        return None

    nombre = input("\nEscribe el nombre de la categoría: ").strip()
    ruta_categoria = RUTA_BASE / nombre

    if ruta_categoria.is_dir():
        return ruta_categoria

    print("La categoría no existe.")
    return None


# ------------------------------------------------------------
# Mostrar las recetas de una categoría
# ------------------------------------------------------------
def mostrar_recetas(ruta_categoria):
    recetas = list(ruta_categoria.glob("*.txt"))

    if not recetas:
        print("Esta categoría no contiene recetas.")
        return []

    for receta in recetas:
        print(f"- {receta.stem}")

    return recetas


# ------------------------------------------------------------
# Leer una receta existente
# ------------------------------------------------------------
def leer_receta():
    categoria = seleccionar_categoria()

    if categoria is None:
        return

    recetas = mostrar_recetas(categoria)

    if not recetas:
        return

    nombre = input("\nEscribe el nombre de la receta: ").strip()
    ruta_receta = categoria / f"{nombre}.txt"

    if ruta_receta.is_file():
        with open(ruta_receta, "r", encoding="utf-8") as archivo:
            print("\nContenido de la receta:")
            print(archivo.read())
    else:
        print("La receta no existe.")


# ------------------------------------------------------------
# Crear una receta nueva dentro de una categoría
# ------------------------------------------------------------
def crear_receta():
    categoria = seleccionar_categoria()

    if categoria is None:
        return

    nombre = input("\nNombre de la nueva receta: ").strip()

    if not nombre or Path(nombre).name != nombre:
        print("El nombre de la receta no es válido.")
        return

    ruta_receta = categoria / f"{nombre}.txt"

    if ruta_receta.exists():
        print("Ya existe una receta con ese nombre.")
        return

    contenido = input("Escribe el contenido de la receta: ")

    with open(ruta_receta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print("Receta creada correctamente.")


# ------------------------------------------------------------
# Crear una categoría nueva
# ------------------------------------------------------------
def crear_categoria():
    nombre = input("\nNombre de la nueva categoría: ").strip()

    if not nombre or Path(nombre).name != nombre:
        print("El nombre de la categoría no es válido.")
        return

    ruta_categoria = RUTA_BASE / nombre

    if ruta_categoria.exists():
        print("La categoría ya existe.")
        return

    ruta_categoria.mkdir()
    print("Categoría creada correctamente.")


# ------------------------------------------------------------
# Eliminar una receta existente
# ------------------------------------------------------------
def eliminar_receta():
    categoria = seleccionar_categoria()

    if categoria is None:
        return

    recetas = mostrar_recetas(categoria)

    if not recetas:
        return

    nombre = input("\nEscribe el nombre de la receta que deseas eliminar: ").strip()
    ruta_receta = categoria / f"{nombre}.txt"

    if ruta_receta.is_file():
        confirmar = input("¿Seguro que deseas eliminarla? (s/n): ").lower()

        if confirmar == "s":
            ruta_receta.unlink()
            print("Receta eliminada correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("La receta no existe.")


# ------------------------------------------------------------
# Eliminar una categoría
# ------------------------------------------------------------
def eliminar_categoria():
    categoria = seleccionar_categoria()

    if categoria is None:
        return

    confirmar = input(
        f"¿Seguro que deseas eliminar la categoría '{categoria.name}' "
        "y todas sus recetas? (s/n): "
    ).lower()

    if confirmar == "s":
        try:
            for receta in categoria.glob("*.txt"):
                receta.unlink()

            categoria.rmdir()
            print("Categoría eliminada correctamente.")

        except OSError:
            print("No se pudo eliminar la categoría. Comprueba su contenido.")
    else:
        print("Operación cancelada.")

# --------------------------------------------------
# Mostrar el menú principal y gestionar las opciones
# --------------------------------------------------
def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("================================")
        print(" ADMINISTRADOR DE RECETAS")
        print("================================")
        print(f"Carpeta de recetas: {RUTA_BASE.resolve()}")
        print(f"Total de recetas: {contar_recetas()}")
        print("\n1. Leer una receta")
        print("2. Crear una receta")
        print("3. Crear una categoría")
        print("4. Eliminar una receta")
        print("5. Eliminar una categoría")
        print("6. Salir")

        # --------------------------------------------------
        # Solicitar al usuario que seleccione una opción
        # --------------------------------------------------
        opcion = input("\nSelecciona una opción: ").strip()

        # --------------------------------------------------
        # Ejecutar la opción seleccionada mediante match-case
        # --------------------------------------------------
        match opcion:
            case "1":
                leer_receta()
            case "2":
                crear_receta()
            case "3":
                crear_categoria()
            case "4":
                eliminar_receta()
            case "5":
                eliminar_categoria()
            case "6":
                print("¡Hasta pronto!")
                break
            case _:
                print("Opción no válida.")

        # --------------------------------------------------
        # Esperar antes de regresar al menú principal
        # --------------------------------------------------
        if opcion != "6":
            input("\nPresiona Enter para volver al menú...")
            
# ------------------------------------------------------------
# Iniciar el programa
# ------------------------------------------------------------
if __name__ == "__main__":
    if not RUTA_BASE.is_dir():
        print(f"No se encontró la carpeta: {RUTA_BASE.resolve()}")
        print("Crea la carpeta 'Recetas' dentro del directorio del proyecto.")
    else:
        menu()