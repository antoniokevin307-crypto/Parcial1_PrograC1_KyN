from aparatos import Aparato

# Clase para manejar el consumo eléctrico de varios aparatos
class ConsumoEnergia:
    def __init__(self, precio_kwh=0.25):
        self.aparatos = []           # Lista donde se guardan los aparatos
        self.precio_kwh = precio_kwh # Precio de la electricidad por kWh

    # Agrega un nuevo aparato, validando que potencia y horas sean positivos
    def agregar_aparato(self, nombre, potencia, horas):
        if potencia <= 0 or horas <= 0:
            print("Los valores deben ser positivos, revisá bien.")
            return
        aparato = Aparato(nombre, potencia, horas)
        self.aparatos.append(aparato)
        print(f"El aparato '{nombre}' se guardó correctamente.")

    # Elimina un aparato por nombre
    def eliminar_aparato(self, nombre):
        for aparato in self.aparatos:
            if aparato.nombre.lower() == nombre.lower():
                self.aparatos.remove(aparato)
                print(f"El aparato '{nombre}' fue eliminado.")
                return
        print("No se encontró ese aparato.")

    # Edita potencia y horas de un aparato existente
    def editar_aparato(self, nombre, nueva_potencia, nuevas_horas):
        for aparato in self.aparatos:
            if aparato.nombre.lower() == nombre.lower():
                aparato.potencia = nueva_potencia
                aparato.horas = nuevas_horas
                print(f"El aparato '{nombre}' fue actualizado.")
                return
        print("No encontré ese aparato.")

    # Muestra un reporte de consumo y costo de todos los aparatos
    def mostrar_reporte(self):
        if not self.aparatos:
            print("No hay aparatos registrados todavía.")
            return

        # Ordena los aparatos de mayor a menor consumo
        ordenados = sorted(self.aparatos, key=lambda a: a.calcular_consumo(), reverse=True)

        total_consumo = 0
        total_costo = 0
        print("\n Reporte de Consumo Eléctrico")
        print("-" * 45)

        for aparato in ordenados:
            consumo = aparato.calcular_consumo()
            costo = aparato.calcular_costo(self.precio_kwh)
            total_consumo += consumo
            total_costo += costo
            print(f"Aparato: {aparato.nombre}")
            print(f"   Consumo: {consumo:.2f} kWh")
            print(f"   Costo: ${costo:.2f}\n")

        print("-" * 45)
        print(f"Consumo total: {total_consumo:.2f} kWh")
        print(f"Gasto mensual: ${total_costo:.2f}")

        # Aparato que más gasta
        mayor = ordenados[0]
        print(f"El aparato que más gasta es: {mayor.nombre} con {mayor.calcular_consumo():.2f} kWh")
