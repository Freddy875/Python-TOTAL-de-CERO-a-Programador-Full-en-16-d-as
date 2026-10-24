# Guía de estilo: cómo documento mi código en Python

Esta guía describe cómo comento mis programas en Python. Primero escribo el programa y después le agrego los comentarios con este formato. Todo está documentado en **español**.

**Regla de oro:** documentar no cambia el código. Los comentarios se agregan sin modificar el código original; el código solo se cambia cuando se pide de forma explícita.

---

## 1. Encabezado del archivo

Va al inicio del archivo. Usa un bloque de `=` (50 caracteres) con dos datos: el **título de la práctica** y el **objetivo**.

```python
# ==================================================
# Práctica: Atributos 3
# Objetivo: Crear una clase llamada Personaje con el
# atributo de clase real (igual a False) y los atributos
# de instancia especie, magico y edad, y mostrar su
# descripción con un método.
# ==================================================
```

Reglas:

- Primera línea: `Práctica: <nombre>`.
- Después: `Objetivo: <qué debe lograr el programa>`.
- El objetivo puede ocupar varias líneas.

---

## 2. Bloques de sección

Cada sección del programa va en **un solo bloque**, con esta estructura:

1. Línea de `-` arriba (50 caracteres).
2. **Título** de la sección.
3. **Descripción** de lo que hace.
4. Línea de `-` abajo.

Después del bloque va el código de esa sección.

```python
# --------------------------------------------------
# Abrir el archivo en modo escritura
# Se usa el modo "w" para reemplazar el contenido
# anterior del archivo
# --------------------------------------------------
mi_archivo = open("mi_archivo.txt", "w")
```

Reglas:

- **No repetir el título.** Si el título del bloque ya dice qué hace la sección, no se escribe otro comentario con lo mismo.
- Los comentarios explicativos van **dentro** del bloque, no sueltos antes ni después.
- Entre bloques se deja una línea en blanco.

---

## 3. Variables

Las variables se documentan en el bloque de la sección, **antes del código**. Se explica qué es cada variable y para qué se usa.

```python
# --------------------------------------------------
# Crear las variables para almacenar las sumas
# Ambas variables comienzan en 0 y se utilizarán para
# acumular por separado los números pares e impares
# --------------------------------------------------
suma_pares = 0
suma_impares = 0
```

---

## 4. Funciones

Una función se documenta de dos formas a la vez:

- **Bloque de sección** antes de la función: qué hace y cómo se usa.
- **Docstring** dentro de la función, con `Parámetros` y `Devuelve`.

```python
# --------------------------------------------------
# Definir la función para convertir USD a EUR
# Recibe el monto en dólares y lo multiplica por 0.90;
# return devuelve el resultado de la conversión
# --------------------------------------------------
def usd_a_eur(dolares):
    """Convierte un monto en dólares a euros.

    Parámetros:
        dolares: monto en dólares (decimal).

    Devuelve:
        El monto equivalente en euros (decimal).
    """
    return dolares * 0.90
```

---

## 5. Clases, atributos y métodos

- **Bloque de sección** antes de la clase (por ejemplo, qué es una clase y la convención del nombre).
- **Docstring** en la clase y en cada método.
- Dentro de la clase, cada atributo y cada método lleva su propio **bloque con guiones más cortos** (46 caracteres), con la misma estructura: línea, título, descripción, línea.

```python
# --------------------------------------------------
# Definir la clase Personaje
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula
# --------------------------------------------------
class Personaje:
    """Clase que representa a un personaje."""

    # ----------------------------------------------
    # Atributo de clase
    # real vale False para todos los personajes: se
    # define dentro de la clase, fuera de los métodos,
    # y lo comparten todas las instancias
    # ----------------------------------------------
    real = False

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta al crear un objeto; recibe los valores
    # iniciales y los guarda como atributos
    # ----------------------------------------------
    def __init__(self, especie, edad):
        """Inicializa el personaje.

        Parámetros:
            especie: especie del personaje (texto).
            edad: edad del personaje (entero).
        """
        self.especie = especie
        self.edad = edad
```

---

## 6. Ciclos `for` y bloques `with`

Los ciclos y los bloques `with` se explican **dentro del bloque de la sección**: qué se recorre (o qué se abre) y qué variable guarda cada elemento.

### Nombres en los ciclos `for`

Siempre voy **de la cantidad grande a la chica**: el nombre de la colección va en plural y el de cada elemento en singular.

```python
for letra in letras:
for numero in numeros:
for nombre in nombres:
```

```python
# --------------------------------------------------
# Recorrer la lista de nombres
# for recorre cada elemento de la lista y almacena
# temporalmente cada nombre en la variable nombre
# --------------------------------------------------
for nombre in nombres:
    print(f"Hola {nombre}")
```

### Bloques `with`

```python
# --------------------------------------------------
# Leer el archivo
# with abre el archivo en modo lectura ("r") y lo
# cierra automáticamente al terminar el bloque
# --------------------------------------------------
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
```

---

## 7. Resultado esperado o resultado final

El resultado esperado se escribe **dentro del bloque de la sección**, indicando lo que imprime el programa.

```python
# --------------------------------------------------
# Usar el método para describir al personaje
# Se llama al método con la instancia; imprime:
# Este personaje es un Humano, mágico, tiene 17 años
# y es real: False.
# --------------------------------------------------
harry_potter.describir()
```

---

## 8. Comentarios cortos en línea

Para aclarar algo puntual se usa un **comentario normal de una línea**, sin bloque.

```python
dolares = float(input("¿Cuántos dólares? "))  # Cantidad ingresada por el usuario

if num % 2 == 0:  # Verifica si el número es par
    suma_pares += num
```

---

## 9. Resumen rápido

| Elemento | Cómo se documenta |
|---|---|
| Encabezado | Bloque de `=` con `Práctica:` y `Objetivo:` |
| Sección | Bloque de `-` con título y descripción |
| Variables | En el bloque de la sección, antes del código |
| Funciones | Bloque de sección + docstring (`Parámetros` y `Devuelve`) |
| Clases | Bloque de sección + docstring en la clase y en cada método |
| Atributos y métodos | Bloques con guiones más cortos dentro de la clase |
| Ciclos `for` y `with` | Explicados dentro del bloque de la sección |
| Resultado esperado | Dentro del bloque, indicando lo que imprime |
| Aclaraciones puntuales | Comentario `#` de una línea |
| Idioma | Español |
