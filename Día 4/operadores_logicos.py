### Comparar dos operadores logicos
mi_bool = 4 < 5 < 6
print(mi_bool)  # Esto imprimirá True porque 4 es menor que 5 y 5 es menor que 6

mi_bool = 4 < 5 > 6
print(mi_bool)  # Esto imprimirá False porque 4 es menor que 5 pero 5 no es mayor que 6

### Comparar con operador AND
mi_bool = 4 < 5 and 5 < 6
print(mi_bool)  # Esto imprimirá True porque ambas condiciones son verdaderas

### cambiar las condiciones. Recomendable usar parentesis
mi_bool = (4 < 5) and (5 == 2 * 3)
print(mi_bool)  # Esto imprimirá False porque 4 es menor que 5 pero 5 no es igual a 2 * 3

### Doble comparación 
mi_bool = (55 == 55) and ("gato" == "gato")
print(mi_bool)  # Esto imprimirá True porque ambas condiciones son verdaderas

### Comparar con operador OR
mi_bool = 10 == 5 or 3 < 6
print(mi_bool)  # Esto imprimirá True porque la segunda condición es verdadera

### Comparar con operador OR
mi_bool = 10 == 5 or 3 == 6
print(mi_bool)  # Esto imprimirá False porque ninguna de las condiciones es verdadera

### Comparar con texto

texto = "Esta frase es breve"

mi_bool = "frase" in texto and "breve" in texto
print(mi_bool)  # Esto imprimirá True porque ambas palabras están en el texto

mi_bool = "frase" in texto and "Hola" in texto
print(mi_bool)  # Esto imprimirá False porque la segunda palabra no está en el texto

mi_bool = "frase" in texto or "Hola" in texto
print(mi_bool)  # Esto imprimirá True porque la primera palabra está en el texto

### Operador not
mi_bool = not ("a" == "a")
print(mi_bool)  # Esto imprimirá False porque "a" es igual a "a", y el operador not invierte el resultado

mi_bool = not ("a" != "a")
print(mi_bool)  # Esto imprimirá True porque "a" es igual a "a", y el operador not invierte el resultado
