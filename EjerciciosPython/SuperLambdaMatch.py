totalf=0
totalx=lambda preciototal,lacantidad,elprecio : preciototal+lacantidad*elprecio
print("Usted a ingresado a autoservice SEVIN")
codigosdeproductos={1:"papas fritas",2:"vinagre",3:"fosforos",4:"salsa de tomate",
                 5:"tallarines",6:"toalla nova",7:"cargador"}
producto=0
while producto!=10:
    print(f"""
su total actual es de:{totalf}

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
            totalf=totalx(totalf,cantp,1000)
        case 2 :
            totalf=totalx(totalf,cantp,1300)
        case 3 :
            totalf=totalx(totalf,cantp,300)
        case 4 :
            totalf=totalx(totalf,cantp,800)
        case 5 :
            totalf=totalx(totalf,cantp,1100)
        case 6 :
            totalf=totalx(totalf,cantp,1600)
        case 7 :
            totalf=totalx(totalf,cantp,12000)
    print(f"""
Usted lleva {cantp} {codigosdeproductos[producto]}
          """)
print("su total es de",totalf)