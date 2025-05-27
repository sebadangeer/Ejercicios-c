#SUPERMERCADO,
#Preguntar al usuario cunatos productos llevra.´,
#escribir listado de 3 productos y sus precios,
#mostrar el total neto de la compra,
#y mostrar el total mas IVA (19%)
total=0
productos=[]
while True:
    try:
        cantidadproductos=int(input("Cuantos productos llevara : "))
        for i in range(cantidadproductos):
            producto=int(input("""Que desea llevar
            1.-Vibrador anal $500
            2.-Pene de dinosaurio $400
            3.-El culo del pablo $200
        Ingrese una opcion: """))
            if producto==1:
                print("Metaselo por la raja")
                total+=500
            if producto==2:
                print("Pene de dinosaurio")
                total+=400
            if producto==3:
                print("Lamalo saboreelo")
                total+=200
            productos.append(2)
            print("El total actual es de $",total)
            print("El total con Ava es de $",total*1.19)
        desea_comprar_mas=int(input("""Desea seguir comprando?: 
                1.-Si
                2.-No"""))
        totalproductos=len(productos)
        print(totalproductos)
        if desea_comprar_mas==1:
            total=0
        else:
            break
    except Exception:
        print("Ingrese un valor valido")
            