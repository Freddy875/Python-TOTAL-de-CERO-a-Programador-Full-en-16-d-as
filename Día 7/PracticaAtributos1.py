# ==================================================
# Práctica: Atributos 1
# Objetivo: Crear una clase llamada Casa con los
# atributos color y cantidad_pisos, crear una instancia
# llamada casa_blanca de color "blanco" y con 4 pisos,
# y mostrar su descripción con un método.
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
# Crear la instancia
# Los valores entre paréntesis se envían a __init__: "blanco" se
# guarda en color y 4 en cantidad_pisos
# --------------------------------------------------
casa_blanca = Casa("blanco", 4)

# --------------------------------------------------
# Usar el método para describir la casa
# Se llama al método con la instancia; imprime:
# La casa es de color blanco y tiene 4 pisos.
# --------------------------------------------------
casa_blanca.describir()