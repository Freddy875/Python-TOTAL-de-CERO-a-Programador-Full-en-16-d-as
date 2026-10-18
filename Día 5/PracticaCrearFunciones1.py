# ------------------------------------------------------------
# Práctica Crear Funciones 2
# Declara una función llamada bienvenida que recibe como
# argumento el nombre de una persona y muestra un mensaje
# de bienvenida personalizado.
# También crea una variable llamada nombre_persona
# y almacena un nombre dentro de ella.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Definir la función bienvenida.
# La función recibe el parámetro nombre_persona y lo utiliza
# para mostrar el mensaje de bienvenida.
# ------------------------------------------------------------

def bienvenida(nombre_persona):

    # Imprime un mensaje utilizando el nombre recibido
    # como argumento.
    print(f"¡Bienvenido {nombre_persona}!")


# ------------------------------------------------------------
# Crear la variable nombre_persona.
# Almacena dentro de la variable el nombre que se utilizará
# como argumento de la función.
# ------------------------------------------------------------

nombre_persona = "Carlos"

bienvenida(nombre_persona)  # Llama a la función y pasa el nombre como argumento