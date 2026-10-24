# ==================================================
# Práctica: Path 2
# Objetivo: Crear una ruta relativa que permita llegar
# al archivo "practicas_path.py" a partir de la
# estructura de carpetas "Curso Python" y "Día 6",
# almacenarla en la variable ruta e imprimirla.
# ==================================================

# --------------------------------------------------
# Importar la clase Path del módulo pathlib
# --------------------------------------------------
from pathlib import Path

# --------------------------------------------------
# Crear la ruta relativa al archivo
# Crear la ruta relativa al archivo "practicas_path.py"
# Se unen las carpetas y el archivo en orden; como no empieza
# desde la raíz ni desde Path.home(), la ruta es relativa y se
# interpreta a partir de la carpeta donde se ejecuta el programa
# --------------------------------------------------
ruta = Path("Curso Python", "Día 6", "practicas_path.py")

# --------------------------------------------------
# Mostrar la ruta relativa
# Imprimir la ruta relativa
# --------------------------------------------------

print(ruta)  # Curso Python/Día 6/practicas_path.py (en Windows: Curso Python\Día 6\practicas_path.py)