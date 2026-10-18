# ==================================================
# Práctica: Atributos 2
# Objetivo: Crear una clase llamada Cubo con el atributo
# de clase caras (igual a 6) y el atributo de instancia
# color, crear una instancia llamada cubo_rojo de color
# "rojo" y mostrar su descripción con un método.
# ==================================================

# --------------------------------------------------
# Definir la clase Cubo
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula
# --------------------------------------------------
class Cubo:
    """Clase que representa a un cubo con su color y su cantidad de caras."""

    # ----------------------------------------------
    # Atributo de clase
    # caras vale 6 para todos los cubos: se define dentro de la
    # clase, fuera de los métodos, y lo comparten todas las instancias
    # ----------------------------------------------
    caras = 6

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta automáticamente al crear un objeto; recibe el
    # color y lo guarda como atributo de la instancia
    # (self representa al objeto que se está creando)
    # ----------------------------------------------
    def __init__(self, color):
        """Inicializa el cubo con su color.

        Parámetros:
            color: color del cubo (texto).
        """
        # Atributo de instancia: color es propio de cada cubo, y se
        # guarda con self para que cada objeto tenga su propio valor
        self.color = color

    # ----------------------------------------------
    # Método describir()
    # Muestra el color y la cantidad de caras usando una f-string;
    # el color se toma de la instancia (self) y las caras de la
    # clase (Cubo)
    # ----------------------------------------------
    def describir(self):
        """Muestra en pantalla el color y la cantidad de caras del cubo."""
        print(f"Este cubo es de color {self.color} y tiene {Cubo.caras} caras.")

# --------------------------------------------------
# Crear la instancia
# "rojo" se envía a __init__ y se guarda en el atributo color
# de cubo_rojo
# --------------------------------------------------
cubo_rojo = Cubo("rojo")

# --------------------------------------------------
# Usar el método para describir el cubo
# Se llama al método con la instancia; imprime:
# Este cubo es de color rojo y tiene 6 caras.
# --------------------------------------------------
cubo_rojo.describir()