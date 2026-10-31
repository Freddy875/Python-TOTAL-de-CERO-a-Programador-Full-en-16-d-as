class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"¡Flecha lanzada! Flechas restantes: {self.cantidad_flechas}")
        else:
            print("¡No quedan flechas!")

# Crear una instancia con 3 flechas
legolas = Personaje(3)

# Lanzar flechas
legolas.lanzar_flecha()
legolas.lanzar_flecha()
legolas.lanzar_flecha()
legolas.lanzar_flecha()  # Sin flechas
