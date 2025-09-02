from consumo import ConsumoEnergia

# Función principal que muestra un menú interactivo para el usuario
def menu():
    sistema = ConsumoEnergia()  # Creamos el sistema que manejará los aparatos

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar aparato")
        print("2. Ver reporte")
        print("3. Editar aparato")
        print("4. Eliminar aparato")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":  # Registrar un nuevo aparato
            nombre = input("Nombre del aparato: ")
            try:
                potencia = float(input("Potencia en watts: "))
                horas = float(input("Cuantas horas se usa el aparato al mes: "))
                sistema.agregar_aparato(nombre, potencia, horas)
            except ValueError:
                print("Poné solo números en potencia y horas.")

        elif opcion == "2":  # Mostrar reporte de consumo y costo
            sistema.mostrar_reporte()

        elif opcion == "3":  # Editar un aparato existente
            nombre = input("Nombre del aparato a editar: ")
            try:
                nueva_potencia = float(input("Nueva potencia en watts: "))
                nuevas_horas = float(input("Nuevas horas de uso al mes: "))
                sistema.editar_aparato(nombre, nueva_potencia, nuevas_horas)
            except ValueError:
                print("Poné solo números en potencia y horas.")

        elif opcion == "4":  # Eliminar un aparato
            nombre = input("Nombre del aparato a eliminar: ")
            sistema.eliminar_aparato(nombre)

        elif opcion == "5":  # Salir del programa
            print("Adiós, cuídate.")
            break
        else:
            print("Opción no válida, probá otra.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
