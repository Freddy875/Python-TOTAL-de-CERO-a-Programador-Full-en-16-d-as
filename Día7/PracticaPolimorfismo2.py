class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

# Crear instancias de cada personaje
arquero = Arquero()
mago = Mago()
samurai = Samurai()

# Crear lista en el orden deseado
personajes = [arquero, mago, samurai]

# Iterar y ejecutar ataque de cada personaje
for personaje in personajes:
    personaje.atacar()
