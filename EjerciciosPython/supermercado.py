print("Usted a ingresado a autoservice SEVIN")
def totalfinal(preciototal,cantidad,precio,productollevado):
    codigosdeproductos={1:"papasfritas",2:"vinagre",3:"fosforos",4:"salsa de tomate",
                 5:"tallarines",6:"toalla nova",7:"cargador"}
    print("Usted lleva",codigosdeproductos[productollevado])
    return preciototal+cantidad*precio
total=0
producto=0
while producto!=10:
    print(f"""
su total actual es de:{total}

/que desea llevar/

1.-Papas fritas
2.-Vinagre
3.-Fosforos
4.-Salsa de tomate
5.-Tallarines
6.-Toalla nova
7.-cargador de celular

para salir escriba 10 en la terminal
""")
    producto=int(input("ingrese numero de producto:"))
    if producto==10:
        break
    cantp=int(input("ingrese cantidad de producto: "))
    match (producto):
        case 1 :
            total=totalfinal(total,cantp,1000,producto)
        case 2 :
            total=totalfinal(total,cantp,1300,producto)
        case 3 :
            total=totalfinal(total,cantp,300,producto)
        case 4 :
            total=totalfinal(total,cantp,800,producto)
        case 5 :
            total=totalfinal(total,cantp,1100,producto)
        case 6 :
            total=totalfinal(total,cantp,1600,producto)
        case 7 :
            total=totalfinal(total,cantp,12000,producto)
print("su total es de",total)