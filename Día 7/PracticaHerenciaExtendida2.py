class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

# Clase Ornitorrinco usando herencia múltiple
class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass

# Crear una instancia de Ornitorrinco
perry = Ornitorrinco()

# Probar los métodos y atributos
print("Tiene pico:", perry.tiene_pico)
print("Es vertebrado:", perry.vertebrado)
print("Es venenoso:", perry.venenoso)

perry.poner_huevos()
perry.nadar()
perry.caminar()
perry.amamantar()