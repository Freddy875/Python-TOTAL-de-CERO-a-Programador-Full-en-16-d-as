# ------------------------------------------------------------
# Este programa utiliza el método pop() para eliminar el
# tercer elemento de la lista. Como Python comienza a contar
# los índices desde 0, el tercer elemento corresponde al
# índice 2. El elemento eliminado se guarda en la variable
# "eliminado".
# ------------------------------------------------------------

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

# Eliminamos el tercer elemento y guardamos su valor.
eliminado = frutas.pop(2)

# Mostramos el elemento eliminado y la lista actualizada.
print(f"Elemento eliminado: {eliminado}")
print(f"Lista actualizada: {frutas}")