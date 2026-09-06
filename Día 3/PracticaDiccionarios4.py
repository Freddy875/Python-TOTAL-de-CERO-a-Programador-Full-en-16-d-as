# ------------------------------------------------------------
# Lista de personas
# Cada elemento agregado será un diccionario con la información
# de una persona.
# ------------------------------------------------------------

personas = []


# ------------------------------------------------------------
# Agregar a Karen
# Se crea un diccionario con sus datos y se agrega a la lista.
# ------------------------------------------------------------

karen = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
}

personas.append(karen)


# ------------------------------------------------------------
# Agregar a Lois
# Se crea un diccionario con sus datos, incluyendo su edad,
# y se agrega a la lista de personas.
# ------------------------------------------------------------

lois = {
    "nombre": "Lois",
    "apellido": "Lane",
    "edad": 35,
    "ocupacion": "Periodista",
    "pais": "Estados Unidos"
}

personas.append(lois)


# ------------------------------------------------------------
# Mostrar todas las personas
# El ciclo for recorre la lista y muestra cada persona que
# haya sido agregada.
# ------------------------------------------------------------

for persona in personas:
    print(persona)