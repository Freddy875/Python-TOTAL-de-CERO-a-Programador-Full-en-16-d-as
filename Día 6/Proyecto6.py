# ==================================================
# Proyecto: Día 6 - Administrador de recetas
# Objetivo: Crear un programa de consola que permita
# al usuario leer, crear y eliminar recetas (archivos
# de texto) y categorías (carpetas) guardadas dentro
# de la carpeta "Recetas" de su directorio personal.
# El menú se repite dentro de un ciclo while hasta que
# el usuario elija la opción 6.
# ==================================================

# --------------------------------------------------
# Importar los módulos necesarios
# --------------------------------------------------
# Path permite trabajar con rutas, carpetas y archivos
from pathlib import Path

# system permite ejecutar comandos de la consola (limpiar la
# pantalla) y name indica el sistema operativo ("nt" = Windows)
from os import system, name

# --------------------------------------------------
# Definir la ruta base de las recetas
# --------------------------------------------------
# Path.home() es la carpeta personal del usuario; el operador /
# agrega la carpeta "Recetas" para formar la ruta absoluta
RUTA_RECETAS = Path.home() / "Recetas"


# --------------------------------------------------
# Función: limpiar_pantalla()
# --------------------------------------------------
def limpiar_pantalla():
    """Limpia la consola para que no se acumulen ejecuciones anteriores."""
    # "cls" es el comando de Windows y "clear" el de Linux y macOS
    system("cls" if name == "nt" else "clear")


# --------------------------------------------------
# Función: contar_recetas()
# --------------------------------------------------
def contar_recetas():
    """Devuelve la cantidad total de recetas (archivos .txt) que hay."""
    # rglob("*.txt") busca archivos .txt dentro de Recetas y de todas
    # sus subcarpetas; list() los reúne y len() los cuenta
    return len(list(RUTA_RECETAS.rglob("*.txt")))


# --------------------------------------------------
# Función: nombre_valido()
# --------------------------------------------------
def nombre_valido(nombre):
    """Comprueba que un nombre sirva para crear una carpeta o un archivo.

    Parámetros:
        nombre: texto escrito por el usuario.

    Devuelve:
        True si el nombre es válido, False si no.
    """
    # Un nombre es válido si no está vacío, no es "." ni ".." y no
    # contiene separadores de ruta (Path(nombre).name los descarta)
    return nombre != "" and nombre not in (".", "..") and nombre == Path(nombre).name


# --------------------------------------------------
# Función: confirmar()
# --------------------------------------------------
def confirmar(pregunta):
    """Pide una confirmación al usuario y devuelve True si responde "s"."""
    return input(f"{pregunta} (s/n): ").strip().lower() == "s"


# --------------------------------------------------
# Función: mostrar_bienvenida()
# --------------------------------------------------
def mostrar_bienvenida():
    """Muestra la bienvenida, la ruta de las recetas y el total de recetas."""
    print("=" * 50)
    print("   Bienvenido al Administrador de Recetas")
    print("=" * 50)
    print(f"Ruta de las recetas: {RUTA_RECETAS}")
    print(f"Total de recetas: {contar_recetas()}")
    print()


# --------------------------------------------------
# Función: mostrar_menu()
# --------------------------------------------------
def mostrar_menu():
    """Muestra las opciones disponibles del menú."""
    print("¿Qué deseas hacer?")
    print("  [1] Leer receta")
    print("  [2] Crear receta")
    print("  [3] Crear categoría")
    print("  [4] Eliminar receta")
    print("  [5] Eliminar categoría")
    print("  [6] Finalizar programa")
    print()


# --------------------------------------------------
# Función: elegir_categoria()
# --------------------------------------------------
def elegir_categoria():
    """Muestra las categorías y pide al usuario que elija una.

    Devuelve:
        El Path de la categoría elegida, o None si no existe.
    """
    # iterdir() recorre el contenido de Recetas; is_dir() deja solo
    # las carpetas y sorted() las ordena alfabéticamente
    categorias = sorted(c for c in RUTA_RECETAS.iterdir() if c.is_dir())

    # Si no hay ninguna categoría, no hay nada que elegir
    if not categorias:
        print("No hay categorías disponibles.")
        return None

    # Mostrar el nombre de cada categoría (name es el nombre de la carpeta)
    print("Categorías disponibles:")
    for categoria in categorias:
        print(f"  - {categoria.name}")

    nombre = input("\nEscribe el nombre de la categoría: ").strip()

    # Buscar la categoría comparando nombres sin distinguir mayúsculas
    for categoria in categorias:
        if categoria.name.lower() == nombre.lower():
            return categoria

    print(f"La categoría '{nombre}' no existe.")
    return None


# --------------------------------------------------
# Función: elegir_receta()
# --------------------------------------------------
def elegir_receta(categoria):
    """Muestra las recetas de una categoría y pide al usuario que elija una.

    Parámetros:
        categoria: Path de la carpeta de la categoría.

    Devuelve:
        El Path de la receta elegida, o None si no existe.
    """
    # glob("*.txt") busca los archivos .txt dentro de la categoría
    recetas = sorted(categoria.glob("*.txt"))

    # Si la categoría está vacía, no hay nada que elegir
    if not recetas:
        print(f"La categoría '{categoria.name}' no tiene recetas.")
        return None

    # Mostrar el nombre de cada receta sin la extensión (stem)
    print(f"\nRecetas en '{categoria.name}':")
    for receta in recetas:
        print(f"  - {receta.stem}")

    nombre = input("\nEscribe el nombre de la receta: ").strip()

    # Buscar la receta comparando nombres sin distinguir mayúsculas
    for receta in recetas:
        if receta.stem.lower() == nombre.lower():
            return receta

    print(f"La receta '{nombre}' no existe.")
    return None


# --------------------------------------------------
# Función: leer_receta()  (opción 1)
# --------------------------------------------------
def leer_receta():
    """Pide categoría y receta, y muestra el contenido de la receta."""
    categoria = elegir_categoria()
    if categoria is None:
        return

    receta = elegir_receta(categoria)
    if receta is None:
        return

    # read_text() abre el archivo, lee todo su contenido y lo cierra
    print(f"\n--- {receta.stem} ---")
    print(receta.read_text(encoding="utf-8"))


# --------------------------------------------------
# Función: crear_receta()  (opción 2)
# --------------------------------------------------
def crear_receta():
    """Pide categoría, nombre y contenido, y crea el archivo de la receta."""
    categoria = elegir_categoria()
    if categoria is None:
        return

    nombre = input("\nEscribe el nombre de la nueva receta: ").strip()
    if not nombre_valido(nombre):
        print("El nombre no es válido.")
        return

    # Armar la ruta del nuevo archivo dentro de la categoría
    receta = categoria / f"{nombre}.txt"

    # exists() evita sobrescribir una receta que ya existe
    if receta.exists():
        print(f"La receta '{nombre}' ya existe en esa categoría.")
        return

    contenido = input("Escribe el contenido de la receta: ")

    # write_text() crea el archivo y escribe el contenido
    receta.write_text(contenido, encoding="utf-8")
    print(f"\nReceta '{nombre}' creada correctamente.")


# --------------------------------------------------
# Función: crear_categoria()  (opción 3)
# --------------------------------------------------
def crear_categoria():
    """Pide un nombre y crea una carpeta nueva dentro de Recetas."""
    nombre = input("Escribe el nombre de la nueva categoría: ").strip()
    if not nombre_valido(nombre):
        print("El nombre no es válido.")
        return

    categoria = RUTA_RECETAS / nombre

    if categoria.exists():
        print(f"La categoría '{nombre}' ya existe.")
        return

    # mkdir() crea la carpeta
    categoria.mkdir()
    print(f"\nCategoría '{nombre}' creada correctamente.")


# --------------------------------------------------
# Función: eliminar_receta()  (opción 4)
# --------------------------------------------------
def eliminar_receta():
    """Pide categoría y receta, y elimina el archivo de la receta."""
    categoria = elegir_categoria()
    if categoria is None:
        return

    receta = elegir_receta(categoria)
    if receta is None:
        return

    # Pedir confirmación porque eliminar no se puede deshacer
    if not confirmar(f"\n¿Seguro que quieres eliminar '{receta.stem}'?"):
        print("Operación cancelada.")
        return

    # unlink() elimina el archivo
    receta.unlink()
    print(f"\nReceta '{receta.stem}' eliminada correctamente.")


# --------------------------------------------------
# Función: eliminar_categoria()  (opción 5)
# --------------------------------------------------
def eliminar_categoria():
    """Pide una categoría y elimina la carpeta con todas sus recetas."""
    categoria = elegir_categoria()
    if categoria is None:
        return

    # Pedir confirmación porque también se borran las recetas que contiene
    if not confirmar(f"\n¿Seguro que quieres eliminar '{categoria.name}' y todas sus recetas?"):
        print("Operación cancelada.")
        return

    try:
        # rmdir() solo elimina carpetas vacías, así que primero se
        # eliminan los archivos que contiene la categoría
        for archivo in categoria.iterdir():
            archivo.unlink()
        categoria.rmdir()
        print(f"\nCategoría '{categoria.name}' eliminada correctamente.")
    except OSError:
        print("No se pudo eliminar la categoría porque contiene otras carpetas.")


# --------------------------------------------------
# Función: volver_al_menu()
# --------------------------------------------------
def volver_al_menu():
    """Detiene el programa hasta que el usuario presione una letra y Enter."""
    input("\nPresiona una letra y Enter para volver al menú: ")


# --------------------------------------------------
# Función principal: main()
# --------------------------------------------------
def main():
    """Ejecuta el menú principal en un ciclo hasta que se elija la opción 6."""
    # Comprobar que la carpeta Recetas exista antes de empezar
    if not RUTA_RECETAS.is_dir():
        print(f"No se encontró la carpeta de recetas en: {RUTA_RECETAS}")
        print("Créala (con sus categorías y recetas) y vuelve a ejecutar el programa.")
        return

    opcion = ""

    # El ciclo se repite mientras la opción elegida no sea 6
    while opcion != "6":
        limpiar_pantalla()
        mostrar_bienvenida()
        mostrar_menu()

        opcion = input("Elige una opción (1-6): ").strip()
        limpiar_pantalla()

        # Ejecutar la función que corresponde a la opción elegida
        if opcion == "1":
            leer_receta()
        elif opcion == "2":
            crear_receta()
        elif opcion == "3":
            crear_categoria()
        elif opcion == "4":
            eliminar_receta()
        elif opcion == "5":
            eliminar_categoria()
        elif opcion == "6":
            print("¡Hasta pronto!")
        else:
            print("Opción no válida. Elige un número del 1 al 6.")

        # Después de cada acción se espera antes de limpiar la pantalla,
        # para que el usuario alcance a leer el resultado
        if opcion != "6":
            volver_al_menu()


# --------------------------------------------------
# Ejecutar el programa
# --------------------------------------------------
# Esta condición hace que main() solo se ejecute cuando se corre
# este archivo directamente, y no cuando se importa desde otro
if __name__ == "__main__":
    main()