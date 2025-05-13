from random import randint
import time
vida_de_jugador1=50
vida_de_jugador2=50
turno=0
jugador1=str(input("Ingrese nombre de jugador 1 : "))
time.sleep(1)
jugador2=str(input("ingrese nombre de jugador 2 : "))
while vida_de_jugador1>=0 and vida_de_jugador2>=0:
    if turno%2==0:
        print(jugador1,"▄"*vida_de_jugador1,vida_de_jugador1,"50","                    ",jugador2,"▄"*vida_de_jugador2,vida_de_jugador2,"50")
        print("Turno de ",jugador1)
        time.sleep(1)
        ataque=randint(3,15)
        critico=randint(1,5)
        if critico==2:
            ataque*=2
            print("Has realizado un critico , ", jugador2 , " a recibido ",ataque," de daño" )
            vida_de_jugador2=vida_de_jugador2-ataque
        else:
            print("Has realizado un ataque normal , ", jugador2 , " a recibido ",ataque," de daño" )
            vida_de_jugador2=vida_de_jugador2-ataque
    else:
        print(jugador1,"/"*vida_de_jugador1,vida_de_jugador1,"50","                    ",jugador2,"/"*vida_de_jugador2,vida_de_jugador2,"50")
        print("Turno de ",jugador2)
        time.sleep(1)
        ataque=randint(3,15)
        critico=randint(1,5)
        if critico==2:
            ataque*=2
            print("Has realizado un critico , ", jugador1 , " a recibido ",ataque," de daño" )
            vida_de_jugador1=vida_de_jugador1-ataque
        else:
            print("Has realizado un ataque normal , ", jugador1 , " a recibido ",ataque," de daño" )
            vida_de_jugador1=vida_de_jugador1-ataque
    turno+=1
print(jugador1,"/"*vida_de_jugador1,"                    ",jugador2,"/"*vida_de_jugador2)
if vida_de_jugador1>vida_de_jugador2:
    print("El jugador",jugador1,"a ganado")
else:
    print("El jugador",jugador2,"a ganado")