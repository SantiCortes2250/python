#While
x = 0
while x < 8:
    print(x)
    if x == 4:
        print("se paro el ciclo")
        break
    x += 1

#For
for x in(0,1,2,3,4,5):
    print(x)
    if  x == 2:
        break

#Def

def rango():
    for x in range(1,7):
        print(x)
rango()


def saludo():
    veces = int(input("¿Cuantas veces quiere que lo salude?"))
    for x in range(veces):
        print("Hola", end="")
        print("Adios")

saludo()
        