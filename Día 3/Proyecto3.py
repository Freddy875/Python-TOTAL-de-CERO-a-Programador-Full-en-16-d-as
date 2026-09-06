# ------------------------------------------------------------
# Proyecto del Día 3
# Analizador de texto
# El programa solicita un texto y tres letras para realizar
# diferentes análisis sobre la información proporcionada.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Solicitar el texto
# Se pide al usuario que ingrese el texto que desea analizar.
# ------------------------------------------------------------

texto = input("Ingresa el texto que deseas analizar: ")


# ------------------------------------------------------------
# Crear una lista para almacenar las letras
# La lista permitirá guardar las tres letras que el usuario
# desea buscar dentro del texto.
# ------------------------------------------------------------

letras = []


# ------------------------------------------------------------
# Solicitar las tres letras
# Cada letra ingresada se convierte a minúscula y se agrega
# a la lista utilizando el método append().
# ------------------------------------------------------------

letras.append(input("Ingresa la primera letra: ").lower())

letras.append(input("Ingresa la segunda letra: ").lower())

letras.append(input("Ingresa la tercera letra: ").lower())


# ------------------------------------------------------------
# Convertir el texto a minúsculas
# Se convierte el texto para que la búsqueda no distinga
# entre mayúsculas y minúsculas.
# ------------------------------------------------------------

texto = texto.lower()


# ------------------------------------------------------------
# Contar las letras
# El método count() cuenta directamente cuántas veces aparece
# cada letra de la lista dentro del texto.
# ------------------------------------------------------------

print(f"La letra '{letras[0]}' aparece {texto.count(letras[0])} veces.")

print(f"La letra '{letras[1]}' aparece {texto.count(letras[1])} veces.")

print(f"La letra '{letras[2]}' aparece {texto.count(letras[2])} veces.")


# ------------------------------------------------------------
# Contar las palabras
# El método split() convierte el texto en una lista de palabras.
# La función len() permite conocer cuántas palabras contiene.
# ------------------------------------------------------------

palabras = texto.split()

print(f"El texto contiene {len(palabras)} palabras.")


# ------------------------------------------------------------
# Primera y última letra
# Se utiliza indexación para obtener el primer y último
# carácter del texto.
# ------------------------------------------------------------

print(f"La primera letra del texto es: {texto[0]}")

print(f"La última letra del texto es: {texto[-1]}")


# ------------------------------------------------------------
# Invertir el orden de las palabras
# reverse() invierte el orden de la lista de palabras y
# join() vuelve a unirlas formando un string.
# ------------------------------------------------------------

palabras.reverse()

texto_invertido = " ".join(palabras)

print(f"El texto con las palabras invertidas es: {texto_invertido}")


# ------------------------------------------------------------
# Buscar la palabra "Python"
# El operador in comprueba si la palabra "python" se encuentra
# dentro del texto y devuelve un valor booleano.
# ------------------------------------------------------------

contiene_python = "python" in texto


# ------------------------------------------------------------
# Mostrar si se encuentra "Python"
# Se utiliza un diccionario para relacionar el resultado
# booleano con un mensaje para el usuario.
# ------------------------------------------------------------

mensajes = {
    True: "La palabra Python sí se encuentra en el texto.",
    False: "La palabra Python no se encuentra en el texto."
}

print(mensajes[contiene_python])