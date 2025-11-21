# Simulacro -- Módulo 1 Python

## Título

Sistema Integral de Gestión de Inventario y Ventas para Tienda de
Electrónica con Reportes Dinámicos

## Caso de uso (Épica)

Como encargado del área digital de una cadena nacional de tiendas de
electrónica, necesitas un sistema robusto que no solo permita registrar
ventas y productos, sino también generar reportes detallados, aplicar
descuentos según el tipo de cliente, agrupar estadísticas por marca y
evaluar el rendimiento del inventario con base en las ventas realizadas.

## Requisitos Funcionales

### 1. Gestión del inventario

-   Registrar, consultar, actualizar y eliminar productos.\
-   Cada producto debe incluir:
    -   Nombre del producto\
    -   Marca\
    -   Categoría\
    -   Precio unitario\
    -   Cantidad en stock\
    -   Garantía en meses

### 2. Registro y consulta de ventas

-   Registrar ventas incluyendo:
    -   Cliente\
    -   Tipo de cliente\
    -   Producto vendido\
    -   Cantidad\
    -   Fecha de venta\
    -   Descuento aplicado\
-   Validar stock disponible.\
-   Actualizar inventario automáticamente.\
-   Permitir consultar el historial de ventas.

### 3. Módulo de reportes

-   Top 3 productos más vendidos.\
-   Ventas agrupadas por marca.\
-   Cálculo de ingreso bruto y neto.\
-   Reporte de rendimiento del inventario.

### 4. Validaciones avanzadas

-   Validar entradas del usuario.\
-   Evitar ventas con stock insuficiente.\
-   Evitar registro de productos inválidos.\
-   Manejar errores de entrada sin detener el programa.

### 5. Diseño modular con funciones

-   Usar funciones para cada operación principal.\
-   Utilizar parámetros y valores de retorno.\
-   Usar al menos una función lambda para cálculos agregados.

### 6. Almacenamiento de datos

-   Usar diccionarios anidados y listas.\
-   Aplicar búsquedas y agrupamientos eficientes.

## Criterios de Aceptación

-   El sistema inicia con al menos 5 productos precargados.\
-   Todas las interacciones deben estar en inglés.\
-   Seguir buenas prácticas de codificación.\
-   Programa ejecutado por consola con menú interactivo.\
-   Manejo adecuado de excepciones sin cierres abruptos.
