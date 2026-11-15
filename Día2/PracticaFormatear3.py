# ------------------------------------------------------------
# Este programa declara dos variables para almacenar los
# puntos acumulados anteriormente y los puntos nuevos
# obtenidos por un usuario. Luego, calcula el total de
# puntos sumando ambos valores y muestra un mensaje
# personalizado utilizando una f-string.
# ------------------------------------------------------------

puntos_anteriores = 875
puntos_nuevos = 350

# Calculamos el total de puntos acumulados.
puntos_totales = puntos_anteriores + puntos_nuevos

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")