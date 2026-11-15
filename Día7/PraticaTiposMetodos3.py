# ==================================================
# Práctica Tipos de Métodos 3
# Objetivo: crear un método de instancia
# lanzar_flecha() que reste 1 a la cantidad de
# flechas de un Personaje y avise cuando ya no
# queden flechas.
# ==================================================


# --------------------------------------------------
# Clase Personaje
# Representa a un personaje que puede lanzar
# flechas. Cada instancia guarda su propia cantidad
# de flechas.
# --------------------------------------------------
class Personaje:
    """Clase que representa a un personaje arquero."""

    # ------------------------------
    # Método constructor __init__
    # Se ejecuta al crear un personaje.
    # cantidad_flechas: atributo de instancia con el
    # número de flechas que tiene ese personaje.
    # ------------------------------
    def __init__(self, cantidad_flechas):
        """
        Inicializa al personaje con sus flechas.

        Parámetros:
            cantidad_flechas (int): flechas iniciales.

        Devuelve:
            None.
        """
        self.cantidad_flechas = cantidad_flechas

    # ------------------------------
    # Método de instancia lanzar_flecha
    # Usa self para trabajar con las flechas de ese
    # personaje en particular. Si tiene flechas, resta
    # 1 e informa cuántas quedan; si no, avisa que no
    # quedan flechas.
    # ------------------------------
    def lanzar_flecha(self):
        """
        Lanza una flecha si hay disponibles.

        Parámetros:
            self: la instancia de Personaje.

        Devuelve:
            None. Solo modifica cantidad_flechas e imprime el resultado.
        """
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"¡Flecha lanzada! Flechas restantes: {self.cantidad_flechas}")
        else:
            print("¡No quedan flechas!")


# --------------------------------------------------
# Crear una instancia con 3 flechas
# legolas: objeto de la clase Personaje que empieza
# con 3 flechas.
# --------------------------------------------------
legolas = Personaje(3)


# --------------------------------------------------
# Lanzar flechas
# Se llama 4 veces al método: las 3 primeras gastan
# las flechas y la cuarta muestra el aviso.
# Resultado esperado:
#   ¡Flecha lanzada! Flechas restantes: 2
#   ¡Flecha lanzada! Flechas restantes: 1
#   ¡Flecha lanzada! Flechas restantes: 0
#   ¡No quedan flechas!
# --------------------------------------------------
legolas.lanzar_flecha()
legolas.lanzar_flecha()
legolas.lanzar_flecha()
legolas.lanzar_flecha() # Sin flechas