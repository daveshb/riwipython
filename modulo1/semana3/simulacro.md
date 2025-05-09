# Simulacro de Examen: Gestión de Inventario de una Librería en Python

## Caso de Uso (Épica):
Como gerente de una librería, quiero un sistema que me permita gestionar el inventario de libros de manera eficiente, para que pueda realizar un seguimiento preciso de los títulos disponibles, su cantidad y los precios actualizados. Además, quiero poder calcular el valor total del inventario para saber cuánto dinero está invertido en los productos.

## Funcionalidades Principales:
Para alcanzar un resultado óptimo en esta prueba, deberás implementar las siguientes funcionalidades en Python:

### 1. **Añadir libros al inventario:**
   - Permitir al usuario agregar libros con atributos como: título, precio y cantidad disponible.
   - Validar que el precio y la cantidad sean números positivos.

### 2. **Consultar libros en inventario:**
   - Buscar un libro por su título y mostrar sus detalles (título, precio, cantidad).
   - Si el libro no existe, mostrar un mensaje de error indicando que el libro no se encuentra en el inventario.

### 3. **Actualizar precios de libros:**
   - Modificar el precio de un libro específico en el inventario.
   - Validar que el nuevo precio sea un número positivo antes de realizar el cambio.

### 4. **Eliminar libros del inventario:**
   - Permitir la eliminación de un libro que ya no está disponible.
   - Confirmar la existencia del libro antes de eliminarlo.

### 5. **Calcular el valor total del inventario:**
   - Calcular el valor total del inventario multiplicando el precio por la cantidad de cada libro.
   - Mostrar el total acumulado con dos decimales.

## Criterios de Aceptación:
- El programa debe permitir agregar al menos 5 libros iniciales.
- Al consultar un libro, debe indicar si no existe en el inventario con un mensaje claro.
- La actualización de precios debe validar que el nuevo precio sea un número positivo.
- La eliminación de un libro debe confirmar su existencia antes de borrarlo.
- El cálculo del valor total del inventario debe ser preciso y mostrar el resultado con dos decimales.
- El código debe estar estructurado en funciones para cada operación.
- El código y los comentarios deben estar 100% en inglés (sin excepción alguna).

## Instrucciones:
1. Crea una lista de libros iniciales con al menos 5 libros, donde cada libro sea un diccionario con las claves: `title`, `price`, y `quantity`.
2. Implementa funciones para cada una de las funcionalidades mencionadas.
3. La estructura general debe incluir un menú interactivo que permita a los usuarios seleccionar las acciones a realizar.
4. Al finalizar, asegúrate de mostrar el valor total del inventario con dos decimales.

## Ejemplo de Libros Iniciales:
```python
inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

```
