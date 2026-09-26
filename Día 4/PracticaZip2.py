# ------------------------------------------------------------
# Práctica Zip 2
# Crea un objeto zip a partir de una lista de marcas
# y una lista de productos.
# El objeto se almacena en la variable mi_zip.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Listas de marcas y productos.
# Cada marca se relacionará con el producto que ocupa
# la misma posición en la lista.
# ------------------------------------------------------------

marcas = ["Nike", "Apple", "Samsung", "Adidas", "Sony"]
productos = ["Zapatillas", "iPhone", "Televisor", "Camiseta", "PlayStation"]

# ------------------------------------------------------------
# Crear el objeto zip.
# zip() combina cada marca con el producto que se encuentra
# en la misma posición.
# ------------------------------------------------------------

mi_zip = zip(marcas, productos)

# ------------------------------------------------------------
# list() convierte el objeto zip en una lista de tuplas.
# Cada tupla contiene una marca y su producto correspondiente.
# ------------------------------------------------------------

print(list(mi_zip))