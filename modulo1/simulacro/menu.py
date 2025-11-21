from utils import saludar_usuario

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opción (1-5): ")
    
    if opcion == "1":
        print("✓ Opción 1 seleccionada")
        saludar_usuario()
    elif opcion == "2":
        print("✓ Opción 2 seleccionada")
    elif opcion == "3":
        print("✓ Opción 3 seleccionada")
    elif opcion == "4":
        print("✓ Opción 4 seleccionada")
    elif opcion == "5":
        print("✓ Saliendo del programa...")
        break
    else:
        print("✗ Opción no válida")
