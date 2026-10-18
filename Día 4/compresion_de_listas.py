# ------------------------------------------------------------
# Crear una lista recorriendo un string
# Recorre cada letra de la palabra y la agrega a una lista.
# ------------------------------------------------------------

palabra = "python"

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)


# ------------------------------------------------------------
# Otra forma de hacerlo
# Utiliza una comprensión de listas para recorrer cada letra
# de la palabra y crear directamente una lista.
# ------------------------------------------------------------

palabra2 = "python"

lista2 = [letra for letra in palabra2]

print(lista2)


# ------------------------------------------------------------
# Una tercera forma
# Crea una lista recorriendo directamente el string "python"
# mediante una comprensión de listas.
# ------------------------------------------------------------

lista3 = [letra for letra in "python"]

print(lista3)


# ------------------------------------------------------------
# Crear una lista utilizando range()
# Genera los números desde 0 hasta 20, avanzando de 2 en 2.
# La comprensión de listas almacena cada número generado.
# ------------------------------------------------------------

lista4 = [numero for numero in range(0, 21, 2)]

print(lista4)


# ------------------------------------------------------------
# Modificar los datos
# Recorre los números generados por range() y multiplica
# cada número por 2 antes de almacenarlo en la lista.
# ------------------------------------------------------------

lista4 = [numero * 2 for numero in range(0, 21, 2)]

print(lista4)


# ------------------------------------------------------------
# Usando if para elegir números
# Recorre los números de 0 a 20 de 2 en 2.
# Solo incluye los números cuyo resultado al multiplicarlos
# por 2 sea mayor que 10.
# ------------------------------------------------------------

lista5 = [numero for numero in range(0, 21, 2) if numero * 2 > 10]

print(lista5)


# ------------------------------------------------------------
# Usando un else
# Si el número multiplicado por 2 es mayor que 10,
# se agrega el número.
# Si no se cumple la condición, se agrega "no".
# ------------------------------------------------------------

lista6 = [numero if numero * 2 > 10 else "no" for numero in range(0, 21, 2)]

print(lista6)


# ------------------------------------------------------------
# Transformar pies en metros
# Recorre la lista de pies y convierte cada valor a metros.
# El resultado de cada conversión se almacena en una nueva lista.
# ------------------------------------------------------------

pies = [10, 20, 30, 40, 50]

metros = [pie / 3.281 for pie in pies]

print(metros)
