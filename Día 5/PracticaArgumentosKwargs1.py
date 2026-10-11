# Definir la función para contar los atributos pasados como argumentos nombrados
def cantidad_atributos(**kwargs):
    return len(kwargs)  # Devuelve la cantidad de claves en el diccionario kwargs

# Ejemplo de uso
print(cantidad_atributos(nombre="Juan", edad=30, ciudad="Madrid"))  # Salida: 3
print(cantidad_atributos(a=1, b=2))  # Salida: 2
print(cantidad_atributos())  # Salida: 0
