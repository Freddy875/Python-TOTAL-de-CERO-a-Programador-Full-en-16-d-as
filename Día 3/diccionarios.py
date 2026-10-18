# ------------------------------------------------------------
# Tipo de dato diccionario
# Un diccionario almacena información en pares de clave y valor.
# type() permite comprobar el tipo de dato de la variable.
# ------------------------------------------------------------

diccionario = {"clave1": "valor1", "clave2": "valor2"}

print(type(diccionario))

print(diccionario)


# ------------------------------------------------------------
# Valores repetidos y claves únicas
# Los valores de un diccionario pueden repetirse, pero cada
# clave debe ser única.
# ------------------------------------------------------------

diccionario = {"clave1": "valor1", "clave2": "valor1"}

print(diccionario)


# ------------------------------------------------------------
# Acceder a un valor mediante su clave
# Se utiliza la clave entre corchetes para obtener el valor
# que tiene asociado dentro del diccionario.
# ------------------------------------------------------------

diccionario = {"clave1": "valor1", "clave2": "valor2"}

resultado = diccionario["clave2"]

print(resultado)


# ------------------------------------------------------------
# Diccionario con diferentes tipos de datos
# Un diccionario puede contener strings, números enteros
# y números decimales como valores.
# ------------------------------------------------------------

cliente = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": "22 años",
    "peso": 70,
    "altura": 1.76
}

print(cliente)

# ------------------------------------------------------------
# Acceder a un valor específico del diccionario
# Se utiliza la clave "apellido" para obtener y mostrar
# únicamente el valor asociado a esa clave.
# ------------------------------------------------------------

print(cliente["apellido"])


# ------------------------------------------------------------
# Diccionarios con listas y otros diccionarios
# Los valores de un diccionario también pueden ser listas
# o incluso otros diccionarios.
# ------------------------------------------------------------

dic = {
    "c1": 55,
    "c2": [10, 20, 30],
    "c3": {"s1": 100, "s2": 200}
}

print(dic)


# ------------------------------------------------------------
# Acceder a una lista dentro de un diccionario
# La clave "c2" permite obtener la lista asociada a ella.
# ------------------------------------------------------------

print(dic["c2"])


# ------------------------------------------------------------
# Acceder a un elemento de una lista dentro de un diccionario
# Primero se accede a la lista mediante su clave y después
# se utiliza un índice para obtener uno de sus elementos.
# ------------------------------------------------------------

print(dic["c2"][1])


# ------------------------------------------------------------
# Acceder a un valor de un diccionario anidado
# Primero se accede al diccionario asociado a "c3" y después
# se utiliza la clave "s2" para obtener su valor.
# ------------------------------------------------------------

print(dic["c3"]["s2"])


# ------------------------------------------------------------
# Acceder a un elemento de una lista dentro del diccionario
# La clave permite acceder a la lista y el índice permite
# obtener un elemento específico.
# ------------------------------------------------------------

dic = {
    "clave1": ["a", "b", "c"],
    "clave2": ["d", "e", "f"]
}

print(dic["clave2"][0])


# ------------------------------------------------------------
# Tratar un elemento como string
# Se accede a un elemento de la lista y se utiliza upper()
# para convertir ese string a mayúsculas.
# ------------------------------------------------------------

print(dic["clave2"][1].upper())


# ------------------------------------------------------------
# Agregar un nuevo elemento al diccionario
# Se crea una nueva clave y se le asigna un valor.
# ------------------------------------------------------------

dic = {"1": "a", "2": "b"}

print(dic)

dic["3"] = "c"

print(dic)


# ------------------------------------------------------------
# Modificar el valor de una clave existente
# Al asignar un nuevo valor a una clave que ya existe,
# el valor anterior es reemplazado.
# ------------------------------------------------------------

dic["2"] = "e"

print(dic)


# ------------------------------------------------------------
# Método keys()
# Devuelve una vista con todas las claves del diccionario.
# ------------------------------------------------------------

dic = {"1": "a", "2": "b"}

print(dic.keys())


# ------------------------------------------------------------
# Método values()
# Devuelve una vista con todos los valores del diccionario.
# ------------------------------------------------------------

print(dic.values())


# ------------------------------------------------------------
# Método items()
# Devuelve una vista con los pares de clave y valor
# contenidos en el diccionario.
# ------------------------------------------------------------

print(dic.items())