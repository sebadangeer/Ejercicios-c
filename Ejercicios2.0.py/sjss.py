cantidad={1:0,2:0,3:0,4:0}
valor={1:4500,2:5000,3:5200,4:4800}
nombre={1:"Pikachu roll",2:"Otaku roll",3:"Pulpo venenoso roll",4:"Anguila electrica"}
total=0
codigo="jsjs"
descto=0
def boleta(desto):
            print(f"""
        ******************************
TOTAL PRODUCTOS:{cantidad[1]+cantidad[2]+cantidad[3]+cantidad[4]}
******************************
Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023 5
Pikachu Roll : {cantidad[1]}
Otaku Roll : {cantidad[2]}
Pulpo Venenoso Roll: {cantidad[3]}
Anguila Eléctrica Roll: {cantidad[4]}
******************************
Subtotal por pagar: ${total}
Descuento por código: ${desto}
TOTAL: ${total-desto}
              """)
def compra ():
    while True:
        global total
        while True:
            try:
                quelleva=int(input("""Que desea llevar
 1. Pikachu Roll $4500
 2. Otaku Roll $5000
 3. Pulpo Venenoso Roll $5200
 4. Anguila Eléctrica Roll $4800
5.salir
Ingrese opc : """))
                break
            except Exception:
                print("Ingrese solo numeros...")
        if quelleva==5:
            print("Saliendo")
            break
        elif quelleva>0 and quelleva<6:
            cantidad[quelleva]+=1
            total+=valor[quelleva]
            print(cantidad)
            print(total)
        else:
            print("Ingrese una opc valida")
def pago ():
    global descto
    while True:
        try:
            confirmacion=int(input("""Tiene codigo de descuento
        1.-SI 
        2.-NO     
        Ingrese una opcion : """))
            break
        except Exception:
            print("Ingrese un numero")
    if confirmacion==1:
        while True:
            codigo_usuario=str(input("""Para salir ingrese x                
    Ingrese su codigo de descuento : """))
            if codigo_usuario==codigo:
                descto=total*0.10
                boleta(descto)
                break
            if codigo_usuario=="x":
                boleta(descto)
                break
    else:
        boleta(descto)
while True:
    while True:
        try:
            opcion=int(input("""
    1.-Compra
    2.-Pago
        Ingrese una opcion : """))
            break
        except Exception:
            print("Ingrese un numero ")
    match opcion:
        case 1:
            compra()
        case 2:
            pago()
            break
        case _ : 
            print("Opción Invalida)")