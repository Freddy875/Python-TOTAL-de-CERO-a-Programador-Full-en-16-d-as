# ------------------------------------------------------------
# Práctica Min y Max 3
# Obtiene el valor mínimo de las edades de un diccionario
# y obtiene el último nombre en orden alfabético.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Diccionario de edades.
# Cada nombre funciona como clave y su edad como valor.
# ------------------------------------------------------------

diccionario_edades = {
    "Carlos": 55, "María": 42, "Mabel": 78, "José": 44,
    "Lucas": 24, "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49
}

# ------------------------------------------------------------
# Obtiene la edad mínima del diccionario.
# values() obtiene únicamente los valores del diccionario,
# y min() busca el valor más pequeño entre ellos.
# ------------------------------------------------------------

edad_minima = min(diccionario_edades.values())

# ------------------------------------------------------------
# Obtiene el último nombre en orden alfabético.
# keys() obtiene las claves del diccionario,
# y max() busca la clave que aparece al final
# según el orden alfabético.
# ------------------------------------------------------------

ultimo_nombre = max(diccionario_edades.keys())

# ------------------------------------------------------------
# Imprime la edad mínima y el último nombre
# en orden alfabético.
# ------------------------------------------------------------

print(f"Edad mínima: {edad_minima}")
print(f"Último nombre en orden alfabético: {ultimo_nombre}")