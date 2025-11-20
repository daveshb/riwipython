def crear_tabla(numero):
        nombre_archivo = f"tablas/tabla_{numero}.txt"

        with open(nombre_archivo, "w") as archivo:
            for i in range(1, 11):
                linea = f"{numero} x {i} = {numero * i}\n"
                archivo.write(linea)

        print(f"Archivo '{nombre_archivo}' creado con exito.")

def saludar():
    print("hola mundo")

def areaRectangulo (a,b):
     return a * b