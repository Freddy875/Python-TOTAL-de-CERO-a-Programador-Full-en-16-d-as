# ==================================================
# Práctica: Rutas anidadas con pathlib y Path.home()
# Objetivo: Utilizar Path.home() como base para crear
# una ruta anidada hacia el archivo "sagrada_familia.txt",
# ubicado dentro de las carpetas Europa, España y
# Barcelona, y después imprimirla.
# ==================================================

# --------------------------------------------------
# Importar la clase Path del módulo pathlib
# --------------------------------------------------
from pathlib import Path

# --------------------------------------------------
# Obtener la carpeta personal del usuario como base
# --------------------------------------------------
# Path.home() devuelve la ruta del directorio del usuario
# --------------------------------------------------

base = Path.home()

# --------------------------------------------------
# Crear la ruta anidada de la guía detallada
# --------------------------------------------------
# Se unen la base y cada carpeta, en orden, hasta llegar
# al archivo; Path usa el separador correcto según el
# sistema operativo (/ o \)
# --------------------------------------------------

guia_detalle = Path(base, "Europa", "España", "Barcelona", "sagrada_familia.txt")

# --------------------------------------------------
# Mostrar la ruta completa
# --------------------------------------------------
print(guia_detalle)  # Ejemplo: /home/fernando/Europa/España/Barcelona/sagrada_familia.txt