from Empleado import empleado
while True:
    print("\n------------BIENVENIDO A TUPAGO---------------")
    while True:
        print("\n------Escoja su cargo----------------")
        print(" 1 = Operario")
        print("2 = Administrativo")
        tipoCargo = int(input("Ingrese la opcion:"))
        if tipoCargo == 1:
            print("El valor de horas extras es de: 5.000")
        elif tipoCargo == 2:
            print("El valor de horas extras es de 7.000")
        else:
            print("Por favor ingrese la opcion que se le indica")
            break
    
    objeto = empleado(input("=> Nombre Completo:")), input("=> Edad"), input("=> Documento:"), float(input("=> Salario:")),
    objeto.total_pago()
    print(objeto)