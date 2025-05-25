import random
import time
cajero=str(input("""En que modo estara el cajero
on
off
Ingrese modo:"""))
time.sleep(1)
cantidadde5=30
cantidadde10=30
cantidadde20=30
def retiros (user,dinero,saldodeusuario,usuarioscreados,dineroaentregar):
    intentos=1
    global cantidadde5
    global cantidadde10
    global cantidadde20
    saldototaldelcajeronuevo=cantidadde5*5000+cantidadde10*10000+cantidadde20*20000
    claveingresada=int(input("Ingrese su clave de 4 digitos : "))
    time.sleep(1)
    while claveingresada!=usuarioscreados[user]and intentos!=3:
            time.sleep(1)
            print("Clave invalida")
            claveingresada=int(input("Ingrese su clave de 4 digitos : "))
            intentos+=1
            if intentos==3:
                 print("Has excedido el numero de intentos")
                 time.sleep(1)
                 break
    if claveingresada==usuarioscreados[user]:
        print("Usuario su saldo total es", saldodeusuario[user])
        cash_need=str(input("Cuanto dinero desea sacar : "))
        if cash_need=="0":
            print("Ingrese monto")
            cash_need=str(input("Cuanto dinero desea sacar : "))
        for i in str(cash_need):
            dinero+=i
        if dinero[-1] in "123456789":
            print()
        elif dinero[-2] in "123456789":
            print()
        elif dinero[-3] in "123456789":
            print()
        elif dinero[-4] in "12346789":
            print()
        else:
            cash_need=int(cash_need)
            while cash_need>saldodeusuario[user] or saldototaldelcajeronuevo<cash_need:
                print("el saldo solicitado no esta disponible")
                cash_need=int(input("Cuanto dinero desea sacar : "))
                cash_need=(cash_need)
            if cash_need<=saldototaldelcajeronuevo and saldodeusuario[user]>=cash_need:
                while cash_need!=dineroaentregar:
                        billde20=random.randint(0,cantidadde20)
                        billetesde20=billde20*20000
                        billde10=random.randint(0,cantidadde10)
                        billetesde10=billde10*10000
                        billde5=random.randint(0,cantidadde5)
                        billetesde5=billde5*5000
                        dineroaentregar=billetesde5+billetesde10+billetesde20     
        if cash_need==dineroaentregar:
            print("Se le han dado", billde5,"billetes de 5, ",billde10,"billetes de 10","y ", billde20, "billetes de 20")
            saldodeusuario[user]=saldodeusuario[user]-dineroaentregar
            print("Su saldo total es de : ", saldodeusuario[user])
            cantidadde5-=billde5
            cantidadde10-=billde10
            cantidadde20-=billde20
            saldototaldelcajeronuevo=cantidadde5*5000+cantidadde10*10000+cantidadde20*20000
            print("En el cajero quedan ", saldototaldelcajeronuevo)
            print("Que tenga buen dia")
        else:
            print("El monto solicitado no esta disponible")
            print("El saldo de este cajero es de  :",saldototaldelcajeronuevo)
            print("Usted no pudo sacar dinero")
    return saldodeusuario,cantidadde5,cantidadde10,cantidadde20
dinero1=[]
lista_de_usuarios=[215852385,140220965,106460655]
saldodeusuario1={215852385:500000,140220965:150000,106460655:700000}
usuarioscreados1={215852385:1852,140220965:5678,106460655:2222}
dineroaentregar1=0
while cajero=="on":
    usuario=int(input("""          
Este cajero solo puede retirar multiplos de $5000
Bienvenido usuario            
        Ingrese su rut: """))
    if usuario==1:
        break
    if usuario in lista_de_usuarios:
            match usuario:
                case 215852385:
                    variable=retiros(usuario,dinero1,saldodeusuario1,usuarioscreados1,dineroaentregar1)
                case 140220965:
                    variable=retiros(usuario,dinero1,saldodeusuario1,usuarioscreados1,dineroaentregar1)
                case 106460655:
                    variable=retiros(usuario,dinero1,saldodeusuario1,usuarioscreados1,dineroaentregar1)
    else:
        print("Usuario incorrecto o inexistente")