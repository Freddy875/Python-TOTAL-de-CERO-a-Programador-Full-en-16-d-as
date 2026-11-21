# ==================================================
# Práctica: Librería Rich - Control de gastos del mes
# Objetivo: Crear un programa que le permita a una
# persona registrar sus gastos del mes, verlos en una
# tabla ordenada y revisar cuánto le queda de su
# presupuesto, usando la librería Rich para mostrar
# tablas, paneles, colores y una barra de avance que
# indica qué porcentaje del presupuesto ya se gastó.
# ==================================================


# --------------------------------------------------
# Importar la librería Rich
# Rich es una librería externa (se instala con
# pip install rich) que permite mostrar en la consola
# texto con colores y estilos, tablas, paneles y
# barras de progreso.
# Console: es la consola de Rich; su método print()
# entiende etiquetas como [bold green]texto[/], que
# ponen el texto en negritas y verde.
# Table: crea tablas con columnas y filas.
# Panel: dibuja un recuadro alrededor de un texto.
# ProgressBar: dibuja una barra de avance.
# Prompt, FloatPrompt: piden datos al usuario; Prompt
# puede limitar las respuestas con choices, y
# FloatPrompt solo acepta números decimales.
# Group: junta varios elementos para mostrarlos juntos
# --------------------------------------------------
from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.prompt import Prompt, FloatPrompt

consola = Console()


# --------------------------------------------------
# Definir las constantes del programa
# CATEGORIAS: lista con los tipos de gasto permitidos.
# COLORES_CATEGORIA: diccionario que asigna un color de
# Rich a cada categoría, para distinguirlas en la tabla
# --------------------------------------------------
CATEGORIAS = ["comida", "transporte", "servicios", "diversion", "otros"]

COLORES_CATEGORIA = {
    "comida": "green",
    "transporte": "cyan",
    "servicios": "yellow",
    "diversion": "magenta",
    "otros": "white",
}


# --------------------------------------------------
# Definir la clase Gasto
# Una clase es un molde que sirve para crear objetos.
# En esta clase, cada instancia es un gasto.
# Atributos de instancia: descripcion, categoria y
# monto.
# Instancias: se crean en la función agregar_gasto()
# --------------------------------------------------
class Gasto():
    """Clase que representa un gasto."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # Guarda la descripción (por ejemplo "Súper"), la
    # categoría (por ejemplo "comida") y el monto
    # ----------------------------------------------
    def __init__(self, descripcion, categoria, monto):
        """Inicializa el gasto.

        Parámetros:
            descripcion: en qué se gastó (texto).
            categoria: tipo de gasto (texto).
            monto: cantidad gastada (decimal).
        """
        self.descripcion = descripcion
        self.categoria = categoria
        self.monto = monto


# --------------------------------------------------
# Definir la clase Presupuesto
# Cada instancia es el presupuesto de un mes.
# Atributos de instancia: limite (dinero disponible
# para el mes) y gastos (lista de instancias de Gasto,
# que comienza vacía).
# Instancias: se crea una en la función inicio()
# --------------------------------------------------
class Presupuesto():
    """Clase que representa el presupuesto del mes."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # ----------------------------------------------
    def __init__(self, limite):
        """Inicializa el presupuesto.

        Parámetros:
            limite: dinero disponible para el mes (decimal).
        """
        self.limite = limite
        self.gastos = []

    # ----------------------------------------------
    # Método total_gastado
    # sum() suma los montos de todos los gastos; se usa
    # una expresión generadora que toma gasto.monto de
    # cada gasto de la lista
    # ----------------------------------------------
    def total_gastado(self):
        """Devuelve la suma de todos los gastos (decimal)."""
        return sum(gasto.monto for gasto in self.gastos)

    # ----------------------------------------------
    # Método disponible
    # Resta lo gastado al límite; si el resultado es
    # negativo, la persona se pasó del presupuesto
    # ----------------------------------------------
    def disponible(self):
        """Devuelve el dinero que queda del presupuesto (decimal)."""
        return self.limite - self.total_gastado()

    # ----------------------------------------------
    # Método total_por_categoria
    # Crea un diccionario con cada categoría en 0 y,
    # con for, suma cada gasto a su categoría.
    # Por ejemplo: {"comida": 850.0, "transporte": 200.0,
    # "servicios": 0, ...}
    # ----------------------------------------------
    def total_por_categoria(self):
        """Devuelve un diccionario con el total de cada categoría."""
        totales = {categoria: 0 for categoria in CATEGORIAS}
        for gasto in self.gastos:
            totales[gasto.categoria] += gasto.monto
        return totales


# --------------------------------------------------
# Definir la función para agregar un gasto
# Prompt.ask() pide la descripción; con choices solo
# acepta una de las CATEGORIAS y, si el usuario escribe
# otra cosa, Rich vuelve a preguntar automáticamente.
# FloatPrompt.ask() pide el monto y solo acepta
# números. Se crea la instancia de Gasto, se agrega a
# la lista del presupuesto y se imprime en verde:
# ✔ Gasto agregado: Súper por $850.00
# --------------------------------------------------
def agregar_gasto(presupuesto):
    """Pide los datos de un gasto y lo agrega al presupuesto.

    Parámetros:
        presupuesto: presupuesto del mes (Presupuesto).
    """
    descripcion = Prompt.ask("Descripción del gasto")
    categoria = Prompt.ask("Categoría", choices=CATEGORIAS, default="otros")
    monto = FloatPrompt.ask("Monto")

    if monto <= 0:  # No tiene sentido un gasto de 0 o negativo
        consola.print("[bold red]✖ El monto debe ser mayor que 0[/]")
        return

    presupuesto.gastos.append(Gasto(descripcion, categoria, monto))
    consola.print(f"[bold green]✔ Gasto agregado:[/] {descripcion} por ${monto:,.2f}")


# --------------------------------------------------
# Definir la función para mostrar los gastos
# Si la lista está vacía, avisa en amarillo.
# Si no, crea una Table con título y cuatro columnas;
# justify="right" alinea los montos a la derecha.
# enumerate(..., start=1) numera los gastos desde 1.
# Cada categoría se pinta con su color usando la
# etiqueta [color]texto[/color].
# Al final se agrega una fila con el TOTAL en negritas.
# Por ejemplo, muestra:
# ┏━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┓
# ┃ # ┃ Descripción ┃ Categoría  ┃     Monto ┃
# ┡━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━┩
# │ 1 │ Súper       │ comida     │   $850.00 │
# │   │ TOTAL       │            │   $850.00 │
# └───┴─────────────┴────────────┴───────────┘
# --------------------------------------------------
def mostrar_gastos(presupuesto):
    """Muestra todos los gastos en una tabla.

    Parámetros:
        presupuesto: presupuesto del mes (Presupuesto).
    """
    if not presupuesto.gastos:
        consola.print("[yellow]Todavía no hay gastos registrados[/]")
        return

    tabla = Table(title="Gastos del mes", header_style="bold cyan")
    tabla.add_column("#", style="dim")
    tabla.add_column("Descripción")
    tabla.add_column("Categoría")
    tabla.add_column("Monto", justify="right")

    for numero, gasto in enumerate(presupuesto.gastos, start=1):
        color = COLORES_CATEGORIA[gasto.categoria]
        tabla.add_row(str(numero), gasto.descripcion,
                      f"[{color}]{gasto.categoria}[/{color}]", f"${gasto.monto:,.2f}")

    tabla.add_section()  # Línea que separa los gastos del total
    tabla.add_row("", "[bold]TOTAL[/]", "", f"[bold]${presupuesto.total_gastado():,.2f}[/]")
    consola.print(tabla)


# --------------------------------------------------
# Definir la función para mostrar el resumen
# Calcula el porcentaje gastado del presupuesto y
# elige un color: verde si es menos del 70%, amarillo
# si está entre 70% y 100%, y rojo si se pasó.
# ProgressBar dibuja una barra; total es el 100% y
# completed es lo que se lleva gastado (min() evita
# que la barra se salga si se gastó de más).
# Group junta varios elementos (texto y barra) para
# meterlos en un mismo Panel, que es el recuadro;
# la barra va al final porque no termina con un salto
# de línea y taparía lo que viniera después.
# Después se muestra una tabla con el total gastado
# en cada categoría. Por ejemplo, muestra:
# ╭──────── Resumen ────────╮
# │ Presupuesto: $5,000.00  │
# │ Gastado:     $850.00    │
# │ Disponible:  $4,150.00  │
# │ 17.0% del presupuesto   │
# │ ━━━━━━━━━━━━━━━━━━━━━━━ │
# ╰─────────────────────────╯
# --------------------------------------------------
def mostrar_resumen(presupuesto):
    """Muestra un panel con el estado del presupuesto.

    Parámetros:
        presupuesto: presupuesto del mes (Presupuesto).
    """
    gastado = presupuesto.total_gastado()
    porcentaje = gastado / presupuesto.limite * 100

    if porcentaje < 70:
        color = "green"
    elif porcentaje <= 100:
        color = "yellow"
    else:
        color = "red"

    barra = ProgressBar(total=presupuesto.limite,
                        completed=min(gastado, presupuesto.limite),
                        complete_style=color)

    contenido = Group(
        f"Presupuesto: [bold]${presupuesto.limite:,.2f}[/]",
        f"Gastado:     [bold {color}]${gastado:,.2f}[/]",
        f"Disponible:  [bold]${presupuesto.disponible():,.2f}[/]",
        f"[{color}]{porcentaje:.1f}% del presupuesto[/]",
        barra,
    )
    consola.print(Panel(contenido, title="Resumen", border_style=color, width=45))

    if porcentaje > 100:
        consola.print("[bold white on red] ¡Cuidado! Te pasaste de tu presupuesto [/]")

    tabla = Table(title="Gasto por categoría")
    tabla.add_column("Categoría")
    tabla.add_column("Total", justify="right")

    for categoria, total in presupuesto.total_por_categoria().items():
        color_categoria = COLORES_CATEGORIA[categoria]
        tabla.add_row(f"[{color_categoria}]{categoria}[/]", f"${total:,.2f}")

    consola.print(tabla)


# --------------------------------------------------
# Definir la función que organiza el programa
# consola.rule() dibuja una línea con un título.
# Se pide el presupuesto del mes y se crea la
# instancia mi_presupuesto. while repite el menú hasta
# que el usuario elija "s"; Prompt.ask con choices
# solo acepta las letras del menú.
# Con "a" se agrega un gasto, con "g" se ven los
# gastos y con "r" se ve el resumen.
# Al salir, se muestra el resumen final
# --------------------------------------------------
def inicio():
    """Organiza la ejecución de todo el programa."""
    consola.rule("[bold cyan]Control de gastos del mes[/]")
    limite = FloatPrompt.ask("¿Cuál es tu presupuesto para este mes?")

    while limite <= 0:  # El presupuesto debe ser positivo
        consola.print("[red]El presupuesto debe ser mayor que 0[/]")
        limite = FloatPrompt.ask("¿Cuál es tu presupuesto para este mes?")

    mi_presupuesto = Presupuesto(limite)
    opcion = ""

    while opcion != "s":
        consola.print("\n[bold magenta]Agregar gasto (a) · Ver gastos (g) · Resumen (r) · Salir (s)[/]")
        opcion = Prompt.ask("Elija", choices=["a", "g", "r", "s"])

        if opcion == "a":
            agregar_gasto(mi_presupuesto)
        elif opcion == "g":
            mostrar_gastos(mi_presupuesto)
        elif opcion == "r":
            mostrar_resumen(mi_presupuesto)

    consola.rule("[bold cyan]Resumen final[/]")
    mostrar_resumen(mi_presupuesto)
    consola.print("[bold cyan]¡Hasta pronto! Cuida tu dinero 💰[/]")


# --------------------------------------------------
# Iniciar el programa
# Se llama a la función inicio() para ejecutar todo.
# Si el usuario escribe un presupuesto de 5000, agrega
# "Súper" en comida por 850 y sale, se muestra el
# panel de resumen con $4,150.00 disponibles, una
# barra verde al 17.0% y la tabla por categoría
# --------------------------------------------------
inicio()
