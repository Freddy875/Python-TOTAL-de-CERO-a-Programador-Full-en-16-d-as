# ==================================================
# Práctica Tipos de Métodos 1
# Objetivo: crear un método estático respirar() en la
# clase Mascota que imprima "Inhalar... Exhalar" y
# llamarlo sin necesidad de crear una instancia.
# ==================================================


# --------------------------------------------------
# Clase Mascota
# Representa una mascota y contiene un método
# estático que no depende de ningún objeto ni de la
# clase para funcionar.
# --------------------------------------------------
class Mascota:
    """Clase que representa a una mascota."""

    # ------------------------------
    # Método estático respirar
    # El decorador @staticmethod indica que el método
    # no recibe self ni cls, por lo que se puede usar
    # directamente desde la clase.
    # ------------------------------
    @staticmethod
    def respirar():
        """
        Imprime en pantalla el proceso de respiración.

        Parámetros:
            Ninguno.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Inhalar... Exhalar")


# --------------------------------------------------
# Llamada al método estático
# Se invoca desde la clase Mascota sin crear una
# instancia.
# Resultado esperado: imprime "Inhalar... Exhalar"
# --------------------------------------------------
Mascota.respirar()