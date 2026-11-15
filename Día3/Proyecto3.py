# ------------------------------------------------------------
# Proyecto del Día 3
# Analizador de texto
#
# Ingresa un texto a elección y luego tres letras.
# El programa debe:
# - Contar cuántas veces aparece cada letra.
# - Contar la cantidad de palabras.
# - Mostrar la letra inicial y final.
# - Invertir el orden de las palabras.
# - Comprobar si la palabra "Python" aparece en el texto.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Ingresar el texto
# Se solicita al usuario un texto y se convierte a minúsculas
# para facilitar las búsquedas y comparaciones.
# ------------------------------------------------------------

texto = input("Ingresa un texto a elección: ")
texto = texto.lower()


# ------------------------------------------------------------
# Ingresar las tres letras
# Se crea una lista vacía y se agregan las tres letras
# ingresadas por el usuario.
# ------------------------------------------------------------

letras = []

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())


# ------------------------------------------------------------
# Contar la cantidad de veces que aparece cada letra
# El método count() cuenta cuántas veces aparece cada letra
# dentro del texto.
# ------------------------------------------------------------

print("\n")
print("CANTIDAD DE LETRAS")

print(f"Hemos encontrado {texto.count(letras[0])} veces la letra '{letras[0]}' en el texto")
print(f"Hemos encontrado {texto.count(letras[1])} veces la letra '{letras[1]}' en el texto")
print(f"Hemos encontrado {texto.count(letras[2])} veces la letra '{letras[2]}' en el texto")


# ------------------------------------------------------------
# Contar la cantidad de palabras
# split() separa el texto en una lista de palabras.
# len() permite conocer cuántos elementos tiene esa lista.
# ------------------------------------------------------------

print("\n")
print("CANTIDAD DE PALABRAS")

palabras = texto.split()

print(f"Hemos encontrado {len(palabras)} palabras en el texto")


# ------------------------------------------------------------
# Obtener la primera y la última letra
# El índice 0 obtiene el primer carácter.
# El índice -1 obtiene el último carácter del texto.
# ------------------------------------------------------------

print("\n")
print("LETRA INICIAL Y LETRA FINAL")

print(f"La letra inicial del texto es '{texto[0]}'")
print(f"La letra final del texto es '{texto[-1]}'")


# ------------------------------------------------------------
# Invertir el orden de las palabras
# reverse() modifica la lista y coloca las palabras en orden
# inverso.
# join() vuelve a unir las palabras formando nuevamente un texto.
# ------------------------------------------------------------

print("\n")
print("TEXTO INVERTIDO")

palabras.reverse()
texto_invertido = " ".join(palabras)

print(f"El texto invertido es: {texto_invertido}")


# ------------------------------------------------------------
# Buscar la palabra "Python"
# El operador in comprueba si "python" se encuentra dentro
# del texto y devuelve un valor booleano: True o False.
# ------------------------------------------------------------

print("\n")
print("BUSCAR LA PALABRA PYTHON")

if "python" in texto:
    print("La palabra Python sí se encuentra en el texto.")
else:
    print("La palabra Python no se encuentra en el texto.")

# ------------------------------------------------------------
# Guardar los resultados
# Se crea un archivo de texto para guardar los datos ingresados
# y los resultados obtenidos por el programa.
# El modo "a" permite agregar nuevos resultados sin borrar
# los anteriores.
# ------------------------------------------------------------

with open("resultados.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"Texto ingresado: {texto}\n")
    archivo.write(f"Primera letra: {letras[0]}\n")
    archivo.write(f"Segunda letra: {letras[1]}\n")
    archivo.write(f"Tercera letra: {letras[2]}\n")
    archivo.write(f"Cantidad de '{letras[0]}': {texto.count(letras[0])}\n")
    archivo.write(f"Cantidad de '{letras[1]}': {texto.count(letras[1])}\n")
    archivo.write(f"Cantidad de '{letras[2]}': {texto.count(letras[2])}\n")
    archivo.write(f"Cantidad de palabras: {len(palabras)}\n")
    archivo.write(f"Primera letra del texto: {texto[0]}\n")
    archivo.write(f"Última letra del texto: {texto[-1]}\n")
    archivo.write(f"Texto invertido: {texto_invertido}\n")
    archivo.write(f"Contiene Python: {'Sí' if 'python' in texto else 'No'}\n")
    archivo.write("-" * 50 + "\n")