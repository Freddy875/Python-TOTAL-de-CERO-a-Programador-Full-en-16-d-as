# ==================================================
# PRÁCTICA HERENCIA EXTENDIDA 2
# Objetivo: crear la clase Ornitorrinco con herencia
# múltiple, tomando sus métodos y atributos de Ave,
# Reptil, Pez y Mamifero.
# ==================================================


# --------------------------------------------------
# CLASE VERTEBRADO
# Clase base de todas las demás. Por eso cualquier
# animal que herede de ella ya es vertebrado.
# --------------------------------------------------
class Vertebrado:
    """Representa a un animal vertebrado."""

    # ------------------------------
    # Atributo de clase
    # vertebrado: indica que el animal tiene columna.
    # ------------------------------
    vertebrado = True


# --------------------------------------------------
# CLASE AVE
# Hereda de Vertebrado. Aporta el pico y la capacidad
# de poner huevos.
# --------------------------------------------------
class Ave(Vertebrado):
    """Representa a un ave, con pico y que pone huevos."""

    # ------------------------------
    # Atributo de clase
    # tiene_pico: indica que el animal tiene pico.
    # ------------------------------
    tiene_pico = True

    # ------------------------------
    # Método poner_huevos
    # Muestra que el ave pone huevos.
    # ------------------------------
    def poner_huevos(self):
        """Imprime que el animal está poniendo huevos.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Poniendo huevos")


# --------------------------------------------------
# CLASE REPTIL
# Hereda de Vertebrado. Aporta el veneno.
# --------------------------------------------------
class Reptil(Vertebrado):
    """Representa a un reptil venenoso."""

    # ------------------------------
    # Atributo de clase
    # venenoso: indica que el animal tiene veneno.
    # ------------------------------
    venenoso = True


# --------------------------------------------------
# CLASE PEZ
# Hereda de Vertebrado. Aporta la capacidad de nadar y
# también pone huevos.
# --------------------------------------------------
class Pez(Vertebrado):
    """Representa a un pez, que nada y pone huevos."""

    # ------------------------------
    # Método nadar
    # Muestra que el pez está nadando.
    # ------------------------------
    def nadar(self):
        """Imprime que el animal está nadando.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Nadando")

    # ------------------------------
    # Método poner_huevos
    # Muestra que el pez pone huevos.
    # ------------------------------
    def poner_huevos(self):
        """Imprime que el animal está poniendo huevos.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Poniendo huevos")


# --------------------------------------------------
# CLASE MAMIFERO
# Hereda de Vertebrado. Aporta caminar y amamantar.
# --------------------------------------------------
class Mamifero(Vertebrado):
    """Representa a un mamífero, que camina y amamanta."""

    # ------------------------------
    # Método caminar
    # Muestra que el mamífero está caminando.
    # ------------------------------
    def caminar(self):
        """Imprime que el animal está caminando.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Caminando")

    # ------------------------------
    # Método amamantar
    # Muestra que el mamífero amamanta a sus crías.
    # ------------------------------
    def amamantar(self):
        """Imprime que el animal está amamantando a sus crías.

        Parámetros:
            self: instancia de la clase.

        Devuelve:
            None. Solo imprime el mensaje.
        """
        print("Amamantando crías")


# --------------------------------------------------
# CLASE ORNITORRINCO
# Usa herencia múltiple para reunir lo que aportan
# Ave, Reptil, Pez y Mamifero. Python busca en este
# orden: Ornitorrinco, Ave, Reptil, Pez, Mamifero y
# Vertebrado. Ave y Pez tienen poner_huevos(), pero se
# usa el de Ave porque va primero.
# --------------------------------------------------
class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    """Representa a un ornitorrinco con herencia múltiple."""
    pass


# --------------------------------------------------
# PRUEBA DE LOS ATRIBUTOS Y MÉTODOS
# Crea un ornitorrinco y comprueba todo lo que heredó.
# Variables:
#   perry: objeto de la clase Ornitorrinco.
# Resultado esperado:
#   Tiene pico: True
#   Es vertebrado: True
#   Es venenoso: True
#   Poniendo huevos
#   Nadando
#   Caminando
#   Amamantando crías
# --------------------------------------------------
perry = Ornitorrinco()

print("Tiene pico:", perry.tiene_pico)
print("Es vertebrado:", perry.vertebrado)
print("Es venenoso:", perry.venenoso)

perry.poner_huevos()
perry.nadar()
perry.caminar()
perry.amamantar()