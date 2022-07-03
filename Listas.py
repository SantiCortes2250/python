Nombre = ['Luisa','Santiago','Camila','Mariana','Rodolfo','Pedro']
print(Nombre)

#Seleccionar
print(Nombre[0])
print(Nombre[2])
print(Nombre[-3])
print(Nombre[-2])

#Agrega al final de la lista

Nombre.append("Camila")

#Insertar en una Posicion

Nombre.insert(1, "Pedro")

#Remover

Nombre.remove("Luisa")

#Tamaño de lista

X = len(Nombre)
print(X)

#Poner la Lista en reverso

Nombre.reverse()

#Recorrido de una lista

for elemento in Nombre:
    print(elemento)

for x in range(2):
    x = input("ingrese un numero:")
    Nombre.insert(0, x)





