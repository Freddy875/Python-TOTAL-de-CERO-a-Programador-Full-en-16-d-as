# ==================================================
# Práctica: Atributos 1 (versión con datos del usuario)
# Objetivo: Crear una clase llamada Casa con los
# atributos color y cantidad_pisos, pedir esos valores
# al usuario, crear una instancia con ellos y mostrar
# su descripción con un método.
# ==================================================

# --------------------------------------------------
# Definir la clase Casa
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula
# --------------------------------------------------
class Casa:
    """Clase que representa a una casa con su color y cantidad de pisos."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta automáticamente al crear un objeto; recibe los
    # valores iniciales y los guarda como atributos de la instancia
    # (self representa al objeto que se está creando)
    # ----------------------------------------------
    def __init__(self, color, cantidad_pisos):
        """Inicializa la casa con su color y su cantidad de pisos.

        Parámetros:
            color: color de la casa (texto).
            cantidad_pisos: número de pisos de la casa (entero).
        """
        # Guardar el color recibido en el atributo color del objeto
        self.color = color

        # Guardar la cantidad de pisos en el atributo cantidad_pisos
        self.cantidad_pisos = cantidad_pisos

    # ----------------------------------------------
    # Método describir()
    # Muestra el color y la cantidad de pisos usando una f-string,
    # que inserta los valores de los atributos dentro del texto
    # ----------------------------------------------
    def describir(self):
        """Muestra en pantalla el color y la cantidad de pisos de la casa."""
        print(f"La casa es de color {self.color} y tiene {self.cantidad_pisos} pisos.")

# --------------------------------------------------
# Pedir los datos de la casa al usuario
# input() muestra una pregunta y devuelve lo que el usuario escribe
# siempre como texto; por eso la cantidad de pisos se convierte a
# número entero con int()
# --------------------------------------------------
color_casa = input("¿De qué color es tu casa? ")
pisos_casa = int(input("¿Cuántos pisos tiene? "))

# --------------------------------------------------
# Crear la instancia
# Los valores escritos por el usuario se envían a __init__ y se
# guardan en color y cantidad_pisos
# --------------------------------------------------
mi_casa = Casa(color_casa, pisos_casa)

# --------------------------------------------------
# Usar el método para describir la casa
# Se llama al método con la instancia; imprime, por ejemplo:
# La casa es de color blanco y tiene 4 pisos.
# --------------------------------------------------
mi_casa.describir()