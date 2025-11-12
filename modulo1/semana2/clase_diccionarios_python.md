# Clase: Diccionarios en Python

## 1. Datos generales de la clase

- **Tema:** Diccionarios en Python   
- **Objetivos de aprendizaje:**
  1. Entender qué es un diccionario y en qué se diferencia de listas y tuplas.
  2. Comprender las características clave: claves únicas, claves inmutables, valores mutables.
  3. Usar los métodos principales: `keys()`, `values()`, `items()` y `get()`.
  4. Recorrer un diccionario con ciclos `for`.
  5. Aplicar todo en pequeños ejercicios prácticos.

---

## 2. Actividad de inicio

**Pregunta para el grupo:**

> “Si quisieran guardar la información de un estudiante (nombre, edad, ciudad) en Python, ¿cómo lo harían con una lista? ¿y con una tupla?”

Permite que propongan algo parecido a:

```python
estudiante_lista = ["Lucía", 22, "Medellín"]
```

Luego plantea el problema:

- ¿Qué pasa si no recuerdas qué hay en cada posición?
- ¿Cómo haces para agregar o cambiar solo la ciudad?

Usa esto para introducir la idea de **pares clave-valor**.

---

## 3. Introducción a los diccionarios

### Explicación

1. **Definición simple**

   > Un diccionario es una colección **no ordenada** de pares **clave-valor**.  
   > En lugar de acceder por índice (0, 1, 2…), accedemos por **claves**.

2. **Sintaxis básica**

   Ejemplo en código:

   ```python
   coder = {
       "nombre": "John Doe",
       "apellido": "Smith",
       "edad": 30,
       "direccion": "123 Main St",
       "estado": True,
       "email": "john.doe@example.com"
   }
   ```

3. **Acceso a los valores**

   ```python
   print(coder["nombre"])   # John Doe
   print(coder["edad"])     # 30
   ```

   Comenta que entre `[]` siempre va la **clave**, no un índice numérico.

### Mini ejercicio guiado

Pídeles que creen un diccionario llamado `persona` con estas claves:

- `"nombre"`
- `"edad"`
- `"ciudad"`

y que impriman el valor de `"ciudad"`.

Ejemplo de solución:

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}
print(persona["ciudad"])
```

---

## 4. Características clave de los diccionarios

### 4.1 Claves únicas

> Cada clave debe ser **única**. Si repites una clave, el último valor sobrescribe al anterior.

Demostración rápida:

```python
datos = {
    "nombre": "Carlos",
    "nombre": "María"
}
print(datos["nombre"])  # ¿Qué creen que imprime?
```

Explica que se imprime `"María"` porque el valor anterior fue sobrescrito.

### 4.2 Claves inmutables

> Las claves deben ser de un tipo **inmutable**: cadenas, números o tuplas (con elementos inmutables).

Ejemplo válido:

```python
dicc = {
    "nombre": "Lucía",
    123: "un número",
    (1, 2): "una tupla"
}
```

Ejemplo inválido (no lo ejecutes si no quieres error, solo muéstralo):

```python
# No permitido:
# dicc = { ["lista"]: "valor" }
```

### 4.3 Valores mutables

> Los valores sí pueden ser de cualquier tipo: listas, otros diccionarios, etc.

Ejemplo:

```python
coder = {
    "nombre": "David",
    "skills": ["Python", "Git", "HTML"],
    "proyectos": {
        "portfolio": True,
        "api_flask": False
    }
}
```

---

## 5. Métodos básicos del diccionario

En esta sección se cubren **`keys()`**, **`values()`**, **`items()`** y **`get()`** usando un diccionario base:

```python
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Lima"
}
```

### 5.1 `keys()` – obtener las claves

> `keys()` devuelve todas las claves del diccionario en un objeto `dict_keys`.  
> Para manejarlo más fácil, se puede convertir a una lista.

```python
claves = list(persona.keys())
print(claves)   # ['nombre', 'edad', 'ciudad']
```

**Ejercicio rápido**

1. Crear un diccionario `libro` con `titulo`, `autor`, `año`.
2. Guardar las claves en una lista llamada `campos`.
3. Imprimir `campos`.

### 5.2 `values()` – obtener los valores

Ejemplo similar al de la diapositiva:

```python
libro = {
    "titulo": "Cien Años de Soledad",
    "autor": "Gabriel García Márquez",
    "año_publicacion": 1967
}

valores = list(libro.values())
print(valores[0])   # Cien Años de Soledad
```

**Mini reto**

> Imprime todos los valores del diccionario `libro` usando un `for`.

```python
for valor in libro.values():
    print(valor)
```

### 5.3 `items()` – pares clave-valor

> `items()` devuelve una colección `dict_items`, que es una lista de tuplas `(clave, valor)`.

```python
coche = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

items = list(coche.items())
print(items[2])     # ('año', 2020)
print(items[2][0])  # 'año'
print(items[2][1])  # 2020
```

**Ejercicio**

> Recorre `coche.items()` e imprime algo como:  
> `"clave: marca, valor: Toyota"`

```python
for clave, valor in coche.items():
    print(f"clave: {clave}, valor: {valor}")
```

### 5.4 `get(clave, valor_por_defecto)` – acceso seguro

> `get()` devuelve el valor de una clave si existe.  
> Si no existe, devuelve el **valor por defecto** en lugar de lanzar un error.

```python
estudiante = {
    "nombre": "Lucía",
    "edad": 22,
    "carrera": "Ingeniería"
}

nombre = estudiante.get("nombre", "No disponible")
print(nombre)   # Lucía

promedio = estudiante.get("promedio", "No disponible")
print(promedio) # No disponible
```

En contraste:

```python
# estudiante["promedio"]  # Esto lanzaría KeyError
```

**Ejercicio individual**

Crear un diccionario `config`:

```python
config = {
    "tema": "oscuro",
    "tamaño_fuente": 14
}
```

Luego:

1. Usar `get` para leer `"tema"` con valor por defecto `"claro"`.
2. Usar `get` para leer `"idioma"` con valor por defecto `"es"`.

---

## 6. Recorrer diccionarios con `for`

Usaremos:

```python
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
```

### 6.1 Recorrer solo claves

```python
for clave in persona.keys():
    print(clave)
```

**Resultado esperado:**

- nombre  
- edad  
- ciudad  

### 6.2 Recorrer solo valores

```python
for valor in persona.values():
    print(valor)
```

**Resultado esperado:**

- Juan  
- 25  
- Madrid  

### 6.3 Recorrer claves y valores a la vez

```python
for clave, valor in persona.items():
    print(f"Clave: {clave}, Valor: {valor}")
```

**Resultado esperado:**

- Clave: nombre, Valor: Juan  
- Clave: edad, Valor: 25  
- Clave: ciudad, Valor: Madrid  

---

## 7. Actividad práctica final

**Reto integrador**

Crea un diccionario llamado `curso_python` que contenga:

- `"nombre_curso"`: cadena  
- `"duracion_horas"`: número  
- `"estudiantes"`: lista con nombres de 3 compañer@s  
- `"activo"`: booleano  

Luego:

1. Imprime todas las claves con `keys()`.
2. Imprime todos los valores con `values()`.
3. Imprime cada par clave-valor en una línea usando `items()` y un `for`.
4. Usa `get()` para leer la clave `"nivel"` con valor por defecto `"principiante"`.

Posible solución:

```python
curso_python = {
    "nombre_curso": "Introducción a Python",
    "duracion_horas": 20,
    "estudiantes": ["Ana", "Luis", "Sofía"],
    "activo": True
}

print(list(curso_python.keys()))
print(list(curso_python.values()))

for clave, valor in curso_python.items():
    print(f"{clave}: {valor}")

nivel = curso_python.get("nivel", "principiante")
print("Nivel del curso:", nivel)
```

---

## 8. Cierre y conclusión

- Los diccionarios son fundamentales para manejar datos de forma **organizada y eficiente** usando pares **clave-valor**.
- Métodos como `keys()`, `values()`, `items()` y `get()` permiten trabajar de forma **flexible y segura** con la información.
- Saber **iterar** sobre diccionarios te ayudará a resolver problemas más complejos, como procesar JSON, configurar aplicaciones, manejar datos de usuarios, etc.

**Pregunta final para reflexión:**

> “¿En qué tipo de proyecto real podrían usar diccionarios?  
> (por ejemplo: guardar usuarios, productos de un carrito de compras, configuración de una app, etc.)”
