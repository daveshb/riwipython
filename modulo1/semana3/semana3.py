
# fruits = ["Uva", "Mango", "Naranja", "Madarina"]

# with open("modulo1/semana2/fruits.txt","w") as archivo:
#     for item in fruits:
#         archivo.write(f" la fruta es : {item} \n")


# with  open("modulo1/semana2/fruits.txt","r") as file:
#     for linea in file:
#         print(linea)

while True:
    try:
        num = int(input("Ingrese un numero para la tabla: "))

        with open(f"tablas/tabla-del-{num}.txt","w") as file:
            for i in range(1,11):
                file.write(f"{num} x {i} = {num * i} \n")
        break
    except ValueError as E: 
        print(E)
        print("ingrese solo numeros")
            



