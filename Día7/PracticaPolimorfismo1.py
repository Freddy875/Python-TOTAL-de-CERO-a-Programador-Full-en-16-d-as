# ==================================================
# PRÁCTICA POLIMORFISMO 1
# Objetivo: comprobar el comportamiento polimórfico
# de la función len(), que calcula la longitud de un
# objeto según su tipo (string, lista o tupla).
# ==================================================

# --------------------------------------------------
# VARIABLES
# palabra: string con 12 caracteres.
# lista: lista con 3 elementos de tipo string.
# tupla: tupla con 4 elementos de tipo entero.
# --------------------------------------------------
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

# --------------------------------------------------
# ITERACIÓN Y LONGITUD DE CADA OBJETO
# El ciclo for recorre una lista formada por los tres
# objetos (palabra, lista, tupla). En cada vuelta,
# obj toma uno de ellos y len() devuelve su longitud,
# sin importar de qué tipo sea.
# Resultado esperado: imprime 12, 3 y 4.
# --------------------------------------------------
for objeto in [palabra, lista, tupla]:
    # Muestra la cantidad de caracteres o elementos del objeto actual
    print(len(objeto))