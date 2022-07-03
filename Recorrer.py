#Recorrer una lista

def lista():
    for x in ['perro','gato','loro','vaca','hipopotamo']:
        print(x)

lista()

#Recorrer diccionearios

x = {"a": 1,
"b": 2,
"c":3,
"d":4}

for key in x:
    print(key)

#Recorrer una lista de tuplas

def tuplas():
    coleccion = [('a','b','c'), ('x','y','z'),('1','2','3','4','5')]
    for item in coleccion:
        x1 = item[0]
        x2 = item[1]
        x3 = item[2]
        print(x1)

tuplas()


