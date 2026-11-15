# ==================================================
# PRÁCTICA POLIMORFISMO 3
# Objetivo: crear la función personaje_defender(),
# que recibe una instancia de cualquier personaje
# (Mago, Arquero, Samurai) y ejecuta su método
# defender() sin importar de qué tipo se trate.
# ==================================================

# --------------------------------------------------
# CLASE MAGO
# Personaje del juego que se defiende con magia.
# --------------------------------------------------
class Mago():
    """Representa a un mago del juego."""

    # ------------------------------
    # Método: defender
    # ------------------------------
    def defender(self):
        """Imprime la defensa del mago.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Escudo mágico".
        """
        print("Escudo mágico")

# --------------------------------------------------
# CLASE ARQUERO
# Personaje del juego que se defiende escondiéndose.
# --------------------------------------------------
class Arquero():
    """Representa a un arquero del juego."""

    # ------------------------------
    # Método: defender
    # ------------------------------
    def defender(self):
        """Imprime la defensa del arquero.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Esconderse".
        """
        print("Esconderse")

# --------------------------------------------------
# CLASE SAMURAI
# Personaje del juego que se defiende bloqueando.
# --------------------------------------------------
class Samurai():
    """Representa a un samurai del juego."""

    # ------------------------------
    # Método: defender
    # ------------------------------
    def defender(self):
        """Imprime la defensa del samurai.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Bloqueo".
        """
        print("Bloqueo")

# --------------------------------------------------
# FUNCIÓN POLIMÓRFICA
# personaje_defender() funciona con cualquier objeto
# que tenga un método defender(); cada clase responde
# con su propia defensa aunque el método se llame
# igual.
# --------------------------------------------------
def personaje_defender(personaje):
    """Ejecuta la defensa del personaje recibido.

    Parámetros:
        personaje: instancia de Mago, Arquero o Samurai.
    Devuelve: nada, solo imprime la defensa del personaje.
    """
    personaje.defender()

# --------------------------------------------------
# INSTANCIAS DE CADA PERSONAJE
# mago: instancia de la clase Mago.
# arquero: instancia de la clase Arquero.
# samurai: instancia de la clase Samurai.
# --------------------------------------------------
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# --------------------------------------------------
# PRUEBA DE LA FUNCIÓN CON CADA PERSONAJE
# Se llama a personaje_defender() una vez por cada
# instancia para comprobar que la misma función
# sirve para los tres tipos de personaje.
# Resultado esperado: imprime
#   Escudo mágico
#   Esconderse
#   Bloqueo
# --------------------------------------------------
personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)