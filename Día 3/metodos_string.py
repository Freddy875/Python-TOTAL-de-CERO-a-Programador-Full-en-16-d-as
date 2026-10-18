# ------------------------------------------------------------
# String original
# Se declara una variable que contiene un texto y se muestra
# su contenido sin realizar ninguna modificación.
# ------------------------------------------------------------

texto = "Este es el texto de Fern"

resultado = texto

print(resultado)


# ------------------------------------------------------------
# Método upper()
# Convierte todos los caracteres del string a mayúsculas.
# ------------------------------------------------------------

resultado = texto.upper()

print(resultado)


# ------------------------------------------------------------
# Método upper() aplicado directamente al string
# El método puede utilizarse directamente sobre una cadena
# de texto sin necesidad de almacenarla previamente en una
# variable.
# ------------------------------------------------------------

texto = "Este es el texto de Fern".upper()

resultado = texto

print(resultado)


# ------------------------------------------------------------
# Método upper sin paréntesis
# Al escribir upper sin (), no se ejecuta el método. En su
# lugar, se obtiene la referencia al método.
# ------------------------------------------------------------

texto = "Este es el texto de Fern".upper

resultado = texto

print(resultado)


# ------------------------------------------------------------
# Método upper() con slicing
# Primero se extrae un fragmento del string mediante slicing
# y después se convierte ese fragmento a mayúsculas.
# ------------------------------------------------------------

texto = "Este es el texto de Fern"

resultado = texto[2:8].upper()

print(resultado)


# ------------------------------------------------------------
# Método lower()
# Convierte todos los caracteres del string a minúsculas.
# ------------------------------------------------------------

resultado = texto.lower()

print(resultado)


# ------------------------------------------------------------
# Método split()
# Divide el string utilizando los espacios como separadores
# y devuelve los elementos separados dentro de una lista.
# ------------------------------------------------------------

resultado = texto.split()

print(resultado)


# ------------------------------------------------------------
# Método split() con un separador específico
# En este caso, el string se divide cada vez que encuentra
# la letra "t".
# ------------------------------------------------------------

resultado = texto.split("t")

print(resultado)


# ------------------------------------------------------------
# Método join() con espacios
# Une varias palabras para formar un único string.
# El espacio " " funciona como separador entre las palabras.
# ------------------------------------------------------------

palabra1 = "Aprender"
palabra2 = "python"
palabra3 = "es"
palabra4 = "divertido"

unir = " ".join([palabra1, palabra2, palabra3, palabra4])

print(unir)


# ------------------------------------------------------------
# Método join() con guiones
# Une las palabras utilizando "-" como separador.
# ------------------------------------------------------------

unir = "-".join([palabra1, palabra2, palabra3, palabra4])

print(unir)


# ------------------------------------------------------------
# Método find()
# Busca la primera aparición de la letra "s" y devuelve
# el índice donde se encuentra.
# ------------------------------------------------------------

resultado = texto.find("s")

print(resultado)


# ------------------------------------------------------------
# Método find() cuando no encuentra el texto
# Busca la letra "g". Como no existe en el string, find()
# devuelve -1.
# ------------------------------------------------------------

resultado = texto.find("g")

print(resultado)


# ------------------------------------------------------------
# Método find() para buscar una palabra
# Busca la primera aparición de "text" y devuelve el índice
# donde comienza esa palabra.
# ------------------------------------------------------------

resultado = texto.find("text")

print(resultado)


# ------------------------------------------------------------
# Método replace()
# Busca el texto "Fern" y lo reemplaza por "Javier".
# El resultado se almacena en una nueva variable.
# ------------------------------------------------------------

resultado = texto.replace("Fern", "Javier")

print(resultado)