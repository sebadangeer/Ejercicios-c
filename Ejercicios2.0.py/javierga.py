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
saldo=500000
while True:
    try:
        opc=int(input("""Menu
            1.- Pago de Credito
            2.- Simulacion de compras
            3.- Consulta de Saldo
            4.Salir
            """))
        match opc:
            case 1:
                print("Usted tiene una deuda de $ ",deuda)
                op2=int(input("""Desea pagar o volver al menu
                              1.- Pagar
                              2.- Volver al menu
                              """))
                if op2==1:
                    pago_credito=int(input("Ingrese el monto que va a pagar : "))
                    while pago_credito<0 and pago_credito<=deuda:
                        print("Ingrese un monto valido")
                        pago_credito=int(input("""Ingrese 1 para salir
                        Ingrese el monto que va a pagar : """))
                        if pago_credito==1:
                            print("No quiere pagar nada")
                            break    
                    deuda=deuda-pago_credito
                    saldo=saldo+pago_credito
                    print("Su saldo es $ ", saldo)
                    print("Su deuda es $ ", deuda)
                if op2==2:
                    print("")
            case 2:
                compra=int(input("Ingrese el monto a pagar"))
                if compra<=saldo:
                    print("Pago realizado con exito")
                    saldo=saldo-compra
                    deuda=deuda+compra
                else:
                    print("Su saldo no es suficiente")
            case 3:
                print("Su saldo es $ ", saldo)
            case 4:
                print("Saliendo...")
                break
            case _ :
                print("Opcion invalida")
                


    except:
        print("Ingrese un valor valido")