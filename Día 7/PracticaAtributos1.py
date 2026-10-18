class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

    def describir(self):
        print(f"La casa es de color {self.color} y tiene {self.cantidad_pisos} pisos.")

# Crear la instancia
casa_blanca = Casa("blanco", 4)

# Usar el método para describir la casa
casa_blanca.describir()

