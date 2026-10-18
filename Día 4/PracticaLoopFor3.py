# ------------------------------------------------------------
# Práctica Loop For 3
#
# Dada una lista de números, utiliza un loop For para realizar
# por separado la suma de los números pares e impares.
#
# El resultado de los números pares debe almacenarse en
# suma_pares y el de los números impares en suma_impares.
#
# Para identificar cada tipo de número se utiliza el módulo:
#
# num % 2 == 0 → número par
# num % 2 == 1 → número impar
# ------------------------------------------------------------


# ------------------------------------------------------------
# Crear la lista de números
#
# Se almacenan los números que serán recorridos para
# clasificarlos como pares o impares.
# ------------------------------------------------------------

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]


# ------------------------------------------------------------
# Crear las variables para almacenar las sumas
#
# Ambas variables comienzan en 0 y se utilizarán para
# acumular por separado los números pares e impares.
# ------------------------------------------------------------

suma_pares = 0
suma_impares = 0


# ------------------------------------------------------------
# Recorrer la lista y clasificar los números
#
# for recorre cada número de lista_numeros y lo almacena
# temporalmente en la variable num.
#
# El operador % obtiene el resto de una división.
# Si el resto de dividir num entre 2 es 0, el número es par.
# Si no es par, se considera impar.
# ------------------------------------------------------------

for num in lista_numeros:

    if num % 2 == 0:  # Verifica si el número es par
        suma_pares += num

    else:  # Si no es par, es impar
        suma_impares += num


# ------------------------------------------------------------
# Imprimir los resultados
#
# Se muestran por separado las sumas de los números pares
# y de los números impares.
# ------------------------------------------------------------

print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")