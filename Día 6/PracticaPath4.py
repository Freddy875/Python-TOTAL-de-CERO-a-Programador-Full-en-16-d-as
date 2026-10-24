# ==================================================
# Práctica: Comprobar si una ruta existe con pathlib
# Objetivo: Crear una ruta relativa hacia el archivo
# "leccion_path.py" y utilizar el método exists() para
# comprobar si esa ubicación existe en el disco.
# ==================================================

# --------------------------------------------------
# Importar la clase Path del módulo pathlib
# --------------------------------------------------
from pathlib import Path

# --------------------------------------------------
# Crear la ruta relativa al archivo
# --------------------------------------------------
# Se unen las carpetas y el archivo en orden; solo se crea un
# objeto Path en memoria, no se crea nada en el disco
ruta = Path("Python", "Día 6", "leccion_path.py")

# --------------------------------------------------
# Comprobar si la ruta existe
# --------------------------------------------------
# exists() devuelve un valor booleano: True si la ruta existe
# a partir de la carpeta donde se ejecuta el programa, False si no
print(ruta.exists())  # True si existe en tu disco, False si no