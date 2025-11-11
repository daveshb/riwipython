
#  Introducción a **Funciones en Python**

---

## 1) ¿Qué es una función?
Una **función** es un bloque reutilizable de código que ejecuta una tarea. Se define con `def` y se **llama** por su nombre.

```py
    def saludar():
    print("¡Hola, coder!")

saludar()  # Llamada
```
**Salida:** `¡Hola, coder!`

---

## 2) Parámetros y argumentos

### 2.1 Posicionales (orden importa)
```py
def presentar(nombre, edad):
    print(f"Me llamo {nombre} y tengo {edad} años.")

presentar("Ana", 20)
```

### 2.2 Nombrados (keyword arguments)
```py
presentar(edad=25, nombre="Luis")
```

---

## 3) `return`: devolver valores
```py
def area_rectangulo(base, altura):
    return base * altura

resultado = area_rectangulo(4, 3)
print("Área:", resultado)
```
**Salida:** `Área: 12`

> Una función **termina** cuando ejecuta `return` y puede **enviar** un valor de vuelta.

---

## 4) Parámetros con valores por defecto
```py
def saludar(nombre="Mundo"):
    print(f"Hola, {nombre}!")

    saludar()        # Usa el valor por defecto
    saludar("Pedro") # Sobrescribe el valor por defecto
```
**Salida:**
```
Hola, Mundo!
Hola, Pedro!
```

---

## 5) `*args` y `**kwargs` (parámetros avanzados, versión fácil)

- `*args` → empaqueta **posicionales** en una **tupla**.
- `**kwargs` → empaqueta **nombrados** en un **diccionario**.

```py
def listar_compras(*items, **extras):
    print("Items:", items)
    print("Extras:", extras)

listar_compras("leche", "pan", tienda="D1", metodo_pago="efectivo")
```
**Salida (aprox.):**
```
Items: ('leche', 'pan')
Extras: {'tienda': 'D1', 'metodo_pago': 'efectivo'}
```

---

## 6) Alcance (scope): variables locales y globales

```py
x = 10  # global

def f():
    x = 99  # local
    print("Dentro de f ->", x)

f()
print("Fuera ->", x)
```
**Salida:**
```
Dentro de f -> 99
Fuera -> 10
```

> La variable `x` **dentro** de la función **no** es la misma que la de **afuera**.

---

## 7) Retornos múltiples
En Python puedes devolver **varios valores** (en realidad, una **tupla**).

```py
def min_max(numeros):
    return min(numeros), max(numeros)

mn, mx = min_max([3.2, 4.5, 4.0, 2.9])
print("min:", mn, "max:", mx)
```
**Salida:** `min: 2.9 max: 4.5`

---

## 8) Closures (suave y útil)
Una función **interna** que recuerda valores de la **externa**.

```py
def potencia(n):
    def elevar(x):
        return x ** n
    return elevar

cuadrado = potencia(2)
cubo = potencia(3)

print(cuadrado(5), cubo(2))  # 25 8
```

---

## 9) Funciones anónimas (**lambda**)
Pequeñas funciones de **una sola expresión**.

```py
doblar = lambda x: x * 2
print(doblar(4))  # 8

# Útil para ordenar
nombres = ["ana", "Pedro", "luis"]
print(sorted(nombres, key=lambda s: s.lower()))
```

---

# 🧪 Ejercicios **resueltos** (para mostrar en clase)

### R1) Calculadora simple
```py
def calc(a, b, op="+"):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else "Error: división por cero"
    return "Operación no soportada"

print(calc(6, 2))        # 8
print(calc(6, 2, "*"))   # 12
print(calc(6, 0, "/"))   # Error: división por cero
```

### R2) Formatear nombre completo
```py
def nombre_completo(nombre, apellido, mayus=False):
    completo = f"{nombre.strip()} {apellido.strip()}"
    return completo.upper() if mayus else completo.title()

print(nombre_completo("  ana ", " pérez  "))          # Ana Pérez
print(nombre_completo("pedro", "garcía", mayus=True)) # PEDRO GARCÍA
```

### R3) Suma flexible con `*args`
```py
def suma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(suma(1, 2, 3))     # 6
print(suma(5))           # 5
print(suma())            # 0
```

### R4) Filtro con `**kwargs`
```py
def filtrar_producto(nombre, **filtros):
    # Solo mostramos cómo llegan los filtros
    return {"nombre": nombre, "filtros": filtros}

print(filtrar_producto("teclado", color="negro", precio_max=100.0))
# {'nombre': 'teclado', 'filtros': {'color': 'negro', 'precio_max': 100.0}}
```

### R5) Conversor de temperaturas (retornos múltiples)
```py
def convertir_celsius(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k

f, k = convertir_celsius(25)
print(f"Fahrenheit: {f}, Kelvin: {k}")
```

### R6) Generador de potencias (closure)
```py
def generar_potencia(n):
    def elevar(x):
        return x ** n
    return elevar

al_cuadrado = generar_potencia(2)
al_cubo = generar_potencia(3)

print(al_cuadrado(9))  # 81
print(al_cubo(3))      # 27
```

### R7) Descuento con valor por defecto
```py
def aplicar_descuento(precio, porcentaje=10):
    return round(precio * (1 - porcentaje/100), 2)

print(aplicar_descuento(100))     # 90.0
print(aplicar_descuento(100, 25)) # 75.0
```

---

#  Mini–quiz 

1) ¿Qué imprime?
```py
def f(a, b=2):
    return a * b

print(f(3))
print(f(3, 5))
```
**Respuesta:** `6` y `15`.

2) ¿Qué tipo de dato devuelve una función con múltiples valores en el `return`?  
**Respuesta:** una **tupla**.

3) ¿Para qué sirven `*args` y `**kwargs`?  
**Respuesta:** para **agrupar** parámetros posicionales y nombrados, respectivamente.

---

#  Practica

> Crea un archivo `ejercicios.py` y resuelvan los siguientes:

1. **Impuestos:** función `impuesto(precio, iva=19)` que devuelva el precio final con IVA.  
2. **Promedio seguro:** `promedio(numeros)` que devuelva 0 si la lista está vacía.  
3. **Contar vocales:** `contar_vocales(texto)`.  
4. **Palíndromo:** `es_palindromo(texto)` que ignore espacios y tildes simples.  
5. **Password fuerte:** `es_fuerte(password)`; al menos 8 chars, 1 mayúscula, 1 minúscula y 1 dígito.  
6. **Fibonacci:** `fib(n)` que devuelva una lista con los primeros `n` números.  
7. **Buscar máximos:** `top2(nums)` que devuelva **dos** mayores distintos (usa retornos múltiples).  
8. **Ticket:** `total_ticket(*precios, propina=0)` suma precios y aplica propina %.  
9. **Filtrar por kwargs:** `filtrar_alumnos(alumnos, **criterios)` (por ejemplo `curso="JS"`, `activo=True`).  
10. **Closure contador:** `contador(inicio=0)` que devuelva una función `inc()` que aumente en 1 cada vez que se llame.  
11. **Lambda orden:** ordenar lista de tuplas `(nombre, edad)` por edad.

---

## Recursos recomendados
- Documentación oficial Python: https://docs.python.org/3/tutorial/
- PEP 8 (estilo de código): https://peps.python.org/pep-0008/

---
