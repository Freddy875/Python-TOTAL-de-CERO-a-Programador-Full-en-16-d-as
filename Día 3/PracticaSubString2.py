# ------------------------------------------------------------
# Este programa utiliza slicing para extraer cada tercer
# carácter de la frase, comenzando desde el noveno carácter
# hasta el final.
#
# Se utiliza [8::3] porque Python comienza a contar los
# índices desde 0. Por eso, el noveno carácter corresponde
# al índice 8, y el salto 3 permite tomar cada tercer
# carácter.
# ------------------------------------------------------------

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

resultado = frase[8::3]

print(resultado)