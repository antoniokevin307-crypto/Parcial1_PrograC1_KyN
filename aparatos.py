class Aparato:
    def __init__(self, nombre, potencia, horas):
        self.nombre = nombre
        self.potencia = potencia
        self.horas = horas

    def calcular_consumo(self):
        return self.potencia * self.horas / 1000  # kWh

    def calcular_costo(self, precio_kwh):
        return self.calcular_consumo() * precio_kwh
