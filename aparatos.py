class Aparato:
    def __init__(self, nombre, potencia, horas):
        self.nombre = nombre        # Nombre del aparato
        self.potencia = potencia    # Potencia en vatios
        self.horas = horas          # Horas de uso al día

    def calcular_consumo(self):
        return self.potencia * self.horas / 1000  # Consumo en kWh

    def calcular_costo(self, precio_kwh):
        return self.calcular_consumo() * precio_kwh  # Costo según el precio de la energía

