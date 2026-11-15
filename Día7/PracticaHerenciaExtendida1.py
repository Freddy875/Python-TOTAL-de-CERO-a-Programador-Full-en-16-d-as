# ==================================================
# PRÁCTICA HERENCIA EXTENDIDA 1
# Objetivo: crear una herencia múltiple para que la
# clase Hija herede de Padre la forma de reír y de
# Madre la vocación (el trabajo en la Fiscalía).
# ==================================================


# --------------------------------------------------
# CLASE PADRE
# Define el trabajo en el Hospital y la forma de reír
# que la clase Hija va a heredar.
# --------------------------------------------------
class Padre():
    """Representa al padre, con su trabajo y su forma de reír."""

    # ------------------------------
    # Método trabajar
    # Muestra el lugar de trabajo del padre.
    # ------------------------------
    def trabajar(self):
        """Imprime el lugar de trabajo del padre.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Trabajando en el Hospital")

    # ------------------------------
    # Método reir
    # Muestra la forma de reír que hereda la clase Hija.
    # ------------------------------
    def reir(self):
        """Imprime la forma de reír del padre.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Ja ja ja!")


# --------------------------------------------------
# CLASE MADRE
# Define el trabajo en la Fiscalía, que es la vocación
# que hereda la clase Hija.
# --------------------------------------------------
class Madre():
    """Representa a la madre, con su trabajo en la Fiscalía."""

    # ------------------------------
    # Método trabajar
    # Muestra el lugar de trabajo de la madre.
    # ------------------------------
    def trabajar(self):
        """Imprime el lugar de trabajo de la madre.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Trabajando en la Fiscalía")


# --------------------------------------------------
# CLASE HIJA
# Hereda de Madre y de Padre. El orden importa: Python
# busca los métodos primero en Madre y después en Padre.
# Por eso trabajar() viene de Madre, y reir(), que Madre
# no tiene, viene de Padre.
# Resultado esperado:
#   trabajar() imprime "Trabajando en la Fiscalía"
#   reir() imprime "Ja ja ja!"
# --------------------------------------------------
class Hija(Madre, Padre):
    """Representa a la hija, que hereda de Madre y de Padre."""
    pass

# --------------------------------------------------
# PRUEBA DE LA HERENCIA
# Crea un objeto de cada clase y muestra qué hace cada
# uno y qué heredó la hija de sus padres.
# Variables:
#   padre: objeto de la clase Padre.
#   madre: objeto de la clase Madre.
#   hija: objeto de la clase Hija.
# Resultado esperado:
#   El padre hace esto:
#   Trabajando en el Hospital
#   Ja ja ja!
#
#   La madre hace esto:
#   Trabajando en la Fiscalía
#
#   La hija heredó el trabajo de su madre:
#   Trabajando en la Fiscalía
#
#   La hija heredó la risa de su padre:
#   Ja ja ja!
# --------------------------------------------------
padre = Padre()
madre = Madre()
hija = Hija()

print("El padre hace esto:")
padre.trabajar()
padre.reir()

print("\nLa madre hace esto:")
madre.trabajar()

print("\nLa hija heredó el trabajo de su madre:")
hija.trabajar()

print("\nLa hija heredó la risa de su padre:")
hija.reir()