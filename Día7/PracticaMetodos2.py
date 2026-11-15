# ==================================================
# Práctica: Métodos 2
# Objetivo: Crear una clase llamada Mago con el método
# lanzar_hechizo(), que imprima "¡Abracadabra!", crear
# una instancia de Mago en el objeto merlin y hacer que
# lance un hechizo.
# ==================================================

# --------------------------------------------------
# Definir la clase Mago
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula.
# Una instancia es el objeto en sí, creado a partir
# del molde; en esta clase, cada instancia es un mago.
# Atributos de clase: ninguno.
# Atributos de instancia: ninguno.
# Instancias: se crea una más adelante, llamada merlin
# --------------------------------------------------
class Mago:
    """Clase que representa a un mago."""

    # ----------------------------------------------
    # Método: lanzar_hechizo()
    # Se ejecuta al llamarlo con una instancia; hace que
    # el mago lance un hechizo mostrando en pantalla:
    # ¡Abracadabra!
    # ----------------------------------------------
    def lanzar_hechizo(self):
        """Muestra en pantalla el hechizo del mago.

        Devuelve:
            Nada; solo imprime "¡Abracadabra!" en pantalla.
        """
        print("¡Abracadabra!")


# --------------------------------------------------
# Crear una instancia de Mago
# Se crea la variable merlin, que es la instancia
# (un mago) creada a partir de la clase Mago
# --------------------------------------------------
merlin = Mago()

# --------------------------------------------------
# Hacer que lance un hechizo
# Se llama al método lanzar_hechizo() con la instancia
# merlin; imprime:
# ¡Abracadabra!
# --------------------------------------------------
merlin.lanzar_hechizo()