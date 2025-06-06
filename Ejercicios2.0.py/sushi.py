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
pik=0
otaku=0
pulpo=0
anwila=0
codigo="Matichupalo"
codigo_usuario=""
def compra():
    global pik,otaku,pulpo,anwila,total
    print("que desea llear ctm")
    while True:
        try:
            opc=int(input("""Elija un producto
 1. Pikachu Roll $4500
 2. Otaku Roll $5000
 3. Pulpo Venenoso Roll $5200
 4. Anguila Eléctrica Roll $4800 
 5.Dejar de comprar   
ingrese una opc :             """))
            match opc:
                case 1:
                    pik+=1
                    total+=4500
                case 2:
                    otaku+=1
                    total+=5000
                case 3:
                    pulpo+=1
                    total+=5200
                case 4:
                    anwila+=1
                    total+=4800
                case _ :
                    print("Ingrese una de las opc disponibles")
            if opc==5:
                print("Volviendo al menú")
                break
        except Exception:
            print("Ingrese una opc valida")
def pago ():
    while True:
        try:
            confirmacion=int(input("""Tiene codigo de descuento
        1.-SI 
        2.-NO
                
        Ingrese una opcion : """))
            break
        except Exception:
            print("Ingrese numeros")
    if confirmacion==1:
        while True:
            codigo_usuario=str(input("""Para salir ingrese x                
    Ingrese su codigo de descuento : """))
            if codigo_usuario==codigo:
                descto=total*0.10
                print(f"""
        ******************************
TOTAL PRODUCTOS:{otaku+pik+anwila+pulpo}
******************************
Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023 5
Pikachu Roll : {pik}
Otaku Roll : {otaku}
Pulpo Venenoso Roll: {pulpo}
Anguila Eléctrica Roll: {anwila}
******************************
Subtotal por pagar: ${total}
Descuento por código: $ {descto}
TOTAL: ${total-descto}
              """)
                break
            if codigo_usuario=="x":
                    print(f"""
        ******************************
TOTAL PRODUCTOS:{otaku+pik+anwila+pulpo}
******************************
Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023 5
Pikachu Roll : {pik}
Otaku Roll : {otaku}
Pulpo Venenoso Roll: {pulpo}
Anguila Eléctrica Roll: {anwila}
******************************
Subtotal por pagar: ${total}
Descuento por código: $0
TOTAL: ${total}
              """)
                    break

    else:
        print(f"""
        ******************************
TOTAL PRODUCTOS:{otaku+pik+anwila+pulpo}
******************************
Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023 5
Pikachu Roll : {pik}
Otaku Roll : {otaku}
Pulpo Venenoso Roll: {pulpo}
Anguila Eléctrica Roll: {anwila}
******************************
Subtotal por pagar: ${total}
Descuento por código: $0
TOTAL: ${total}
              """)
while True:
    try:
        opciones=int(input("""Bienvenido a sushilospajitas
    Que desea hacer
                     
    1 comprar
    2 pagar"""))
        match opciones:
            case 1:
                compra()
            case 2:
                pago()
                break
            case _ :
                print("Ingrese una opc valida ctm")
    except Exception:
        print("Ingrese un valor entero")
