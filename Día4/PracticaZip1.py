# ------------------------------------------------------------
# Práctica Zip 1
# Muestra una frase indicando la capital de cada país.
# Utiliza zip() para combinar los países con sus capitales
# y un loop for para recorrerlos.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Listas de capitales y países.
# Cada país y su capital ocupan la misma posición
# en sus respectivas listas.
# ------------------------------------------------------------

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# ------------------------------------------------------------
# Loop con zip()
# zip() empareja cada país con la capital que se encuentra
# en la misma posición.
# En cada vuelta, los valores se guardan en pais y capital.
# ------------------------------------------------------------

for pais, capital in zip(paises, capitales):

    # Imprime el país junto con su capital correspondiente.
    print(f"La capital de {pais} es {capital}")