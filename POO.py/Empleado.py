from clases import persona

class Empleado(persona):
  def __init__(slef, nombre, edad, documento, tipoCargo, salario, bonificacion, descuento, horasExtras, total= 0 ):
    super().__init__(nombre, edad, documento)
    self.extras_Operario = 5000
    self.extras_Administrativo = 7000
    self.tipoCargo = tipoCargo
    self.salario = salario
    self.bonificacion = bonificacion
    self.descuento = descuento
    self.horasExtras = horasExtras
    self.total = total

  def total_pago(self):
    if self.tipoCargo == 1:
      total_extras = self.horasExtras * self.extras_Operario
    elif self.tipoCargo == 2:
      total_extras = self.horasExtras * self.extras_Administrativo
    self.total_pago = (float(self.salario) + float(self.bonificacion) + float(total_extras)) - float(self.descuento)

  def __str__(self):
    return "\nEl pago del señor" + self.nombre + "es un total de:" + "$" + str(self.total_pago)
