# Listas y Tuplas en Python — Clase práctica

## 1) Listas (`list`)

### ¿Qué es una lista?
Una **lista** es una colección ordenada y **mutable**, lo que significa que sus elementos pueden cambiarse después de creada.

```python
mi_lista = [1, 2, 3]
```

### Mutabilidad de las listas
```python
lista_numerica = [1, 2, 3]
print("Original:", lista_numerica)

lista_numerica.append(4)
lista_numerica.append(5)
lista_numerica.append(6)

print("Modificada:", lista_numerica)
```

### Acceso por índice
```python
frutas = ["Mango", "Orange", "Banana", "Apple", "Grapes"]

print(frutas[0])
print(frutas[2])
print(frutas[3])
```

### Diversidad de tipos
```python
lista_combinada = [
    1, "dos", True, False, ["a", "b"], ("c", "d", "e", "f")
]

print(lista_combinada[4])
print(lista_combinada[5][2])
```

### Métodos comunes de listas
| Método | Descripción |
|--------|-------------|
| `append(e)` | Agrega un elemento al final |
| `insert(i,e)` | Inserta un elemento en la posición `i` |
| `count(e)` | Cuenta apariciones |
| `remove(e)` | Elimina la primera aparición |
| `pop(i)` | Elimina y retorna el elemento |
| `index(e)` | Índice de la primera aparición |
| `sort()` | Ordena |
| `reverse()` | Invierte |
| `clear()` | Vacía la lista |
| `copy()` | Copia la lista |

---

## 2) Tuplas (`tuple`)

### ¿Qué es una tupla?
Una **tupla** es una colección ordenada e **inmutable**.

```python
mi_tupla = (1, "dos", True)
```

### Inmutabilidad
```python
t = (10, 20, 30)
# t[0] = 99  # Error
```

### Acceso por índice
```python
ciudades = ("Medellín", "Bogotá", "Cali")

print(ciudades[0])
print(ciudades[1])
print(ciudades[2])
```

### Diversidad de tipos
```python
tupla = ("a", "b", True, False, [1, 2])
print(tupla[4])
```

### Duplicados
```python
t = (1,1,2,3,3,3)
print(t.count(3))
print(t.index(3))
```

---

## 3) Ejercicios

### Ejercicios de listas
1. Crea una lista con 5 frutas y muestra la tercera fruta.  
2. Agrega 2 frutas nuevas usando `append()`.  
3. Ordena la lista alfabéticamente.  
4. Trabaja con `[3,1,2]`: inserta `99`, elimina `1`, agrega `7`, ordénala descendentemente.  
5. Accede a `'e'` dentro de una tupla interna en una lista mezclada.  

### Ejercicios de tuplas
6. Crea una tupla con 3 colores y muestra el segundo.  
7. Intenta modificar la tupla y captura la excepción.  
8. Convierte `(1,2,3)` a lista, agrega `4`, vuelve a tupla.  
9. Modifica el `[1,2,3]` dentro de `("a","b",[1,2,3])`.  
10. Usa `count()` e `index()` con una tupla que tenga duplicados.  
