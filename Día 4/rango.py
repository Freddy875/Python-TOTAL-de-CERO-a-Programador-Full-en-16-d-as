lista_numerica = [1, 2, 3, 4, 5]

for numero in lista_numerica:
    print(numero)

print("\n")

### No se incluye el número dentro de parentesis, siempre empizan con cero si no se especifica el final
for numero in range(5):
    print(numero)

print("\n")

### Estableer donde empieza y termina el rango

for numero in range(10,21):
    print(numero)

### Un tercer elemento en range que son los pasos es decir si quieres que vaya saltando números si no se pone nada por defecto es 1

print("\n")

for numero in range(10,21,3):
    print(numero)


mi_lista = list(range(1,101))

print(mi_lista)
