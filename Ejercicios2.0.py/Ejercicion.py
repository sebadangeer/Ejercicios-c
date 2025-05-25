# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá
# ingresarlo. Si el código ingresado es “soygay”, debe realizar un 10% de descuento al total del pedido, en caso
# contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
# tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la
# cantidad de cada uno de ellos y si aplica o no el descuento
total=0
productos=0
carrito=[]
precio=[]
totalcondescuento=0
while True:

    print("Bienvenido a Sushitumare")
    Opc=int(input("""Que desea realizar:
1.-Comprar
2.-Ver mi carrito
3.-Ir a pagar
                  
Ingrese opcion :"""))
    match Opc:
        case 1 :
            while True:
                Compra=int(input("""Que desea llevar :
        1. Pikachu Roll $4500
        2. Otaku Roll $5000
        3. Pulpo Venenoso Roll $5200
        4. Anguila Eléctrica Roll $4800
        5.  Volver al menú

        Ingrese codigo de producto :"""))
                match Compra:
                    case 1 :
                        print("Pikachu roll $4500")
                        total+=4500
                        carrito.append("Pikachu roll")
                        precio.append(4500)
                        productos+=1
                    case 2 :
                        print("Otaku roll $5000")
                        total+=5000
                        carrito.append("Otaku roll")
                        precio.append(5000)
                        productos+=1
                    case 3 :
                        print("Pulpo venenoso roll $4500")
                        total+=5200
                        carrito.append("Pulpo venenoso roll")
                        precio.append(5200)
                        productos+=1
                    case 4 :
                        print("Anguila Electrica roll $4800")
                        total+=4800
                        carrito.append("Anguila Electrica roll")
                        precio.append(4800)
                        productos+=1
                    case 5 :
                        break
                print(f"Usted lleva un total de ${total} ")
                        
        case 2:
            variable=0
            variable2=0
            totalcondescuento=0
            print("Usted lleva los siguientes productos : ")
            for i in range(productos):
                print(f" {i+1}.-{carrito[variable]} $ {precio[variable2]} ")
                variable+=1
                variable2+=1
            print("Su total es de : " ,total)
        case 3:
            op=int(input(f"""Bienvenido a la caja
    
Su total a pagar es de $ {total}

Usted tiene algun codigo de descuento?
1.-Si
2.-No"""))
            if op==1:
                codigoreal="Soyotaku"
                codigouser=str(input("Ingrese su codigo de descuento"))
                while codigouser!=codigoreal:
                    print("""Su codigo de descuento no es valido...
Ingrese x cuando se le solicite el codigo para salir del bucle
o intentelo de nuevo""")
                    codigouser=str(input("Ingrese su codigo de descuento"))
                    if codigouser=="x":
                        break
                totalcondescuento=total*0.10
                print(f"Descuento aplicado , el valor de su descuento es de $",totalcondescuento)
            if op==2:
                print(f"""
******************************
TOTAL PRODUCTOS:{productos}
******************************""")
            variable=0
            variable2=0
            print("Usted lleva los siguientes productos : ")
            for i in range(productos):
                print(f" {i+1}.-{carrito[variable]} $ {precio[variable2]} ")
                variable+=1
                variable2+=1
            print(f"""******************************
            Subtotal por pagar: ${total}
            Descuento por código: {totalcondescuento}
            TOTAL: ${total-totalcondescuento}
                        """)
            salida=int(input("""Desea realizar otra compra
        1.-Si
        2.-No
        Ingrese una opc : """))
            if salida==1:
                print("")
            else:
                break