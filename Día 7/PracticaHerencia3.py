# Clase base
class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

# Clase derivada
class Automovil(Vehiculo):
    pass

# Crear una instancia de Automovil
mi_auto = Automovil()

# Llamar a los métodos heredados (aunque no hacen nada aún)
mi_auto.acelerar()
mi_auto.frenar()
