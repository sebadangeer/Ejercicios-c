carrito=[]
precio={1:200,2:1000,3:700,4:1500,5:4900}
producto={1:"Cigarro",2:"Papas fritas",3:"Doritos",4:"Ketchup",5:"Cajetilla de cigarros"}
cantidad={1:5,2:3,3:8,4:2,5:7}
total=0
while True:
    try:
        opcion=int(input("""Menú supermercado
1.-Comprar
2.-Ver carrito
3.-Registrar mi boleta
"""))
        match opcion:
            case 1:
                var=1
                for i in enumerate(producto):
                    print(f"""{var}.- {producto[var]} ${precio[var]} 
Cantidad de producto:{cantidad[var]}""")
                    var+=1
                    print(""" 
                          """)
                while True:
                    try:
                       quedesea=int(input("Ingrese un numero de producto : "))
                       if quedesea in (producto):
                           break
                       else:
                           print("Ingrese un producto valido")
                    except Exception:
                        print("Ingrese un numero entero")
    except Exception:
        print("Ingrese una opc valida")
