# ============================================================
# PRÁCTICA HERENCIA 3
# Objetivo: Crear una clase base Vehiculo con atributos (marca,
# modelo, color y año) y los métodos acelerar() y frenar(), una
# clase Automovil que los herede, y pedir al usuario los datos
# de su automóvil para mostrarlos y probar los métodos.
# ============================================================


# ------------------------------------------------------------
# CLASE BASE: Vehiculo
# Define los atributos de instancia del vehículo y los métodos
# que comparten todas las clases que hereden de ella.
# ------------------------------------------------------------
class Vehiculo:
    def __init__(self, marca, modelo, color, anio):
        # Guardamos los valores recibidos como atributos del objeto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio

    def mostrar_datos(self):
        # Imprime la ficha del vehículo con sus atributos
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Año: {self.anio}\n")

    def acelerar(self):
        # Usa los atributos del objeto para personalizar el mensaje
        print(f"El {self.marca} {self.modelo} está acelerando.")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando.")


# ------------------------------------------------------------
# CLASE DERIVADA: Automovil
# Hereda de Vehiculo sus atributos y métodos; con "pass" no
# agrega nada nuevo y usa todo lo de la clase base.
# ------------------------------------------------------------
class Automovil(Vehiculo):
    pass


# ------------------------------------------------------------
# PEDIR LOS DATOS AL USUARIO
# Se solicitan marca, modelo, color y año; el año se convierte
# a entero porque input() siempre regresa texto.
# ------------------------------------------------------------
marca = input("Escribe la marca del automóvil: ")
modelo = input("Escribe el modelo: ")
color = input("Escribe el color: ")
anio = int(input("Escribe el año: "))


# ------------------------------------------------------------
# CREAR UNA INSTANCIA DE AUTOMOVIL
# Se crea el objeto mi_auto con los datos del usuario.
# ------------------------------------------------------------
mi_auto = Automovil(marca, modelo, color, anio)


# ------------------------------------------------------------
# MOSTRAR DATOS Y LLAMAR A LOS MÉTODOS HEREDADOS
# Todos estos métodos vienen de la clase Vehiculo.
# ------------------------------------------------------------
mi_auto.mostrar_datos()
mi_auto.acelerar()
mi_auto.frenar()