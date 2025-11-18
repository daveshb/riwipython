# Clase: Manejo de Archivos en Python

## 1. Introducción

En Python, el manejo de archivos es fundamental cuando se necesita
guardar información de manera permanente o leer datos externos. Los
programas suelen requerir trabajar con registros, configuraciones,
reportes, logs o bases de datos, y Python facilita este proceso de forma
sencilla.

## 2. Abrir un archivo
        
Para abrir un archivo usamos:

    open("archivo.txt", modo)

Modos más comunes: - "r": leer. El archivo debe existir. - "w":
escribir. Si existe, se sobrescribe. - "a": añadir contenido al final. -
"r+": lectura y escritura.

## 3. Cerrar un archivo

Todo archivo debe cerrarse manualmente con:

    archivo.close()

Sin embargo, lo más recomendable es usar:

    with open("archivo.txt", "r") as archivo:
        ...

Esto cierra el archivo automáticamente y evita errores.

## 4. Leer un archivo

### Leer todo el contenido:

    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)

## 5. Leer un archivo línea por línea

    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            print("Linea:", linea.strip())

## 6. Escribir en un archivo

    datos = ["Ana", "Luis", "Zoe"]

    with open("nombres.txt", "w") as archivo:
        for nombre in datos:
            archivo.write(nombre + "\n")

## 7. Ejemplo completo: escribir y leer

    datos = ["Ana", "Luis", "Zoe"]

    with open("nombres.txt", "w") as archivo:
        for nombre in datos:
            archivo.write(nombre + "\n")

    with open("nombres.txt", "r") as archivo:
        contenido = archivo.read()

    print(contenido)

## 8. Ejercicio demostrativo: crear un archivo con la tabla de multiplicar

    def crear_tabla():
        numero = int(input("Ingresa un numero para generar su tabla de multiplicar: "))
        nombre_archivo = f"tabla_{numero}.txt"

        with open(nombre_archivo, "w") as archivo:
            for i in range(1, 11):
                linea = f"{numero} x {i} = {numero * i}\n"
                archivo.write(linea)

        print(f"Archivo '{nombre_archivo}' creado con exito.")

    crear_tabla()

## 9. Ejercicios para practicar

### Ejercicio 1: Guardar frutas

Solicita al usuario 5 frutas y guárdalas en `frutas.txt`, una por línea.

### Ejercicio 2: Contar líneas

Lee un archivo de texto y muestra cuántas líneas contiene.

### Ejercicio 3: Buscar una palabra

Pide una palabra y muestra todas las líneas de un archivo donde
aparezca.

### Ejercicio 4: Crear lista de tareas

Un programa que: 1. Pida tareas al usuario. 2. Las agregue al archivo
usando modo "a". 3. Muestre todas las tareas al final.

### Ejercicio 5: Guardar números pares

Genera los números del 1 al 100 y guarda solo los pares en `pares.txt`.

### Ejercicio 6: Transformar datos

Dado un archivo con nombres, crea otro archivo con los mismos nombres en
mayúsculas.
