# ==================================================
# Práctica: Archivos y Funciones 1
# Objetivo: Crear una función llamada abrir_leer() que
# abra (open) un archivo indicado como parámetro y
# devuelva su contenido (read), y probarla con un
# archivo de texto ubicado junto a este script.
# ==================================================

# --------------------------------------------------
# Importar la clase Path del módulo pathlib
# --------------------------------------------------
from pathlib import Path

# --------------------------------------------------
# Definir la función abrir_leer()
# --------------------------------------------------
def abrir_leer(nombre_archivo):
    """Abre un archivo y devuelve su contenido.

    Parámetros:
        nombre_archivo: ruta del archivo a abrir (texto o Path).

    Devuelve:
        Un string con todo el contenido del archivo.
    """
    # Abrir el archivo en modo lectura ("r"); with lo cierra
    # automáticamente al terminar el bloque
    with open(nombre_archivo, "r") as archivo:
        return archivo.read()  # Leer y devolver el contenido del archivo

# --------------------------------------------------
# Preparar el archivo de prueba
# __file__ es la ruta de este script y parent su carpeta; así el
# archivo se busca siempre junto al script, sin importar desde
# qué carpeta se ejecute el programa
# --------------------------------------------------

ruta_archivo = Path(__file__).parent / "ejemplo.txt"

# Crear el archivo con un texto de ejemplo (si ya existe, se reemplaza su contenido)
ruta_archivo.write_text("Hola, este es el contenido de ejemplo.txt")

# --------------------------------------------------
# Ejemplo de uso de la función
# --------------------------------------------------
# Ejemplo de uso:
contenido = abrir_leer(ruta_archivo)
print(contenido)  # Imprime el contenido del archivo