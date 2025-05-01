def pollo(cantidad,valor):
    return cantidad*valor
print("desea llevar pollo")
cuanto=int(input("cuantos pollos llevara"))
quepollo=int(input("de que precio sera"))
precio=pollo(cuanto,quepollo)
print(precio)