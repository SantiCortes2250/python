class Recarga:
    def __init__(self):
        pass
    
    def cantidadMinutos(self, operador, valorRecarga):
        self.operador = operador
        self.valorRecarga = valorRecarga
        
        
        if self.operador == 1:
            self.valorMinuto = 100
            self.cantidadMinutos = round(self.valorRecarga / self.valorMinuto)
            
        elif self.operador == 2:
            self.valorMinuto = 110
            self.cantidadMinutos = round(self.valorRecarga / self.valorMinuto)
            
        elif self.operador == 3:
            self.valorMinuto = 120
            self.cantidadMinutos = round(self.valorRecarga / self.valorMinuto)
            
        elif self.operador == 4:
            self.valorMinuto = 90
            self.cantidadMinutos = round(self.valorRecarga / self.valorMinuto)
            
        if self.valorRecarga >= 20000:
            return round(self.cantidadMinutos * 2)
        else:
            return round(self.cantidadMinutos)
        
    def calcularPaquetes(self, numero):
        
            self.paquete = numero
            if self.paquete == 1:
                return 3000
            elif self.paquete == 2:
                return 5000
            elif self.paquete == 3:
                return 10000
       
objeto = Recarga()

while True:
    print("Bienvenido a la aplicacion de Recargas: ")
    print("Porfavor seleccione una opcion: ")
    n = int(input('1 recarga de celular, 2 recarga de paquete de datos, 3 minutos + internet, 4 para salir: '))
    print("ingrese "
        
    if n == 1:
        print("Seleccione el operador que desea: ")
        print (f'La cantidad de minutos obtenidos es de: ', objeto.cantidadMinutos(int(input('1 para claro, 2 para movistar, 3 para tigo, 4 para virgin: ')), int(input('Ingrese el valor a recargar: '))) )
        
        
    elif n == 2:
        print (f'El valor del paquete es de: ', objeto.calcularPaquetes(int(input('1 paquete 3000, 2 paquete 5000, 3 paquete 10000: '))) )
        
        
    elif n == 3:
        print (f'La cantidad de minutos obtenidos es de: ', objeto.cantidadMinutos(int(input('1 para claro, 2 para movistar, 3 para tigo, 4 para virgin: ')), int(input('Ingrese el valor a recargar: '))) )
            
        
        print (f'El valor del paquete es de: ', objeto.calcularPaquetes(int(input('1 paquete 3000, 2 paquete 5000, 3 paquete 10000: '))) )
        
    elif n == 4:
        print("Gracias por usar la aplicacion")
        
    
    else:
        print("Porfavor ingrese una opcion valida.")
        break

