from consumo import ConsumoEnergia

def menu():
    sistema = ConsumoEnergia()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar aparato")
        print("2. Ver reporte")
        print("3. Editar aparato")
        print("4. Eliminar aparato")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre del aparato: ")
            try:
                potencia = float(input("Potencia en watts: "))
                horas = float(input("Cuantas horas se usa el aparato al mes: "))
                sistema.agregar_aparato(nombre, potencia, horas)
            except ValueError:
                print("Poné solo números en potencia y horas.")

        elif opcion == "2":
            sistema.mostrar_reporte()

        elif opcion == "3":
            nombre = input("Nombre del aparato a editar: ")
            try:
                nueva_potencia = float(input("Nueva potencia en watts: "))
                nuevas_horas = float(input("Nuevas horas de uso al mes: "))
                sistema.editar_aparato(nombre, nueva_potencia, nuevas_horas)
            except ValueError:
                print("Poné solo números en potencia y horas.")

        elif opcion == "4":
            nombre = input("Nombre del aparato a eliminar: ")
            sistema.eliminar_aparato(nombre)

        elif opcion == "5":
            print("Adiós, cuídate.")
            break
        else:
            print("Opción no válida, probá otra.")

if __name__ == "__main__":
    menu()
