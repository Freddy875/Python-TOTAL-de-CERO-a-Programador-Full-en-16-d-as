# ==================================================
# Práctica Tipos de Métodos 2 (con interacción)
# Objetivo: avisar al jugador que está muerto,
# preguntarle si quiere revivir y, según su
# respuesta, usar el método de clase revivir() o
# terminar el juego.
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
# Preguntar al jugador
# respuesta: guarda lo que escribe el usuario. Se
# usa strip() para quitar espacios y lower() para
# aceptar mayúsculas o minúsculas (Si, SI, si).
# Resultado esperado: muestra el aviso y espera la
# respuesta del usuario.
# --------------------------------------------------
print("Jugador, estás muerto.")
respuesta = input("¿Quieres revivir? (si/no): ").strip().lower()


# --------------------------------------------------
# Decidir según la respuesta
# Si responde "si" o "sí", se llama a revivir() y se
# confirma con el atributo vivo. Si responde "no",
# termina el juego. Cualquier otra respuesta se
# considera no válida.
# Resultado esperado:
#   si -> "¡Has revivido! ¿Está vivo? True"
#   no -> "Fin del juego"
#   otra -> "Respuesta no válida. Fin del juego"
# --------------------------------------------------
if respuesta in ("si", "sí"):
    Jugador.revivir()
    print(f"¡Has revivido! ¿Está vivo? {Jugador.vivo}")
elif respuesta == "no":
    print("Fin del juego")
else:
    print("Respuesta no válida. Fin del juego")