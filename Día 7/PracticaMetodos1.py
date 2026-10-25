# ==================================================
# Práctica: Métodos 1
# Objetivo: Crear una clase llamada Perro con el método
# ladrar(), que cada vez que se ejecute muestre en
# pantalla "Guau!", y ejecutarlo en una instancia de
# Perro.
# ==================================================

# --------------------------------------------------
# Definir la clase Perro
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula.
# Una instancia es el objeto en sí, creado a partir
# del molde; en esta clase, cada instancia es un perro.
# Atributos de clase: ninguno.
# Atributos de instancia: ninguno.
# Instancias: se crea una más adelante, llamada
# mi_perro
# --------------------------------------------------
class Perro:
    """Clase que representa a un perro."""

    # ----------------------------------------------
    # Método: ladrar()
    # Se ejecuta al llamarlo con una instancia; hace que
    # el perro ladre mostrando en pantalla: Guau!
    # ----------------------------------------------
    def ladrar(self):
        """Muestra en pantalla el ladrido del perro.

        Devuelve:
            Nada; solo imprime "Guau!" en pantalla.
        """
        print("Guau!")


# --------------------------------------------------
# Crear una instancia de Perro
# Se crea la variable mi_perro, que es la instancia
# (un perro) creada a partir de la clase Perro
# --------------------------------------------------
mi_perro = Perro()

# --------------------------------------------------
# Hacer que el perro ladre
# Se llama al método ladrar() con la instancia
# mi_perro; imprime:
# Guau!
# --------------------------------------------------
mi_perro.ladrar()