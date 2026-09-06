# ------------------------------------------------------------
# Proyecto del Día 3
# Analizador de texto
# El programa recibe un texto y tres letras para realizar
# diferentes análisis sobre la información proporcionada.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Solicitar el texto
# Se pide al usuario que ingrese el texto que desea analizar.
# ------------------------------------------------------------

texto = input("Ingresa el texto que deseas analizar: ")


# ------------------------------------------------------------
# Solicitar las tres letras
# Se pide al usuario que ingrese tres letras para buscarlas
# dentro del texto.
# ------------------------------------------------------------

letra1 = input("Ingresa la primera letra: ")
letra2 = input("Ingresa la segunda letra: ")
letra3 = input("Ingresa la tercera letra: ")


# ------------------------------------------------------------
# Preparar el texto y las letras
# Se convierten el texto y las letras a minúsculas para que
# la búsqueda no distinga entre mayúsculas y minúsculas.
# ------------------------------------------------------------

texto = texto.lower()

letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()


# ------------------------------------------------------------
# Contar las letras
# El método count() cuenta cuántas veces aparece cada letra
# dentro del texto.
# ------------------------------------------------------------

print(f"La letra '{letra1}' aparece {texto.count(letra1)} veces.")

print(f"La letra '{letra2}' aparece {texto.count(letra2)} veces.")

print(f"La letra '{letra3}' aparece {texto.count(letra3)} veces.")


# ------------------------------------------------------------
# Contar las palabras
# El método split() convierte el texto en una lista de palabras.
# La función len() permite conocer cuántos elementos contiene
# esa lista.
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
# Se utiliza reverse() para invertir la lista de palabras
# y join() para volver a unirlas formando un string.
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