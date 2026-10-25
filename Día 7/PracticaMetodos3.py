# ==================================================
# Práctica: Métodos 3
# Objetivo: Crear una clase llamada Alarma con el método
# postergar(cantidad_minutos), que imprima el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos}
# minutos", y ejecutarlo en una instancia de Alarma.
# ==================================================

# --------------------------------------------------
# Definir la clase Alarma
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula.
# Una instancia es el objeto en sí, creado a partir
# del molde; en esta clase, cada instancia es una
# alarma.
# Atributos de clase: ninguno.
# Atributos de instancia: ninguno.
# Instancias: se crea una más adelante, llamada
# mi_alarma
# --------------------------------------------------
class Alarma:
    """Clase que representa a una alarma."""

    # ----------------------------------------------
    # Método: postergar()
    # Se ejecuta al llamarlo con una instancia; recibe
    # la cantidad de minutos que se pospone la alarma
    # e imprime el mensaje con ese valor
    # ----------------------------------------------
    def postergar(self, cantidad_minutos):
        """Muestra en pantalla cuántos minutos se pospuso la alarma.

        Parámetros:
            cantidad_minutos: minutos que se pospone la alarma (entero).

        Devuelve:
            Nada; solo imprime el mensaje en pantalla.
        """
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


# --------------------------------------------------
# Crear una instancia de Alarma
# Se crea la variable mi_alarma, que es la instancia
# (una alarma) creada a partir de la clase Alarma
# --------------------------------------------------
mi_alarma = Alarma()

# --------------------------------------------------
# Postergar la alarma
# Se llama al método postergar() con la instancia
# mi_alarma y se le pasa 10 como cantidad de minutos;
# imprime:
# La alarma ha sido pospuesta 10 minutos
# --------------------------------------------------
mi_alarma.postergar(10)