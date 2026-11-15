# ==================================================
# Práctica: Path 3
# Objetivo: Crear una ruta absoluta que permita llegar
# al archivo "practicas_path.py" a partir de la carpeta
# base del usuario, concatenando las carpetas "Curso Python"
# y "Día 6", almacenarla en la variable ruta e imprimirla.
# ==================================================

# --------------------------------------------------
# Importar la clase Path del módulo pathlib
# --------------------------------------------------
from pathlib import Path

# --------------------------------------------------
# Obtener la carpeta base del usuario
# Obtener el directorio base del usuario (home)
# Path.home() devuelve un objeto Path con la carpeta personal
# del usuario actual (por ejemplo, C:\Users\Fernando o /home/fernando)
# --------------------------------------------------

ruta_base = Path.home()

# --------------------------------------------------
# Crear la ruta absoluta al archivo
# --------------------------------------------------
# Crear la ruta absoluta al archivo "practicas_path.py"
# El operador / concatena objetos Path con textos, uniendo cada
# parte con el separador correcto según el sistema operativo;
# como la ruta parte de ruta_base, es absoluta y no depende de
# la carpeta donde se ejecute el programa
ruta = ruta_base / "Curso Python" / "Día 6" / "practicas_path.py"

# --------------------------------------------------
# Imprimir la ruta absoluta
# --------------------------------------------------

print(ruta)  # Ejemplo: /home/fernando/Curso Python/Día 6/practicas_path.py