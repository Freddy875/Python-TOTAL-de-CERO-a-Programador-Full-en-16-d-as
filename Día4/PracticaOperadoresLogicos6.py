# Definir la frase y las palabras

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

# Verificar si ambas palabras están en la frase

mi_bool = palabra1 in frase and palabra2 in frase

# Mostrar la información al usuario

print("\nFrase:")
print(frase)

print(f"\nPrimera palabra: {palabra1}")
print(f"Segunda palabra: {palabra2}")

if mi_bool:
    print("\nLas dos palabras se encuentran en la frase.")
else:
    print("\nNo se encuentran las dos palabras en la frase.")