# ==================================================
# Práctica: Proyecto del Día 7 - Cuenta bancaria
# Objetivo: Crear un programa que le permita a una
# persona realizar operaciones en su cuenta bancaria:
# depositar y retirar dinero tantas veces como quiera,
# hasta que decida salir, sin poder retirar más dinero
# del que posee.
# ==================================================


# --------------------------------------------------
# Definir la clase Persona
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula.
# Una instancia es el objeto en sí, creado a partir
# del molde; en esta clase, cada instancia es una
# persona con sus propios valores en los atributos.
# Atributos de clase: ninguno.
# Atributos de instancia: nombre y apellido.
# Instancias: no se crean directamente; la clase sirve
# de base para la clase Cliente
# --------------------------------------------------
class Persona():
    """Clase que representa a una persona."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta al crear una instancia; recibe los
    # valores iniciales y los guarda como atributos de
    # instancia, es decir, atributos que son propios de
    # cada persona: nombre y apellido
    # ----------------------------------------------
    def __init__(self, nombre, apellido):
        """Inicializa la persona.

        Parámetros:
            nombre: nombre de la persona (texto).
            apellido: apellido de la persona (texto).
        """
        self.nombre = nombre
        self.apellido = apellido


# --------------------------------------------------
# Definir la clase Cliente
# Hereda de Persona, porque los clientes son personas;
# por eso recibe los atributos nombre y apellido, y
# además tiene atributos propios.
# En esta clase, cada instancia es un cliente con su
# propia cuenta bancaria.
# Atributos de clase: ninguno.
# Atributos de instancia: nombre y apellido (heredados
# de Persona), numero_cuenta y balance (propios).
# Instancias: se crea una más adelante, llamada cliente
# --------------------------------------------------
class Cliente(Persona):
    """Clase que representa a un cliente del banco."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta al crear una instancia; super() llama
    # al constructor de Persona para guardar nombre y
    # apellido, y después se guardan los atributos
    # propios del cliente: numero_cuenta y balance
    # (el saldo que tiene en su cuenta bancaria)
    # ----------------------------------------------
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        """Inicializa el cliente.

        Parámetros:
            nombre: nombre del cliente (texto).
            apellido: apellido del cliente (texto).
            numero_cuenta: número de la cuenta bancaria (texto).
            balance: saldo inicial de la cuenta (decimal).
        """
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # ----------------------------------------------
    # Método especial: __str__()
    # Se ejecuta automáticamente al imprimir una
    # instancia con print(); devuelve todos los datos
    # del cliente, incluyendo el balance, por ejemplo:
    # Cliente: Fernando Sánchez
    # Número de cuenta: 12345
    # Balance: $0
    # ----------------------------------------------
    def __str__(self):
        """Devuelve la representación del cliente en texto.

        Devuelve:
            Un texto con el nombre, el apellido, el número de
            cuenta y el balance del cliente (texto).
        """
        return (f"Cliente: {self.nombre} {self.apellido}\n"
                f"Número de cuenta: {self.numero_cuenta}\n"
                f"Balance: ${self.balance}")

    # ----------------------------------------------
    # Método depositar
    # Suma al balance la cantidad de dinero que el
    # cliente quiere agregar a su cuenta e imprime:
    # Depósito realizado
    # ----------------------------------------------
    def depositar(self, monto_deposito):
        """Agrega dinero a la cuenta del cliente.

        Parámetros:
            monto_deposito: cantidad de dinero a depositar (decimal).
        """
        self.balance += monto_deposito
        print("Depósito realizado")

    # ----------------------------------------------
    # Método retirar
    # Resta del balance la cantidad de dinero que el
    # cliente quiere sacar de su cuenta e imprime:
    # Retiro realizado
    # Si el monto es mayor que el balance, no se hace
    # el retiro e imprime:
    # Fondos insuficientes
    # ----------------------------------------------
    def retirar(self, monto_retiro):
        """Saca dinero de la cuenta del cliente.

        Parámetros:
            monto_retiro: cantidad de dinero a retirar (decimal).
        """
        if self.balance >= monto_retiro:  # Verifica que el dinero alcance
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


# --------------------------------------------------
# Definir la función para crear al cliente
# Pide al usuario su nombre, su apellido y su número
# de cuenta, y los guarda como texto en las variables
# nombre_cliente, apellido_cliente y numero_cuenta;
# con esos datos crea la variable cliente, que es la
# instancia de la clase Cliente, con un balance inicial
# de 0, y return devuelve el cliente ya creado
# --------------------------------------------------
def crear_cliente():
    """Crea un cliente con los datos que ingresa el usuario.

    Devuelve:
        Una instancia de la clase Cliente con balance 0 (Cliente).
    """
    nombre_cliente = input("Ingrese su nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta, 0)
    return cliente


# --------------------------------------------------
# Definir la función que organiza el programa
# Llama a crear_cliente() y guarda la instancia en la
# variable mi_cliente; después imprime sus datos.
# La variable opcion guarda lo que elige el usuario y
# comienza en 0; while repite el menú mientras opcion
# sea diferente de "S", es decir, hasta que el usuario
# decida salir.
# Con "D" se pide el monto y se llama a depositar();
# con "R" se pide el monto y se llama a retirar(); el
# monto se convierte a decimal con float().
# Después de cada operación se imprime el cliente para
# mostrar su balance actualizado
# --------------------------------------------------
def inicio():
    """Organiza la ejecución de todo el programa."""
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != "S":
        print("Elija: Depositar (D), Retirar (R) o Salir (S)")
        opcion = input()

        if opcion == "D":
            monto_deposito = float(input("Monto a depositar: "))  # Cantidad ingresada por el usuario
            mi_cliente.depositar(monto_deposito)
        elif opcion == "R":
            monto_retiro = float(input("Monto a retirar: "))  # Cantidad ingresada por el usuario
            mi_cliente.retirar(monto_retiro)

        print(mi_cliente)

    print("Gracias por operar en Banco Python")


# --------------------------------------------------
# Iniciar el programa
# Se llama a la función inicio() para ejecutar todo.
# Si el usuario escribe Fernando, Sánchez y 12345,
# deposita 500, retira 200 y sale, imprime al final:
# Cliente: Fernando Sánchez
# Número de cuenta: 12345
# Balance: $300.0
# Gracias por operar en Banco Python
# --------------------------------------------------
inicio()
