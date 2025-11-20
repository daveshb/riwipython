
# CRUD en Python con JSON: Mini sistema de gestión de estudiantes

En esta lección vas a construir paso a paso un **CRUD** (Create, Read, Update, Delete) para gestionar estudiantes usando **Python** y un archivo **JSON** como “mini base de datos”.

---

## Objetivos de la clase

Al finalizar podrás:

- Entender qué es CRUD y para qué sirve.
- Usar archivos JSON para guardar datos.
- Implementar funciones para:
  - Crear estudiantes.
  - Leer estudiantes.
  - Actualizar estudiantes.
  - Eliminar estudiantes.

---

## 1. ¿Qué es CRUD?

CRUD son las operaciones básicas de casi cualquier sistema que trabaja con datos:

- **Create**: crear o añadir registros.
- **Read**: leer / consultar registros.
- **Update**: modificar datos existentes.
- **Delete**: eliminar registros.

En esta clase haremos un CRUD de estudiantes donde cada estudiante tendrá:

- `código`
- `nombre`
- `edad`

---

## 2. Configuración inicial del proyecto

### Paso 1: Crear el archivo principal

Crea un archivo llamado:

```
crud_estudiantes.py
```

### Paso 2: Importar librería y definir archivo JSON

```python
import json

ARCHIVO = "estudiantes.json"
```

---

## 3. Inicializar datos

```python
def inicializar():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
```

---

## 4. Guardar datos

```python
def guardar(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)
```

---

## 5. Crear registros (Create)

```python
def crear(codigo, nombre, edad):
    data = inicializar()
    data[codigo] = {"nombre": nombre, "edad": edad}
    guardar(data)
    print("Estudiante creado.")
```

---

## 6. Leer registros (Read)

```python
def leer():
    data = inicializar()
    for cod, info in data.items():
        print(cod, info)
```

---

## 7. Actualizar registros (Update)

```python
def actualizar(codigo, nombre=None, edad=None):
    data = inicializar()
    if codigo in data:
        if nombre:
            data[codigo]["nombre"] = nombre
        if edad is not None:
            data[codigo]["edad"] = edad
        guardar(data)
        print("Estudiante actualizado.")
    else:
        print("Estudiante no encontrado.")
```

---

## 8. Eliminar registros (Delete)

```python
def eliminar(codigo):
    data = inicializar()
    if codigo in data:
        del data[codigo]
        guardar(data)
        print("Estudiante eliminado.")
    else:
        print("Estudiante no encontrado.")
```

---

## 9. Pruebas del CRUD

```python
if __name__ == "__main__":
    crear("A001", "Ana", 21)
    crear("A002", "Luis", 20)
    leer()
    actualizar("A001", edad=22)
    eliminar("A002")
    leer()
```

---

## 10. Conclusión

Este CRUD básico te prepara para trabajar con bases de datos reales, APIs y sistemas profesionales.  
¡Sigue experimentando y mejorando el código!
