# ==================================================
# PRÁCTICA HERENCIA EXTENDIDA 3
# Objetivo: lograr que la clase Hijo herede de Padre
# y de Madre sus atributos y métodos, sobrescribiendo
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
# CLASE MADRE
# Define las características y los métodos que la clase
# Hijo hereda de la madre.
# --------------------------------------------------
class Madre():
    """Representa a la madre, con sus características y hábitos."""

    # ------------------------------
    # Atributos de clase
    # nariz: forma de la nariz.
    # color_pelo: color del pelo.
    # ------------------------------
    nariz = "pequeña"
    color_pelo = "castaño"

    # ------------------------------
    # Método cantar
    # Devuelve la forma de cantar de la madre.
    # ------------------------------
    def cantar(self):
        """Devuelve la forma de cantar.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            str: la descripción de la forma de cantar.
        """
        return "Cantando con voz suave"

    # ------------------------------
    # Método hobby
    # Devuelve el pasatiempo de la madre.
    # ------------------------------
    def hobby(self):
        """Devuelve el pasatiempo de la madre.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            str: la descripción del pasatiempo.
        """
        return "Leo novelas en mi tiempo libre"


# --------------------------------------------------
# CLASE HIJO
# Hereda de Padre y de Madre con herencia múltiple, y
# sobrescribe hobby() para tener su propio pasatiempo.
# Como Python busca primero en Hijo, usa esa versión y
# no las de Padre o Madre.
# --------------------------------------------------
class Hijo(Padre, Madre):
    """Representa al hijo, que tiene su propio pasatiempo."""

    # ------------------------------
    # Método hobby (sobrescrito)
    # Reemplaza el pasatiempo heredado.
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
# Crea un objeto de cada clase, muestra qué tiene el
# hijo de cada uno y compara sus hobbies.
# Variables:
#   padre: objeto de la clase Padre.
#   madre: objeto de la clase Madre.
#   hijo: objeto de la clase Hijo.
# Resultado esperado:
#   Esto es lo que tienes de tu padre:
#   Color de ojos: marrón
#   Tipo de pelo: rulos
#   Altura: media
#   Voz: grave
#   Deporte preferido: tenis
#   Risa: Jajaja
#   Forma de caminar: Caminando con pasos largos y rápidos
#
#   Esto es lo que tienes de tu madre:
#   Nariz: pequeña
#   Color de pelo: castaño
#   Forma de cantar: Cantando con voz suave
#
#   Los hobbies de cada uno:
#   Padre: Pinto madera en mi tiempo libre
#   Madre: Leo novelas en mi tiempo libre
#   Hijo: Juego videojuegos en mi tiempo libre
# --------------------------------------------------
padre = Padre()
madre = Madre()
hijo = Hijo()

print("Esto es lo que tienes de tu padre:")
print(f"Color de ojos: {hijo.color_ojos}")
print(f"Tipo de pelo: {hijo.tipo_pelo}")
print(f"Altura: {hijo.altura}")
print(f"Voz: {hijo.voz}")
print(f"Deporte preferido: {hijo.deporte_preferido}")
print(f"Risa: {hijo.reir()}")
print(f"Forma de caminar: {hijo.caminar()}")

print("\nEsto es lo que tienes de tu madre:")
print(f"Nariz: {hijo.nariz}")
print(f"Color de pelo: {hijo.color_pelo}")
print(f"Forma de cantar: {hijo.cantar()}")

print("\nLos hobbies de cada uno:")
print(f"Padre: {padre.hobby()}")
print(f"Madre: {madre.hobby()}")
print(f"Hijo: {hijo.hobby()}")