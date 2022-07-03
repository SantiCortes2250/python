from Empleado import Empleado
while True:
    print("\n----------PAGO TOTAL----------")
    while True:
        print("\n------Cual es el cargo------")
        print("\n1: Operario.\n2: Administrativo.")
        TipoCargo = int(input("\n=> Opopcion: "))
        if TipoCargo == 1:
            print("El valor por horas extra es de (5.000)\n")
            break
        elif TipoCargo == 2:
            print("El valor por horas extra es de (10.000)\n")
            break
        else:
            print("\nPor favor ingrese una opcion correcta")

    objeto = Empleado(input("=> Nombre: "), input("=> Apellido: "), input("=> Documento: "), float(input("=> Salario: ")), float(input("=> Bonificacion: ")), float(input("=> Descuento: ")), float(input("=> Horas extras: ")), TipoCargo)
    objeto.pago_total()
    print(objeto)