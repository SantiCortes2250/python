#1Elabore una aplicación básica, que haga la resta de dos números y muestre la respuesta en la consola.

class resta:
    def __init__(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2
  

    def restar(self):
        return self.numero1 - self.numero2

entrada1 = int(input("ingrese el numero 1:"))
entrada2 = int(input("ingrese el numero 2:"))
objetoresta = resta(entrada1, entrada2)
print(objetoresta.restar())


#2Elabore una aplicación básica, que multiplique tres números dados y muestre la respuesta en la consola.

class mult:
    def __init__(self, n1, n2, n3):
        self.numero1 = n1
        self.numero2 = n2
        self.numero3 = n3

    def multiplicar(self):
        return self.numero1 * self.numero2 * self.numero3

entrada1 = int(input("ingrese el numero 1"))
entrada2 = int(input("ingrese el numero 2"))
entrada3 = int(input("ingrese el numero 3"))
objetomult = mult(entrada1, entrada2, entrada3)
print(objetomult.multiplicar())


#3Elabore una aplicación básica, que halle el área de un circulo.

class area:
    def __init__(self, n1):
        self.numero1 = n1

    def calcular(self):
        return self.numero1 

entrada1 = int(input("ingrese el radio del circulo:"))
objetoarea = area(3.1416*(entrada1**2))
print(objetoarea.calcular())

#4Elabore un programa que me permita calcular la comisión de un contrato de un empleado, sabiendo que su comisión es del 10% (0.10).

class comision:
    def __init__(self, n1):
        self.numero1 = n1
  

    def calcular(self):
        return self.numero1 

entrada1 = float(input("ingrese el pago del empleado:"))
objetocomision = comision(0.10 * entrada1)
print(objetocomision.calcular())

#5Elabore una aplicación básica, que calcule el promedio de tres notas.

class promedio:
    def __init__(self, n1, n2, n3):
        self.numero1 = n1
        self.numero2 = n2
        self.numero3 = n3

    def calcular(self):
        return self.numero1 + self.numero2 + self.numero3

entrada1 = float(input("ingrese la nota 1:"))
entrada2 = float(input("ingrese la nota 2:"))
entrada3 = float(input("ingrese la nota 2:"))
objetopromedio = promedio(entrada1, entrada2,entrada3/3)
print(objetopromedio.calcular())

#6Elabore una aplicación básica, que calcule la cantidad de horas que paga un cliente de un parqueadero por su moto sabiendo que la hora es a $300 pesos.

class parqueadero:
    def __init__(self, n1):
        self.numero1 = n1

    def calcular(self):
        return self.numero1

entrada1 = int(input("ingrese la cantidad de horas:"))
objetoparqueadero = parqueadero(300 * entrada1)
print(objetoparqueadero.calcular())

#7Elabore una aplicación básica, calcule la nomina de un empleado sabiendo que le pagan por horas, el valor de la hora es a $5000, trabajo en la semana 20 horas.

class nomina:
    def __init__(self, n1):
        self.numero1 = n1

    def calcular(self):
        return self.numero1

pago = 5000
objetonomina = nomina(20 * pago)
print(objetonomina.calcular())

#8Elabore una aplicación básica, muestre los datos personales de un aprendiz

class aprendiz:
    def __init__(self, dat1, dat2, dat3, dat4):
        self.dato1 = dat1
        self.dato2 = dat2
        self.dato3 = dat3
        self.dato4 = dat4

    def mostrar(self):
        return self.dato1, self.dato2, self.dato3, self.dato4


entrada1 = str(input("ingrese sus nombres y apellidos:"))
entrada2 = str(input("ingrese su correo electronico:"))
entrada3 = str(input("ingrese su numero de telefono:"))
entrada4 = str(input("ingrese su direccion:"))

objetoaprendiz = aprendiz(entrada1, entrada2, entrada3, entrada4)
print(objetoaprendiz.mostrar())


#9Elabore una aplicación básica, que me permita sacar el impuesto IVA del 19% (0.19) de una compra hecha por un cliente.

class compra:
    def __init__(self, n1):
        self.numero1 = n1
  

    def sacar_iva(self):
        return self.numero1 

compras = float(input("ingrese el precio de la compra:"))
objetocompra = compra(0.19 * compras)
print(objetocompra.sacar_iva())

#10Elabore una aplicación básica, calcule el pago total por la compra de hamburguesas, teniendo en cuenta que su valor es a $7000

class hamburguesas:
    def __init__(self, n1):
        self.numero1 = n1
  

    def calcular_pago(self):
        return self.numero1 

cantidad = int(input("ingrese la cantidad de hamburguesas compradas:"))
objetohambuerguesa = hamburguesas(7000 * cantidad)
print(objetohambuerguesa.calcular_pago())

#11Elabore una aplicación básica, que calcule la cantidad de pesos que hay en un dólar.

class dolar:
    def __init__(self, n1):
        self.numero1 = n1
  

    def calcular_pesos(self):
        return self.numero1 

cantidad = float(input("ingrese la cantidad de pesos:"))
objetodolar = dolar(0.082 * cantidad)
print(objetodolar.calcular_pesos())

#12Elabore una aplicación básica, que convierta de 5 metros a centímetros.

class coversion:
    def __init__(self, n1):
        self.numero1 = n1

    def convertir(self):
        return self.numero1

metros = 5
objetoconversion = coversion(100 * metros)
print(objetoconversion.convertir())

#13Elabore una aplicación básica, calcule los costos de arreglo de tres camisas sabiendo que el costo unitario por arreglo es de $4000

class camisas:
    def __init__(self, cam1):
        self.camisa1 = cam1

    def calcular_costo(self):
        return self.camisa1

cam = int(input("ingrese el numero de camisas que quiere arreglar:"))
objetocamisas = camisas(cam * 4000)
print(objetocamisas.calcular_costo())

#14Elabore una aplicación básica para una empresa de préstamo de lavadoras, el costo por hora de lavado es $500 y se uso 18 horas.

class lavadoras:
    def __init__(self, lav1):
        self.lavadora1 = lav1

    def calcular_costo(self):
        return self.lavadora1

horas = 18
objetolavadoras = lavadoras(horas * 500 )
print(objetolavadoras.calcular_costo())





















