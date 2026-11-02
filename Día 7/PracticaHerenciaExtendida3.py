# ==================================================
# PRÁCTICA HERENCIA EXTENDIDA 3
# Objetivo: lograr que la clase Hijo herede de Padre
# todos sus atributos y métodos, sobrescribiendo
# hobby() para que tenga un pasatiempo diferente.
# ==================================================


# --------------------------------------------------
# CLASE PADRE
# Define las características físicas, el deporte
# preferido y los métodos que la clase Hijo va a heredar.
# --------------------------------------------------
class Padre():
    """Representa al padre, con sus características y hábitos."""

    # ------------------------------
    # Atributos de clase
    # color_ojos: color de los ojos.
    # tipo_pelo: forma del pelo.
    # altura: estatura.
    # voz: tono de la voz.
    # deporte_preferido: deporte que más le gusta.
    # ------------------------------
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    # ------------------------------
    # Método reir
    # Devuelve la forma de reír del padre.
    # ------------------------------
    def reir(self):
        """Devuelve la forma de reír.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            str: el texto de la risa.
        """
        return "Jajaja"

    # ------------------------------
    # Método hobby
    # Devuelve el pasatiempo del padre.
    # ------------------------------
    def hobby(self):
        """Devuelve el pasatiempo del padre.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            str: la descripción del pasatiempo.
        """
        return "Pinto madera en mi tiempo libre"

    # ------------------------------
    # Método caminar
    # Devuelve la forma de caminar del padre.
    # ------------------------------
    def caminar(self):
        """Devuelve la forma de caminar.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            str: la descripción de la forma de caminar.
        """
        return "Caminando con pasos largos y rápidos"


# --------------------------------------------------
# CLASE HIJO
# Hereda todo de Padre, pero sobrescribe hobby(). Como
# Python busca primero en Hijo, usa esa versión y no la
# de Padre.
# --------------------------------------------------
class Hijo(Padre):
    """Representa al hijo, que tiene su propio pasatiempo."""

    # ------------------------------
    # Método hobby (sobrescrito)
    # Reemplaza el pasatiempo heredado de Padre.
    # ------------------------------
    def hobby(self):
        """Devuelve el pasatiempo del hijo.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            str: la descripción del pasatiempo.
        """
        return "Juego videojuegos en mi tiempo libre"


# --------------------------------------------------
# PRUEBA DE LA HERENCIA
# Crea un hijo y muestra un atributo heredado, un método
# heredado y el método sobrescrito.
# Variables:
#   hijo: objeto de la clase Hijo.
# Resultado esperado:
#   marrón
#   Jajaja
#   Juego videojuegos en mi tiempo libre
# --------------------------------------------------
hijo = Hijo()
print(hijo.color_ojos)          # Heredado del padre
print(hijo.reir())              # Heredado del padre
print(hijo.hobby())             # Método sobrescrito