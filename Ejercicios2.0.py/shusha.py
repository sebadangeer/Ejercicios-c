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

while True:
    quedeseahacer=int(input("""Que desea hacer:
        1.-Comprar
        2.-Ver total
        3.-Ingresar descuento
        4.-ir a pagar
        5.-salir"""))
    if quedeseahacer==1:
        cuantossushis=int(input("Cuantos sushis desea llevar : "))
        for i in range(cuantossushis):
            quesushillevara=int(input("""Que tipo de sushi quiere
        # 1. Pikachu Roll $4500
        # 2. Otaku Roll $5000
        # 3. Pulpo Venenoso Roll $5200
        # 4. Anguila Eléctrica Roll $4800
        # Ingrese una opc : """))
            if quesushillevara==1:
                print("Usted lleva pkchuroll")
                total=total+4500
            elif quesushillevara==2:
                print("Usted lleva otaku roll")
                total=total+5000
            elif quesushillevara==3:
                print("Usted lleva Pulpo venenoso roll")
                total=total+5200
            elif quesushillevara==4:
                print("Usted lleva otaku roll")
                total=total+4800
            else:
                print("La opcion no es valida")
        print("Pedido tomado con exito")
    if quedeseahacer==2:
        print("Su total es de $",total)
    if quedeseahacer==3:
        possecodigo=int(input("""Usted posee codigo
        1.-si
        2.-No"""))
        codigo="soygay"
        codigousuario=str(input("Ingrese su codigo :"))
        while codigousuario!=codigo:
            codigousuario=str(input("Ingrese su codigo :"))

        if codigousuario==codigo:
            print("Codigo valido")
            total=total*0.90
            print("Su total es de", total)
        else:
            print("Codigo invalido como los niños de teleton")
            print("Su total es de", total)
    if quedeseahacer==4:
        