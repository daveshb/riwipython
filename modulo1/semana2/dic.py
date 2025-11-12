# coder = {
#     "nombre": "",
#     "apellido": "Smith",
#     "edad": 30,
#     "estado": False,
#     "email": "john.doe@example.com",
#     "nacionalidad" : "Colombiano",
#     "isActive": False,
#     "direccion": "123 Main St",
#     "skills": ["python","html", "JS"]
# }

# value = coder["skills"][2]
# print(value)


# if coder["nombre"]:
#     print("Sigue aprendiendo")
# else: 
#     print("se fue")


# {
#     "nombre": "Julian",
#     "apellido": "Muñoz",
#     "edad": 22,
#     "email"
# }

coders = []
print(coders)

amaount = int(input("cuantos users va a agregar: "))

while amaount != 0 :

    name = input("Ingrese su nombre: ")
    lastName = input("Ingrese su apellido: ")
    age = input("Ingrese su edad: ")
    email = input("Ingrese su email: ")

    coder = {
        "nombre": name,
        "apellido": lastName,
        "edad": age,
        "email": email
    }

    coders.append(coder)
    amaount -= 1

print(coders)



# obj = coders[3]

# print(obj)