# si es mneor de 10 , rojo
# si es mayor de 10, amarillo, 
# si es mayor de 40 , verde

# value = 41

# if value < 10:
#     print(f"el color es rojo")
# elif value >= 10 and value < 40:
#     print("el color es amarillo")
# else:
#     print("el color es verde")




# for i in range(1,100,1):
#     print(f"hola mundo {i}")
#     print("siempre")






# entrada = ""

# while entrada != "x":
#     print("sigre adentro")
#     entrada = input("ingrese x para salir:")


# iterador = 1

# while iterador < 5:
#     print("El iterador es:", iterador)
#     iterador += 1
#     # iterador = iterador + 1
    

# contraseñaCorrecta = "python123"
# contraseñaUsuario = ""

# intentosPermitidos = 3
# intentos = 0

# while contraseñaUsuario != contraseñaCorrecta:
#     contraseñaUsuario = input("Introduce la contraseña: ")
#     intentos += 1
#     print(intentos)

#     print(f"le quedan {intentosPermitidos - intentos}")

#     if contraseñaUsuario == contraseñaCorrecta:
#         print("¡Contraseña correcta!")
#         break

#     if intentosPermitidos == intentos:
#         print("reintente en una hora")
#         break


# else:
#     print("¡Contraseña correcta!")

# print("Bienvenido al programa")








# tuCalificacion = 0

# if tuCalificacion == 0:
#     print("No hay premio.")
# else:
#     print("prueba")



# from datetime import datetime

# try:
#     año_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))
#     año_actual = datetime.now().year
#     edad = año_actual - año_nacimiento


#     if edad > 136 :
#         raise ValueError("no creoooo")

#     if edad < 0:
#         print("Parece que ingresaste un año en el futuro 😅")
#     else:
#         print(f"Tienes {edad} años.")

# except ValueError as e:
#     print(f"Validation Error: {e}")




# def showMessage(name):
#     print("hola", name)

# showMessage("Andres")

# def multiplicar(number1 = 2, number2 = 4):
#     # result = number1 * number2
#     return number1 * number2

# elValor1 = multiplicar(4,8)
# elVAlor2 = multiplicar(9,4)
# elValor3 = multiplicar(7)

# print(elValor1)
# print(elVAlor2)
# print(elValor3)

# x = 10

# def showValueX():
#     x = 20
#     print(x)

# showValueX()
# print(x)


# nums = [ 23, 22, 10, 100, 200,23,34,65,78,23,56,3]
# animals = ["cat", "dog", "horse", "snake"]

# def showFirstAndLast(cosas):
#     firts = cosas[0]
#     last = cosas[-1]
#     second= cosas[1]

#     return firts , last, second

# value1,value2,value3 = showFirstAndLast(animals)

# print(value1)
# print(value2)
# print(value3)



# def doblarFunc (num):
#     result = num *2
#     return result

# value1 = doblarFunc(40)
# print("valor de func tradi",value1)

# doblar = lambda text, text2: text + " " + text2

# result2 = doblar("Hola", "Juan")
# print("func lambda", result2)



# def calc(a, b, op="+"):

#     try:

#         if op == "+":
#             return a + b
#         if op == "-":
#             return a - b
#         if op == "*":
#             return a * b
#         if op == "/":
#             if b == 0:
#                 print("no puede dividir por cero")
#                 return
#             return a / b 
#         return "Operación  no soportada"

#     except: ValueError
        
        

# print(calc(6, 2))        # 8
# print(calc(6, 2, "*"))   # 12
# print(calc(6, 0, "**")) 
# print(calc(6, 2, "/")) 


# if b != 0 else "Error: división por cero"



animals = ["cat", "dog", "horse", ]
print(animals)

animals.append("parrot")
animals.append("horse")

animals.pop(4)

print(animals)

