# ------------------------------------------------------------
# Práctica Return 2
# Crear una función llamada usd_a_eur que reciba como único
# parámetro un monto en dólares y devuelva su equivalente
# en euros.
# Para esta práctica se utiliza la conversión:
# 1 USD = 0.90 EUR.
# También se debe crear una variable llamada dolares y
# utilizarla para evaluar el resultado de la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función para convertir USD a EUR
# Recibe el monto en dólares mediante el parámetro dolares.
# Multiplica el monto por 0.90 para obtener su equivalente
# en euros y devuelve el resultado con return.
# ------------------------------------------------------------

def usd_a_eur(dolares):
    return dolares * 0.90  # Conversión a euros


# ------------------------------------------------------------
# Crear la variable con un monto en dólares
# Se almacena el valor 100 en la variable dolares.
# ------------------------------------------------------------

dolares = 100  # Puedes cambiar este valor


# ------------------------------------------------------------
# Calcular el monto en euros
# Se llama a la función usd_a_eur() y se le entrega la
# variable dolares como argumento.
# El resultado que devuelve return se guarda en euros.
# ------------------------------------------------------------

euros = usd_a_eur(dolares)


# ------------------------------------------------------------
# Imprimir el resultado
# Se muestra el monto original en dólares y su equivalente
# en euros.
# ------------------------------------------------------------

print(f"{dolares} USD equivalen a {euros} EUR")