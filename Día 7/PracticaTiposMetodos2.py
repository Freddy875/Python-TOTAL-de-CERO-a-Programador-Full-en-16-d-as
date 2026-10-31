# ==================================================
# Práctica Tipos de Métodos 2 (con salida)
# Objetivo: usar el método de clase revivir() para
# cambiar el atributo de clase vivo de la clase
# Jugador y mostrar en pantalla el antes y el
# después.
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


# --------------------------------------------------
# Estado inicial del jugador
# Se consulta el atributo vivo antes de revivir.
# Resultado esperado: imprime "¿Está vivo? False"
# --------------------------------------------------
print(f"¿Está vivo? {Jugador.vivo}")


# --------------------------------------------------
# Revivir al jugador
# Se llama al método de clase directamente desde la
# clase, sin crear una instancia.
# --------------------------------------------------
Jugador.revivir()


# --------------------------------------------------
# Estado final del jugador
# Se consulta de nuevo el atributo vivo después de
# revivir.
# Resultado esperado: imprime "¿Está vivo? True"
# --------------------------------------------------
print(f"¿Está vivo? {Jugador.vivo}")