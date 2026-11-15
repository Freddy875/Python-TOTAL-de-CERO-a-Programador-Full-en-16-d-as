# ==================================================
# PRÁCTICA POLIMORFISMO 2
# Objetivo: lograr un ataque conjugado de tres
# personajes de un juego (Arquero, Mago, Samurai),
# llamando al método atacar() de cada uno dentro de
# un mismo ciclo, gracias al polimorfismo.
# ==================================================

# --------------------------------------------------
# CLASE MAGO
# Personaje del juego cuyo ataque es mágico.
# --------------------------------------------------
class Mago():
    """Representa a un mago del juego."""

    # ------------------------------
    # Método: atacar
    # ------------------------------
    def atacar(self):
        """Imprime el ataque del mago.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Ataque mágico".
        """
        print("Ataque mágico")

# --------------------------------------------------
# CLASE ARQUERO
# Personaje del juego cuyo ataque es con flechas.
# --------------------------------------------------
class Arquero():
    """Representa a un arquero del juego."""

    # ------------------------------
    # Método: atacar
    # ------------------------------
    def atacar(self):
        """Imprime el ataque del arquero.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Lanzamiento de flecha".
        """
        print("Lanzamiento de flecha")

# --------------------------------------------------
# CLASE SAMURAI
# Personaje del juego cuyo ataque es con katana.
# --------------------------------------------------
class Samurai():
    """Representa a un samurai del juego."""

    # ------------------------------
    # Método: atacar
    # ------------------------------
    def atacar(self):
        """Imprime el ataque del samurai.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Ataque con katana".
        """
        print("Ataque con katana")

# --------------------------------------------------
# INSTANCIAS DE CADA PERSONAJE
# arquero: instancia de la clase Arquero.
# mago: instancia de la clase Mago.
# samurai: instancia de la clase Samurai.
# --------------------------------------------------
arquero = Arquero()
mago = Mago()
samurai = Samurai()

# --------------------------------------------------
# LISTA DE PERSONAJES
# personajes: lista con las tres instancias en el
# orden del ataque: Arquero, Mago, Samurai.
# --------------------------------------------------
personajes = [arquero, mago, samurai]

# --------------------------------------------------
# ATAQUE CONJUGADO
# El ciclo for recorre la lista personajes. En cada
# vuelta, personaje toma una instancia y se llama a
# su método atacar(); cada clase responde con su
# propio ataque aunque el método se llame igual.
# Resultado esperado: imprime
#   Lanzamiento de flecha
#   Ataque mágico
#   Ataque con katana
# --------------------------------------------------
for personaje in personajes:
    # Ejecuta el ataque propio del personaje actual
    personaje.atacar()