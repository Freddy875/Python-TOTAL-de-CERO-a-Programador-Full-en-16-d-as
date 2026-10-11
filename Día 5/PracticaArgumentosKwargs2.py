# Definir la función que devuelve una lista con los valores de los atributos
def lista_atributos(**kwargs):
    return list(kwargs.values())  # Extrae los valores y los convierte en lista

# Ejemplo de uso
print(lista_atributos(nombre="Carlos", edad=25, ciudad="Madrid"))  
# Salida: ['Carlos', 25, 'Madrid']

print(lista_atributos(a=10, b=20, c=30))  
# Salida: [10, 20, 30]

print(lista_atributos())  
# Salida: []
    