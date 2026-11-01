# ============================================================
# PRÁCTICA HERENCIA 2
# Objetivo: Crear una clase base Mascota con los atributos de
# instancia edad, nombre y cantidad_patas, una clase Perro que
# los herede, y pedir al usuario los datos de su perro.
# ============================================================


# ------------------------------------------------------------
# CLASE BASE: Mascota
# Define los atributos de instancia edad, nombre y
# cantidad_patas, que se asignan al crear cada objeto.
# ------------------------------------------------------------
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        # Guardamos los valores recibidos como atributos del objeto
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


# ------------------------------------------------------------
# CLASE DERIVADA: Perro
# Hereda de Mascota; con "pass" no agrega nada nuevo y usa
# el __init__ de la clase base.
# ------------------------------------------------------------
class Perro(Mascota):
    pass


# ------------------------------------------------------------
# PEDIR LOS DATOS AL USUARIO
# Se solicitan nombre, edad y cantidad de patas; los números
# se convierten a entero porque input() siempre regresa texto.
# ------------------------------------------------------------
nombre = input("Escribe el nombre de tu perro: ")
edad = int(input("Escribe la edad de tu perro: "))
cantidad_patas = int(input("Escribe la cantidad de patas: "))


# ------------------------------------------------------------
# CREAR UNA INSTANCIA DE PERRO
# Se crea el objeto mi_perro con los datos del usuario,
# respetando el orden del __init__: edad, nombre, patas.
# ------------------------------------------------------------
mi_perro = Perro(edad, nombre, cantidad_patas)


# ------------------------------------------------------------
# MOSTRAR LOS ATRIBUTOS HEREDADOS
# Se imprimen nombre, edad y patas, que vienen de Mascota.
# ------------------------------------------------------------
print(f"Nombre: {mi_perro.nombre}, Edad: {mi_perro.edad}, Patas: {mi_perro.cantidad_patas}")