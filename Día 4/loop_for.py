# ------------------------------------------------------------
# Crear una lista de nombres
#
# Se almacenan los nombres de las personas dentro de una lista.
# ------------------------------------------------------------

nombres = ["Juan", "Ana", "Carlos", "Belen", "Fran"]


# ------------------------------------------------------------
# Recorrer la lista
#
# for recorre cada elemento de la lista y almacena
# temporalmente cada nombre en la variable nombre.
# ------------------------------------------------------------

for nombre in nombres:
    print(f"Hola {nombre}")

mi_lista = ["a", "b", "c"]
for letra in mi_lista:
    print(f"Elemento: {letra}")

print("Agregar un elemento a la lista")

mi_lista.append("d")
for letra in mi_lista:
    numero_letra =mi_lista.index(letra)
    print(f"La letra: {letra} tiene el indice {numero_letra}")

### Agregar elementos a la lista de nombres
nombres.extend(["Luis","Pablo","Laura","Julia"])

print(type(nombres))

### Imprimir solo nombres que empiecen con L

for nombre in nombres:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print(f"Este nombre {nombre} no comienza con L")

numeros = [1,2,3,4,5]

valor = 0

for numero in numeros:
    valor = valor + numero

print(valor)

palabra = "python es genial"

print("\n")

for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print("\n")

libros = {
    1: "El principito",
    2: "Don Quijote de la Mancha",
    3: "Cien años de soledad",
    4: "Orgullo y prejuicio",
    5: "Crimen y castigo"
}

for a, b in libros.items():
    print(a)
    print(b)
