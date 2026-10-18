# ------------------------------------------------------------
# Bucle while básico
#
# Se utiliza while para repetir una acción mientras la
# condición sea verdadera.
# ------------------------------------------------------------

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1

else:
    print("Ya no tienes más monedas")


# ------------------------------------------------------------
# while para repetir una pregunta
#
# El bucle continúa mientras el usuario responda "s".
# ------------------------------------------------------------

respuesta = "s"

while respuesta == "s":
    respuesta = input("¿Quieres seguir? (s/n): ")

else:
    print("Adiós")


# ------------------------------------------------------------
# pass
#
# pass permite dejar un bloque sin ninguna acción.
# En este ejemplo se utiliza cuando una tarea no tiene
# una acción definida.
# ------------------------------------------------------------

print("\n--- PASS ---")

tareas = ["estudiar", "comprar comida", "hacer ejercicio"]

for tarea in tareas:
    if tarea == "comprar comida":
        pass
    else:
        print(f"Realizar tarea: {tarea}")


# ------------------------------------------------------------
# break
#
# break interrumpe completamente el bucle.
# En este ejemplo, el recorrido termina cuando se encuentra
# a María.
# ------------------------------------------------------------

print("\n--- BREAK ---")

personas = ["Ana", "Carlos", "Luis", "María", "Pedro"]

for persona in personas:
    print(f"Buscando a {persona}...")

    if persona == "María":
        print("¡Encontré a María!")
        break


# ------------------------------------------------------------
# continue
#
# continue salta la iteración actual y continúa con la
# siguiente.
# En este ejemplo, se salta a Luis y continúa con María.
# ------------------------------------------------------------

print("\n--- CONTINUE ---")

personas = ["Ana", "Carlos", "Luis", "María"]

for persona in personas:
    if persona == "Luis":
        continue

    print(f"Hola {persona}")