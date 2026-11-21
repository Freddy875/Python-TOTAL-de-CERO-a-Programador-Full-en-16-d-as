from mi_paquete import suma_resta
from mi_subpaquete import saludar

saludar.saludar()  # Llama a la función saludar del módulo saludar.py

# Solicita al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Llama a la función suma y muestra el resultado
resultado_suma = suma_resta.suma(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {resultado_suma}")

# Llama a la función resta y muestra el resultado
resultado_resta = suma_resta.resta(numero1, numero2)
print(f"La resta de {numero1} y {numero2} es: {resultado_resta}")
