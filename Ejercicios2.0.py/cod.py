# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.
# 2
# b. Se debe programar mensajes de error específicos para guiar al
# usuario sobre posibles problemas.
# Instrucciones para el envío de la actividad
deuda=100000
saldo=200000
clave=1234
inventario={1:5,2:3, 3:7}
precios={1:33000,2:40000,3:25000}
total=0
producto={1:"polera",2:"jeans",3:"gorro"}
pago=0
carrito=0
monto_credito=0
def consulta (debe,cupo,opc):
    match opc:
        case 1:
            print(f"usted tiene una deuda de : {debe}")
        case 2:
            print(f"Usted Tiene un cupo disponible de : {cupo}")
def total_a_pagar(valordeproducto,nombredelproducto,numerodeproducto,cupo,carro):
    if cupo>=valordeproducto[numerodeproducto]:
        carro+=valordeproducto[numerodeproducto]
        print("Usted lleva", nombredelproducto[numerodeproducto],"su coste es de  $ ",valordeproducto[numerodeproducto])
    else:
        print("Su saldo no  es suficiente para realizar el pago")
    return carro
def pago_de_deuda(debes,cupo):
    monto_a_pagar=int(input(f"""
Su deuda actual es de $ {debes}  

Este es el menu de pago...

Ingrese 0 si desea volver al menú

Ingrese el monto que desea pagar $ """))
    while monto_a_pagar<0 or monto_a_pagar>=debes:
        if monto_a_pagar==0:
            print("Regresando al menu..............")
            break
        print("Ingrese  un monto valido")
        monto_a_pagar=int(input(f"""
Su deuda actual es de ${debes}                                

Ingrese el monto que desea pagar $ """))
    debes-=monto_a_pagar
    cupo+=monto_a_pagar
    return debes,cupo
while True:
    try:
        opcion=int(input("""Bienvenido al menú ONLINE de su tarjta de crédito " 
            
            Que desea realizar
                
                1.-Acerca de mi tarjeta
                
                2.-Compras
                
                3.-Pago de mi deuda
            
                4.-Salir
    Ingrese una opc : """))
        match opcion:
            case 1:
                acercade=int(input("""
                    1.-Consulta de deuda
                    2.-Saldo                      
                    Que desea saber : """))
                consulta(deuda,saldo,acercade)
            case 2:
                monto_credito=0
                cantp=int(input("Ingrese la cantidad de productos que llevara: "))
                for i in range(cantp):
                    prod=int(input("""Ingrese numero de producto:

                1.-Poleras $33.000
                2.-Jeans $40.000
                3.-Gorro $25.000
                4.-Volver al menú"""))
                    match prod:
                        case 1:
                            pago=total_a_pagar(precios,producto,prod,saldo,carrito)
                            monto_credito+=pago
                        case 2:
                            pago=total_a_pagar(precios,producto,prod,saldo,carrito)
                            monto_credito+=pago
                        case 3:
                            pago=total_a_pagar(precios,producto,prod,saldo,carrito)
                            monto_credito+=pago
                        case 4:
                            break
                print("Su total a pagar es de $ ",monto_credito)
                
                tarjeta=int(input("Ingrese la clave de su tarjeta de credito : "))
                clavereal=1234
                while clavereal!=tarjeta:
                    print("Clave invalida")
                    tarjeta=str(input("""Presione "0" para volver al menú
                                    Ingrese la clave de su tarjeta de credito : """))
                    if tarjeta=="0":
                        break
                if monto_credito<=saldo and tarjeta==clavereal:
                    print("Compra realizada con exito")
                    saldo-=monto_credito
                    deuda+=monto_credito
                else:
                    print("Su saldo no es suficiente para realizar esta compra")

            case 3:
                deuda,saldo=pago_de_deuda(deuda,saldo)
                print(f"""Su deuda actual es de : $ {deuda}
                    El cupo actual de su tarjeta es de : $ {saldo}""")
            case 4:
                print("Saliendo...")
                break
    except Exception:
        print("Ingrese los valores de forma correcta")