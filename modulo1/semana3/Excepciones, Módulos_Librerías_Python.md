# Clase: Excepciones, Módulos y Librerías en Python

## Objetivos de la sesión

Al final de esta clase, serás capaz de:

-   Entender qué es una **excepción** y cómo manejarla con
    `try/except/finally`.
-   Importar y utilizar **módulos** (tanto de la librería estándar como
    propios).
-   Reconocer las principales **librerías** usadas en Python.
-   Crear un archivo `utils.py` con funciones y reutilizarlas desde otro
    archivo.
-   Resolver ejercicios prácticos para afianzar lo aprendido.

------------------------------------------------------------------------

## 1. Excepciones en Python

Una **excepción** es un error que ocurre durante la ejecución de un
programa.\
Si no la manejamos, el programa se detiene.

### Sintaxis básica

``` python
try:
    ...
except TipoDeError:
    ...
finally:
    ...
```

### Ejemplo

``` python
try:
    numero = int(input("Introduce un número entero: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Error: debes ingresar un número válido.")
finally:
    print("Fin del programa.")
```

------------------------------------------------------------------------

## 2. Módulos en Python

``` python
import math
from math import sqrt
import math as m
```

------------------------------------------------------------------------

## 3. Librerías en Python

-   Librerías estándar: `math`, `random`, `datetime`, `os`, `json`, etc.
-   Datos: `numpy`, `pandas`, `matplotlib`, `seaborn`
-   ML: `sklearn`, `tensorflow`, `pytorch`
-   Web: `flask`, `django`, `fastapi`
-   SQL: `sqlite3`, `pymysql`, `psycopg2`

------------------------------------------------------------------------

## 4. Ejemplo usando librerías

``` python
import math
import random
import datetime

print("Raíz:", math.sqrt(16))
print("Aleatorio:", random.randint(1, 10))
print("Fecha:", datetime.date.today())
```

------------------------------------------------------------------------

## 5. Crear y usar un archivo utils.py

### utils.py

``` python
import math
from datetime import date

def doble(n): return n * 2
def es_par(n): return n % 2 == 0
def area_circulo(r): return math.pi * r ** 2
def hoy(): return date.today().isoformat()
```

### main.py

``` python
import utils

n = int(input("Número: "))
print(utils.doble(n))
print(utils.es_par(n))
```

------------------------------------------------------------------------

## 6. Enunciados de ejercicios

1.  Conversor de temperatura con excepciones
2.  Divisor seguro con manejo de múltiples errores
3.  Uso combinado de `math` y `random`
4.  Fechas con `datetime`
5.  Módulo `utils_string.py` con funciones de texto
6.  Calculadora modular
7.  Proyecto mini: Gestor de notas
