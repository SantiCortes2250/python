#OPEREDORES DE CONJUNTO

#interseccion

print({1,2,3,4,5}.intersection({3,4,5,6}))

#Union

print({1,2,3,4,5}.union({3,4,5,6}))

#Diferencia

print({1,2,3,4,5}.difference({3,4,5,6}))

#Diferencia Simetrica

print({1,2,3,4,5}.symmetric_difference({3,4,5,6}))

#Comprobacion de Superconjunto

print({1,2}.issuperset({1,2,3}))

#Verificacion de Subconjunto

print({1,2,3,4,5}.issubset({3,4,5,6}))

#Imprimir lista sin repetir

Comidas = ["Sancocho","Frijoles","Carne","Sancocho","Hamburguesa"]
unique_Comidas = (Comidas)
print(unique_Comidas)
print(list(unique_Comidas))