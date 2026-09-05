var1 = True
var2 = False

### Asignación de valores de forma explicita

print(type(var1)) ### Indica el tipo de dato de la variable var1
print(var1) ### Imprime el valor de la variable var1

### Otra forma de crear variables booleanas

numero = 5 > 5
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Ahora si es menor que 5
numero = 5 < 5
print(type(numero)) ### Indica el tipo de dato de la variable numero    
print(numero) ### Imprime el valor de la variable numero

### Si es igual a 5
numero = 5 == 5
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Preguntar si es mayor o igual a 5
numero = 5 >= 5
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Preguntar si es menor o igual a 5
numero = 5 <= 5
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Preguntar si es diferente a 5
numero = 5 != 3
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Asignación de valores de forma explicita

numero = bool(5 != 3)
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Generar un valor falso
numero = bool()
print(type(numero)) ### Indica el tipo de dato de la variable numero
print(numero) ### Imprime el valor de la variable numero

### Preguntar si algo es verdadero o falso
lista = [1, 2, 3, 4, 5]
control = 5 in lista
print(type(control)) ### Indica el tipo de dato de la variable control
print(control) ### Imprime el valor de la variable control

### Preguntar si algo es verdadero o falso
lista = [1, 2, 3, 4, 5]
print(3 in lista) ### Imprime el valor de la variable control

### Caso contrario si no esta en la lista
lista = [1, 2, 3, 4, 5]
print(6 not in lista) ### Imprime el valor de la variable control

