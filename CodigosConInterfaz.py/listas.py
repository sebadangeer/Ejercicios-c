# lista=["hola"]
# lista.remove("eliminar elementos de la lista")
# lista.sort("ordenar la lista ")
# lista.clear("Limpiar la lista")
# lista.append("Añadir elementos en una lista")
# lista.insert("Añadir elementos a una lista en un lugar especifico")
listas=[[1,2],[1,3]]
print(listas[1])
dicc={"Hola": 1, "chao":2}
#Items es una funcion
for key , value in dicc.items():
    print(key,value)
#añadir llaves
dicc ["nombre de la llave"]="Valor de la  nueva llave"
ki=input("La llave")
valor=input("El valor de la llave")
#asi se añaden elementos al diccionario
dicc[ki]=valor
producto={1:"pera"}
valor={1:500}
print(f"Usted lleva {producto[1]} {valor[1]}")
del dicc["nombre de la llave"]
dicc["chao"].pop["Elemento de la lista"]