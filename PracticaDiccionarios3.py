# ------------------------------------------------------------
# Actualizar valores de un diccionario
# Se reasignan nuevos valores a las claves "edad" y
# "ocupacion" sin modificar la línea original del diccionario.
# ------------------------------------------------------------

mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

mi_dic["edad"] = 36

mi_dic["ocupacion"] = "Editora"


# ------------------------------------------------------------
# Agregar una nueva clave al diccionario
# Se crea la clave "pais" y se le asigna el valor "Colombia".
# ------------------------------------------------------------

mi_dic["pais"] = "Colombia"


# ------------------------------------------------------------
# Mostrar el diccionario actualizado
# Se imprimen los valores actualizados y la nueva clave.
# ------------------------------------------------------------

print(mi_dic)