# ============================================================
# PRÁCTICA HERENCIA 1
# Objetivo: Crear una clase base Persona con los atributos de
# instancia nombre y edad, y una clase Alumno que los herede.
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
# CREAR UNA INSTANCIA DE ALUMNO
# Se crea el objeto alumno1 con nombre y edad fijos.
# ------------------------------------------------------------
alumno1 = Alumno("Ana", 20)


# ------------------------------------------------------------
# MOSTRAR LOS ATRIBUTOS HEREDADOS
# Se imprimen nombre y edad, que vienen de la clase Persona.
# ------------------------------------------------------------
print(f"Nombre: {alumno1.nombre}, Edad: {alumno1.edad}")