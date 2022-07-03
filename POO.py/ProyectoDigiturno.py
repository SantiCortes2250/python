class Digiturno:
    def __init__(self):
        pass
    
    def usuarios(self, usuario):
        self.usuario = usuario

        
    def tipodeusuarioSt(self):
        diccStandard = {"usuario1" : "Juan", "usuario2" : "Martin", "usuario3" : "Kevin"}
        turnostandard = ("St")
        if self.usuario == diccStandard["usuario1"]:
            return "Su nombre es Juan, y su turno es: "+ turnostandard + "12"
        elif self.usuario == diccStandard["usuario2"]:
            return "Su nombre es Martin y su turno es: "+ turnostandard + "11"
        elif self.usuario == diccStandard["usuario3"]:
            return "Su nombre es Kevin y su turno es: "+ turnostandard + "10"
        else:
            print("Su nombre de usuario no se encuentra en la base de datos, o pertenece a otro tipo de usuario")
    
    
    def tipodeusuarioPref(self):
        diccPref = {"usuario1" : "Veronica", "usuario2" : "Andres", "usuario3" : "Santiago"}
        turnopref = ("Pr")
        if self.usuario == diccPref["usuario1"]:
            return "Su nombre es Veronica, y su turno es: "+ turnopref + "9"
        elif self.usuario == diccPref["usuario2"]:
            return "Su nombre es Andres, y su turno es: "+ turnopref + "8"
        elif self.usuario == diccPref["usuario3"]:
            return "Su nombre es Santiago, y su turno es :"+ turnopref + "7"
        else:
            print("Su nombre de usuario no se encuentra en la base de datos, o pertenece a otro tipo de usuario")

    def tipodeusuarioVip(self):
        diccVip = {"usuario1" : "Steven", "usuario2" : "Camila", "usuario3" : "Johanna"}
        turnoVip = ("Vip")
        if self.usuario == diccVip["usuario1"]:
            return "Su nombre es Steven, y su turno es: "+ turnoVip + "6"
        elif self.usuario == diccVip["usuario2"]:
            return "Su nombre es Camila, y su turno es: "+ turnoVip + "5"
        elif self.usuario == diccVip["usuario3"]:
            return "Su nombre es Johanna, y su turno es: "+ turnoVip + "4"
        else:
            print("Su nombre de usuario no se encuentra en la base de datos, o pertenece a otro tipo de usuario")
        
    def tipodeusuarioPlat(self):
        diccPlat = {"usuario1" : "Carlos", "usuario2" : "Maria", "usuario3" : "Daniela"}
        turnoPlat = ("Pl")
        if self.usuario == diccPlat["usuario1"]:
            return "Su nombre es Carlos, y su turno es: "+ turnoPlat + "3"
        elif self.usuario == diccPlat["usuario2"]:
            return "Su nombre es Maria, y su turno es: "+ turnoPlat + "2"
        elif self.usuario == diccPlat["usuario3"]:
            return "Su nombre es Daniela, y su turno es: "+ turnoPlat + "1"
        else:
            print("Su nombre de usuario no se encuentra en la base de datos, o pertenece a otro tipo de usuario")

object = Digiturno()
while True:
    print("Bienvenido al Digiturno, porfavor seleccione su opcion: ")
    print("1 = Usuario Standard")
    print("2 = Usuario preferencial")
    print("3 = Usuario Vip")
    print("4 = Usuario Platinum")
    print("5 = Salir")
    n = int(input("Ingrese su tipo de usuario: "))

    if n == 1:
        object.usuarios(input("Ingrese su nombre de usuario Standard: "))
        print(object.tipodeusuarioSt())
    if n == 2:
        object.usuarios(input("Ingrese su nombre de usuario Preferencial: "))
        print(object.tipodeusuarioPref())
    if n == 3:
        object.usuarios(input("Ingrese su nombre de usuario Vip: "))
        print(object.tipodeusuarioVip())
    if n == 4:
        object.usuarios(input("Ingrese su nombre de usuario Platino: "))
        print(object.tipodeusuarioPlat())
    if n == 5:
        print("Gracias por usar el Digiturno.")
        break