import json

ARCHIVO = "estudiantes.json"

# Inicializar datos
def inicializar():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Guardar datos
def guardar(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

# CREATE - Crear registros
def crear(codigo, nombre, edad):
    data = inicializar()
    data[codigo] = {"nombre": nombre, "edad": edad}
    guardar(data)
    print(f"✓ Estudiante '{nombre}' creado.")

# READ - Leer registros
def leer():
    data = inicializar()
    if not data:
        print("No hay estudiantes registrados.")
        return
    print("\n--- ESTUDIANTES ---")
    for cod, info in data.items():
        print(f"Código: {cod} | Nombre: {info['nombre']} | Edad: {info['edad']}")
    print()

# UPDATE - Actualizar registros
def actualizar(codigo, nombre=None, edad=None):
    data = inicializar()
    if codigo in data:
        if nombre:
            data[codigo]["nombre"] = nombre
        if edad is not None:
            data[codigo]["edad"] = edad
        guardar(data)
        print(f"✓ Estudiante '{codigo}' actualizado.")
    else:
        print(f"✗ Estudiante '{codigo}' no encontrado.")

# DELETE - Eliminar registros
def eliminar(codigo):
    data = inicializar()
    if codigo in data:
        nombre = data[codigo]["nombre"]
        del data[codigo]
        guardar(data)
        print(f"✓ Estudiante '{nombre}' eliminado.")
    else:
        print(f"✗ Estudiante '{codigo}' no encontrado.")

# Pruebas del CRUD
if __name__ == "__main__":
    crear("A001", "Ana", 21)
    crear("A002", "Luis", 20)
    crear("A003", "Zoe", 19)
    leer()
    
    actualizar("A001", edad=22)
    leer()
    
    eliminar("A002")
    leer()
