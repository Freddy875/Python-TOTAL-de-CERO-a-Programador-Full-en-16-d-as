# ------------------------------------------------------------
# Crear una función para mostrar un saludo.
# En este primer ejemplo, la función no recibe parámetros.
# ------------------------------------------------------------

def saludar_persona():

    # Esta función muestra un saludo en pantalla.
    print("Hola mundo")


# ------------------------------------------------------------
# Llama a la función para ejecutar el saludo.
# ------------------------------------------------------------

saludar_persona()


# ------------------------------------------------------------
# Crear una función con parámetro.
# La función recibe un nombre y lo utiliza para crear
# un saludo personalizado.
# ------------------------------------------------------------

def saludar_persona(nombre):

    # Esta función recibe un nombre y muestra un saludo.
    print(f"Hola, {nombre}!")


# ------------------------------------------------------------
# Solicita al usuario su nombre y almacena la respuesta
# en la variable nombre.
# ------------------------------------------------------------

nombre = input("¿Cuál es tu nombre? ")


# ------------------------------------------------------------
# Llama a la función y le pasa el nombre introducido
# por el usuario como argumento.
# ------------------------------------------------------------

saludar_persona(nombre)