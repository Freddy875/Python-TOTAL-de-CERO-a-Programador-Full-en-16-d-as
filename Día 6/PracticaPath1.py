# ==================================================
# Práctica: Path 1
# Objetivo: Almacenar en la variable ruta_base un objeto
# Path que señale el directorio base del usuario,
# utilizando el método home() de la clase Path, y
# después imprimirlo.
# ==================================================

# --------------------------------------------------
# Importar la clase Path del módulo pathlib
# --------------------------------------------------
from pathlib import Path

# --------------------------------------------------
# Crear la variable con el directorio base del usuario
# --------------------------------------------------
# Obtener el directorio base del usuario
# Path.home() devuelve un objeto Path con la carpeta personal
# del usuario actual (por ejemplo, C:\Users\Fernando o /home/fernando)
ruta_base = Path.home()

# --------------------------------------------------
# Mostrar la ruta base
# --------------------------------------------------
# Imprimir la ruta base
print(ruta_base)  # Ejemplo: /home/fernando