# ------------------------------------------------------------
# Este programa utiliza el método replace() para sustituir
# las palabras "difícil" por "fácil" y "mala" por "buena"
# dentro de la frase. Los reemplazos se realizan de forma
# consecutiva y el resultado se muestra en pantalla.
# ------------------------------------------------------------

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

# Reemplazamos las dos palabras indicadas.
frase_modificada = frase.replace("difícil", "fácil").replace("mala", "buena")

print(frase_modificada)