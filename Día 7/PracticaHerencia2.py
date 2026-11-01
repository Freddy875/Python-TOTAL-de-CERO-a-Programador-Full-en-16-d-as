# Clase base
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

# Clase derivada
class Perro(Mascota):
    pass

# Crear una instancia de Perro
mi_perro = Perro(5, "Fido", 4)

# Mostrar los atributos heredados
print(f"Nombre: {mi_perro.nombre}, Edad: {mi_perro.edad}, Patas: {mi_perro.cantidad_patas}")
