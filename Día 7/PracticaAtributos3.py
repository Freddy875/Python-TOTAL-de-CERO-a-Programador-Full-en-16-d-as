# ==================================================
# Práctica: Atributos 3
# Objetivo: Crear una clase llamada Personaje con el
# atributo de clase real (igual a False) y los atributos
# de instancia especie, magico y edad, crear una instancia
# llamada harry_potter con los valores "Humano", True y 17,
# y mostrar su descripción con un método.
# ==================================================

# --------------------------------------------------
# Definir la clase Personaje
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula
# --------------------------------------------------
class Personaje:
    """Clase que representa a un personaje con su especie, si es mágico y su edad."""

    # ----------------------------------------------
    # Atributo de clase
    # real vale False para todos los personajes: se define dentro
    # de la clase, fuera de los métodos, y lo comparten todas las
    # instancias
    # ----------------------------------------------
    real = False

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta automáticamente al crear un objeto; recibe los
    # valores iniciales y los guarda como atributos de la instancia
    # (self representa al objeto que se está creando)
    # ----------------------------------------------
    def __init__(self, especie, magico, edad):
        """Inicializa el personaje con su especie, si es mágico y su edad.

        Parámetros:
            especie: especie del personaje (texto).
            magico: True si el personaje es mágico, False si no (booleano).
            edad: edad del personaje (entero).
        """
        # Atributos de instancia: son propios de cada personaje, y se
        # guardan con self para que cada objeto tenga sus propios valores
        self.especie = especie
        self.magico = magico
        self.edad = edad

    # ----------------------------------------------
    # Método describir()
    # Muestra la especie, si es mágico, la edad y si es real; los
    # datos de la instancia se toman de self y real de la clase
    # (Personaje)
    # ----------------------------------------------
    def describir(self):
        """Muestra en pantalla la descripción completa del personaje."""
        # Expresión condicional: tipo vale "mágico" si magico es True,
        # y "no mágico" en caso contrario
        tipo = "mágico" if self.magico else "no mágico"

        # Se usa una f-string para insertar los valores dentro del texto
        print(f"Este personaje es un {self.especie}, {tipo}, tiene {self.edad} años y es real: {Personaje.real}.")

# --------------------------------------------------
# Crear la instancia
# Los valores entre paréntesis se envían a __init__: "Humano" se
# guarda en especie, True en magico y 17 en edad
# --------------------------------------------------
harry_potter = Personaje("Humano", True, 17)

# --------------------------------------------------
# Usar el método para describir al personaje
# Se llama al método con la instancia; imprime:
# Este personaje es un Humano, mágico, tiene 17 años y es real: False.
# --------------------------------------------------
harry_potter.describir()