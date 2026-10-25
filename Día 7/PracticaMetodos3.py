class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

# Crear una instancia de Alarma
mi_alarma = Alarma()

# Postergar la alarma
mi_alarma.postergar(10)
