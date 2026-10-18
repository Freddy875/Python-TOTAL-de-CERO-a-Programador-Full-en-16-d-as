# ------------------------------------------------------------
# Inmutabilidad de los strings
# Los strings no pueden modificarse directamente mediante
# sus índices. La siguiente línea produciría un error porque
# intenta cambiar el primer carácter del string.
# ------------------------------------------------------------

nombre = "Carina"

# nombre[0] = "K"


# ------------------------------------------------------------
# Reemplazar un string
# Los strings son inmutables, por lo que para cambiar su
# contenido se debe crear un nuevo string y asignarlo a la
# variable.
# ------------------------------------------------------------

nombre = "K" + nombre[1:]

print(nombre)


# ------------------------------------------------------------
# Concatenación de strings
# El operador + permite unir varios strings para formar
# una sola cadena de texto.
# ------------------------------------------------------------

nombre1 = "Xochitl"
nombre2 = "Quetzaly"
nombre3 = "Quetzalma"

print(nombre1 + " " + nombre2 + " " + nombre3)


# ------------------------------------------------------------
# Multiplicación de strings
# El operador * permite repetir un string la cantidad de
# veces indicada.
# ------------------------------------------------------------

print(nombre2 * 3)


# ------------------------------------------------------------
# Strings multilínea
# El carácter \n permite insertar un salto de línea dentro
# de un string.
# ------------------------------------------------------------

poema = "Bajo la luna canta el río\nentre las flores duerme el viento\nmientras la noche guarda su silencio"

print(poema)


# ------------------------------------------------------------
# Strings multilínea con triple comilla
# Las triples comillas permiten escribir un string en varias
# líneas directamente, conservando los saltos de línea.
# ------------------------------------------------------------

poema2 = """Los amorosos buscan la noche 
y guardan sueños entre sus manos 
mientras el silencio los acompaña"""

print(poema2)


# ------------------------------------------------------------
# Consultar el contenido de un string
# El operador in permite comprobar si un texto se encuentra
# dentro de otro string. El resultado es un valor booleano:
# True si lo encuentra y False si no lo encuentra.
# La negación not in comprueba que el texto no se encuentre
# dentro del string.
# ------------------------------------------------------------

print("río" in poema)

print("sol" in poema)

print("sol" not in poema)

# ------------------------------------------------------------
# Longitud de un string
# La función len() permite conocer la cantidad de caracteres
# que contiene un string.
# ------------------------------------------------------------

print(len(poema))