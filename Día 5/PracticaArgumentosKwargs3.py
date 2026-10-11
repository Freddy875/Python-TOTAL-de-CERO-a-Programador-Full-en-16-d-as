# Definir la función para describir a una persona
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")  # Encabezado con el nombre
    for clave, valor in kwargs.items():  # Recorrer los argumentos nombrados
        print(f"{clave}: {valor}")  # Imprimir cada característica