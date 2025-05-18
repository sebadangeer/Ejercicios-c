nombre=input("Ingrese su nombre de usuario : ")
print(f"""Usted a ingresado a autoservice SEVIN
Bienvenido {nombre}""")
def totalfinal(preciototal,cantidad,precio,productollevado):
    codigosdeproductos={1:"papasfritas",2:"vinagre",3:"fosforos",4:"salsa de tomate",
                 5:"tallarines",6:"toalla nova",7:"cargador"}
    print("Usted lleva",codigosdeproductos[productollevado])
    return preciototal+cantidad*precio
total=0
producto=0
totaldeproductos=0
while producto!=10:
    try:
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
        cantp=int(input("ingrese cantidad de producto:"))
        match (producto):
            case 1 :
                total=totalfinal(total,cantp,1000,producto)
                totaldeproductos+=cantp
            case 2 :
                total=totalfinal(total,cantp,1300,producto)
                totaldeproductos+=cantp
            case 3 :
                total=totalfinal(total,cantp,300,producto)
                totaldeproductos+=cantp
            case 4 :
                total=totalfinal(total,cantp,800,producto)
                totaldeproductos+=cantp
            case 5 :
                total=totalfinal(total,cantp,1100,producto)
                totaldeproductos+=cantp
            case 6 :
                total=totalfinal(total,cantp,1600,producto)
                totaldeproductos+=cantp
            case 7 :
                total=totalfinal(total,cantp,12000,producto)
                totaldeproductos+=cantp
    except Exception:
        print("ERROR : HAS INGRESADO TEXTO")
print(f"""El usuario: {nombre}
Lleva  {totaldeproductos} productos

Su total NETO es de {total}

Su total + IVA es de{total*1.19}""")

      