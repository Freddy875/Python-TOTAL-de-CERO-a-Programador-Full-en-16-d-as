### Bucle básico 

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas}  monedas")
    monedas = monedas -1

### Otra forma economica de escribirlo

print("\n")

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas}  monedas")
    monedas -= 1
else:
    print("Ya no tienes más monedas")

respuesta = "s"

while respuesta == "s":
    respuesta = input("¿Quieres seguir? (s/n): ")
else:
    print("Adios")

### Palabras clave pass

while respuesta == "s":
    pass

print("Adios")

### Break para interumpir el flujo

nombre = input("Ingree su nombre: ")

for letra in nombre:
    if letra == "n":
        break
    print(letra)

### Continue

nombre = input("Ingree su nombre: ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)

