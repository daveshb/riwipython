
#  Clase: Condicionales, Ciclos y Manejo de Errores en Python

##  Objetivo
Aprender a utilizar las estructuras de control más comunes en Python:
- Condicionales (`if`, `elif`, `else`)
- Ciclos (`for` y `while`)
- Palabras reservadas (`break`, `continue`, `else`)
- Manejo de errores con `try-except`

---

##  Condicionales `if`, `elif`, `else`

Los condicionales permiten ejecutar diferentes bloques de código dependiendo del valor de una condición.

### Ejemplo:

```python
tuCalificacion = int(input("Ingresa tu calificación (0-5): "))

if tuCalificacion == 0:
    print("No hay premio.")
elif tuCalificacion == 1:
    print("Ganas un trofeo de 100 puntos.")
elif tuCalificacion == 2:
    print("Ganas un trofeo de 200 puntos.")
elif tuCalificacion == 3:
    print("Ganas un trofeo de 300 puntos.")
elif tuCalificacion == 4:
    print("Ganas un trofeo de 400 puntos.")
elif tuCalificacion == 5:
    print("Ganas un trofeo de 500 puntos.")
else:
    print("Calificación fuera de rango.")
```

---

##  Ciclo `for`

El ciclo `for` se usa para recorrer secuencias (listas, cadenas, etc.).

### Ejemplo:

```python
nombreCompleto = "Pepito Pérez"

for i in range(5):
    print(nombreCompleto)
```

 **Ventaja:** No necesitas controlar manualmente el índice.

---

##  Ciclo `while`

El ciclo `while` se ejecuta **mientras** una condición sea verdadera.

### Ejemplo:

```python
flag = "si"

while flag != "no":
    print("Hola mundo")
    flag = input("¿Quieres imprimir el mensaje otra vez? (si/no): ")
```

El ciclo continuará hasta que el usuario escriba **“no”**.

---

##  Ciclo `while` con iterador

También puedes usar un contador (iterador) dentro de un `while`:

```python
iterador = 0

while iterador < 5:
    print("El iterador es:", iterador)
    iterador += 1
```

---

##  Ciclo `while` con `else`

Python permite agregar un bloque `else` a un `while`.  
Este se ejecuta **solo cuando el ciclo termina sin usar `break`.**

```python
contraseñaCorrecta = "python123"
contraseñaUsuario = ""

while contraseñaUsuario != contraseñaCorrecta:
    contraseñaUsuario = input("Introduce la contraseña: ")
else:
    print("¡Contraseña correcta!")

print("Bienvenido al programa")
```

---

##  Palabra reservada `break`

`break` se usa para **detener un ciclo inmediatamente**.

### Ejemplo con `for`:

```python
numeros = [3, 8, 15, 1, 22, 7, 18]
umbral = 10

for numero in numeros:
    if numero > umbral:
        print(f"El primer número mayor que {umbral} es {numero}.")
        break
else:
    print(f"Ningún número es mayor que {umbral}.")
```

---

##  Palabra reservada `continue`

`continue` **salta a la siguiente iteración**, omitiendo el resto del código.

### Ejemplo:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 != 0:
        continue
    print(f"Número par: {numero}")
```

---

##  Manejo de Errores con `try-except`

En programación, los usuarios pueden cometer errores al ingresar datos.  
Con `try-except`, Python evita que el programa se detenga inesperadamente.

### Ejemplo práctico:

Queremos que el usuario ingrese su **año de nacimiento** y el sistema calcule su edad.  
Si el usuario ingresa letras o algo inválido, se captura el error.

```python
from datetime import datetime

try:
    año_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))
    año_actual = datetime.now().year
    edad = año_actual - año_nacimiento

    if edad < 0:
        print("Parece que ingresaste un año en el futuro 😅")
    else:
        print(f"Tienes {edad} años.")

except ValueError:
    print("Error: Debes ingresar un número válido para el año.")
```

 **Explicación:**
- `try:` → bloque que intenta ejecutar el código.
- `except ValueError:` → se ejecuta **si ocurre un error de tipo** (por ejemplo, ingresar letras en lugar de números).
- `datetime.now().year` → obtiene el año actual.

---

##  Recomendación práctica

- Usa `for` cuando sepas **cuántas veces** repetirás algo.  
- Usa `while` cuando **no sepas cuántas veces**, pero tengas una **condición de parada**.
- Usa `break` para **detener** un ciclo.
- Usa `continue` para **saltar** una iteración.
- Usa `try-except` para **evitar que tu programa se rompa** ante errores de usuario.

---

##  Ejercicio final

Crea un programa que:

1. Solicite al usuario su año de nacimiento.  
2. Si ingresa letras o símbolos, capture el error.  
3. Calcule su edad.  
4. Si la edad es menor a 18 años, imprima “Eres menor de edad”.  
5. Si es mayor o igual a 18, imprima “Eres mayor de edad”.

 **Ejemplo de salida:**

```
Por favor, ingresa tu año de nacimiento: 2000
Tienes 25 años.
Eres mayor de edad.
```

Si el usuario ingresa texto:

```
Por favor, ingresa tu año de nacimiento: hola
Error: Debes ingresar un número válido para el año.
```

---

##  Bibliografía
- [Documentación oficial de Python: Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Try and Except in Python](https://realpython.com/python-exceptions/)
