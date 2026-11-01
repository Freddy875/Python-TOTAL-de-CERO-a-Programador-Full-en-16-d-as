# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Clase derivada
class Alumno(Persona):
    pass

# Crear una instancia de Alumno
alumno1 = Alumno("Ana", 20)

# Mostrar los atributos heredados
print(f"Nombre: {alumno1.nombre}, Edad: {alumno1.edad}")
        