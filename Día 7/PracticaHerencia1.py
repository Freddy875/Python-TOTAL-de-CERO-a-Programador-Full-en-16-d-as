# ============================================================
# PRÁCTICA HERENCIA 1 (CON DATOS DEL USUARIO)
# Objetivo: Crear una clase base Persona con los atributos de
# instancia nombre y edad, una clase Alumno que los herede, y
# pedir al usuario sus datos para crear el objeto.
# ============================================================


# ------------------------------------------------------------
# CLASE BASE: Persona
# Define los atributos de instancia nombre y edad, que se
# asignan al crear cada objeto.
# ------------------------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        # Guardamos los valores recibidos como atributos del objeto
        self.nombre = nombre
        self.edad = edad


# ------------------------------------------------------------
# CLASE DERIVADA: Alumno
# Hereda de Persona; con "pass" no agrega nada nuevo y usa
# el __init__ de la clase base.
# ------------------------------------------------------------
class Alumno(Persona):
    pass


# ------------------------------------------------------------
# PEDIR LOS DATOS AL USUARIO
# Se solicitan nombre y edad; la edad se convierte a entero
# porque input() siempre regresa texto.
# ------------------------------------------------------------
nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))


# ------------------------------------------------------------
# CREAR UNA INSTANCIA DE ALUMNO
# Se crea el objeto alumno1 con los datos que dio el usuario.
# ------------------------------------------------------------
alumno1 = Alumno(nombre, edad)


# ------------------------------------------------------------
# MOSTRAR LOS ATRIBUTOS HEREDADOS
# Se imprimen nombre y edad, que vienen de la clase Persona.
# ------------------------------------------------------------
print(f"Nombre: {alumno1.nombre}, Edad: {alumno1.edad}")