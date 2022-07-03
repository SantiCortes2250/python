from Persona import Persona

class Empleado (Persona):
    def __init__(self, nombre, apellido, documento, salario, bonificacion, descuento, horas_extras, TipoCargo, total = 0):
        super().__init__(nombre, apellido, documento) 
        self.extras_ope = 6000
        self.extras_ad = 9000
        self.salario = salario
        self.bonificacion = bonificacion
        self.descuento = descuento
        self.horas_extras = horas_extras
        self.TipoCargo = TipoCargo
        self.total = total

    def pago_total(self):
        if self.TipoCargo == 1:
            total_extras = self.horas_extras * self.extras_ope
        elif self.TipoCargo == 2:
            total_extras = self.horas_extras * self.extras_ad
        self.PagoTotal = (float(self.salario) + float(self.bonificacion) + float(total_extras)) - float(self.descuento)

    def __str__(self):
        return "\nLo que se le debe pagar a " + self.nombre + " " + self.apellido + " es: " + "$" + str(self.PagoTotal) 