# ------------------------------------------------------------
# Diccionario principal
# Comienza vacío y permite agregar nuevas personas utilizando
# un ID como clave principal.
# ------------------------------------------------------------

personas = {}


# ------------------------------------------------------------
# Agregar a Karen
# El ID 1 funciona como clave para acceder a su diccionario
# con toda su información.
# ------------------------------------------------------------

personas[1] = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
}


# ------------------------------------------------------------
# Agregar a Lois
# El ID 2 funciona como clave y contiene otro diccionario
# con la información de Lois.
# ------------------------------------------------------------

personas[2] = {
    "nombre": "Lois",
    "apellido": "Lane",
    "edad": 35,
    "ocupacion": "Periodista",
    "pais": "Estados Unidos"
}


# ------------------------------------------------------------
# Mostrar todas las personas
# items() permite obtener cada ID junto con el diccionario
# de información asociado.
# ------------------------------------------------------------

for id, persona in personas.items():
    print(f"ID: {id}")
    print(persona)