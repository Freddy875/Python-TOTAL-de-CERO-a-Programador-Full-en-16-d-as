# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Solicitar el nombre y una cantidad indeterminada de
# características de una persona para mostrarlas al final.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para describir a una persona
# nombre recibe el nombre de la persona.
# **kwargs recibe las características y sus valores.
# items() permite recorrer cada clave y su valor.
# ------------------------------------------------------------
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


# ------------------------------------------------------------
# Solicitar el nombre de la persona.
# ------------------------------------------------------------
nombre = input("Ingresa el nombre de la persona: ")


# ------------------------------------------------------------
# Recopilar las características de la persona.
# El usuario puede agregar tantas características como quiera.
# ------------------------------------------------------------
caracteristicas = {}

print("Ingresa las características de la persona.")
print("Ejemplo: color_ojos, azules")
print("Escribe 'no' cuando quieras terminar.")

while True:
    respuesta = input("¿Quieres agregar una característica? (si/no): ").lower()

    if respuesta == "no":
        break

    nombre_atributo = input("Nombre de la característica: ")
    valor_atributo = input("Valor de la característica: ")

    caracteristicas[nombre_atributo] = valor_atributo


# ------------------------------------------------------------
# Llamar a la función y mostrar todas las características.
# **caracteristicas desempaqueta el diccionario como argumentos
# nombrados para la función describir_persona().
# ------------------------------------------------------------
describir_persona(nombre, **caracteristicas)
