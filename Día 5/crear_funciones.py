def  saludar_persona():
    # Esta función es para saludar a la persona
    print("Hola mundo")

saludar_persona()

def saludar_persona(nombre):
    # Esta función recibe un nombre y muestra un saludo.
    print(f"Hola, {nombre}!")


nombre = input("¿Cuál es tu nombre? ")

saludar_persona(nombre)