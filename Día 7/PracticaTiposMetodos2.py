# ==================================================
# Práctica Tipos de Métodos 2
# Objetivo: crear un método de clase revivir() que
# cambie el atributo de clase vivo de la clase
# Jugador a True cada vez que se invoque.
# ==================================================


# --------------------------------------------------
# Clase Jugador
# Representa a un jugador. Su estado de vida se
# guarda en un atributo de clase, compartido por
# todos los jugadores.
# --------------------------------------------------
class Jugador:
    """Clase que representa a un jugador del juego."""

    # ------------------------------
    # Atributo de clase vivo
    # Indica si el jugador está vivo. Su valor
    # predeterminado es False.
    # ------------------------------
    vivo = False

    # ------------------------------
    # Método de clase revivir
    # El decorador @classmethod hace que el método
    # reciba cls (la clase) en lugar de self, por lo
    # que modifica el atributo para toda la clase.
    # Resultado esperado: Jugador.vivo pasa a True.
    # ------------------------------
    @classmethod
    def revivir(cls):
        """
        Revive al jugador cambiando el atributo de clase vivo.

        Parámetros:
            cls: la clase Jugador.

        Devuelve:
            None. Solo modifica el atributo vivo a True.
        """
        cls.vivo = True