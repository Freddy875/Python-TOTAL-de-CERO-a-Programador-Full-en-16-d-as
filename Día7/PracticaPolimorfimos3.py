class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

# Función polimórfica
def personaje_defender(personaje):
    personaje.defender()

# Crear instancias
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Probar la función con cada personaje
personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)

