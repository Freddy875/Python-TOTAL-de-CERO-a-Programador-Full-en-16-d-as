<<<<<<< HEAD
# Definir la función para describir a una persona
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")  # Encabezado con el nombre
    for clave, valor in kwargs.items():  # Recorrer los argumentos nombrados
        print(f"{clave}: {valor}")  # Imprimir cada característica
=======
# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crear una función que reciba el nombre de una persona y una
# cantidad indeterminada de características, para mostrarlas
# en pantalla junto con sus respectivos valores.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para describir a una persona
# nombre recibe el nombre de la persona.
# **kwargs recibe argumentos nombrados y los reúne en un
# diccionario, donde cada clave representa una característica
# y cada valor contiene el dato correspondiente.
# ------------------------------------------------------------
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")  # Muestra el encabezado con el nombre

    # Recorre las claves y los valores del diccionario kwargs.
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")  # Muestra cada característica y su valor


# ------------------------------------------------------------
# No se invoca la función, según la consigna.
# ------------------------------------------------------------
>>>>>>> 92fa96b (Crear un funcion que recibe el nombre de una persona y una cantidad indeterminada de caracteristicas)
