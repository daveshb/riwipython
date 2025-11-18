# datos = ["Ana", "Luis", "Zoe"]

# with open("nombres.txt", "w") as archivo:
#     for nombre in datos:
#         archivo.write(nombre + "\n")

# with open("nombres.txt", "r") as archivo:
#     contenido = archivo.read()

# print(contenido)

def crear_tabla():
        numero = int(input("Ingresa un numero para generar su tabla de multiplicar: "))
        nombre_archivo = f"tabla_{numero}.txt"

        with open(nombre_archivo, "w") as archivo:
            for i in range(1, 11):
                linea = f"{numero} x {i} = {numero * i}\n"
                archivo.write(linea)

        print(f"Archivo '{nombre_archivo}' creado con exito.")


crear_tabla()