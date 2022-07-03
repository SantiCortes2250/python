
class Santiago:
    def __init__(self, cualSantiago):
        self.__Santiago = cualSantiago

    def MostrarSantiago(self):
        if (self.__Santiago == 1):
            return "Eres Santiago Castilla"
        elif (self.__Santiago == 2):
            return "Eres Santiago Rincon"
        else:
            return "No eres ningun Santiago"

print("1 = Santiago Castilla, 2 = Santiago Rincon")
print("-------------------------------------------")
objeto = Santiago(int(input("Ingresa 1 o 2: ")))
print("-------------------------------------------")
print(objeto.MostrarSantiago())
    








    