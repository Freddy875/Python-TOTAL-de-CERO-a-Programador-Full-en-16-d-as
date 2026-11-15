# ------------------------------------------------------------
# Diccionario principal
# Comienza vacío y permite agregar personajes utilizando
# un ID como clave principal.
# ------------------------------------------------------------

personajes_marvel = {}


# ------------------------------------------------------------
# Agregar a Spider-Man
# El ID 1 contiene un diccionario con la información
# y el poder principal del personaje.
# ------------------------------------------------------------

personajes_marvel[1] = {
    "nombre": "Peter",
    "apellido": "Parker",
    "nombre_heroe": "Spider-Man",
    "poder": "Sentido arácnido y habilidades de araña"
}


# ------------------------------------------------------------
# Agregar a Iron Man
# El ID 2 contiene la información del personaje y su
# principal habilidad o poder.
# ------------------------------------------------------------

personajes_marvel[2] = {
    "nombre": "Tony",
    "apellido": "Stark",
    "nombre_heroe": "Iron Man",
    "poder": "Armadura tecnológica"
}


# ------------------------------------------------------------
# Agregar al Capitán América
# El ID 3 contiene la información y las habilidades
# principales del personaje.
# ------------------------------------------------------------

personajes_marvel[3] = {
    "nombre": "Steve",
    "apellido": "Rogers",
    "nombre_heroe": "Capitán América",
    "poder": "Fuerza y resistencia mejoradas, escudo de Vibranium, indestructible"
}


# ------------------------------------------------------------
# Mostrar todos los personajes
# items() permite obtener cada ID y el diccionario asociado
# a cada personaje.
# ------------------------------------------------------------

for id, personaje in personajes_marvel.items():
    print(f"ID: {id}")
    print(personaje)