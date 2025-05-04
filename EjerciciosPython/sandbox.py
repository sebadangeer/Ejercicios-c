#print("que tan grande eres")
#edad=int(input())
#if edad<12:
#    print("eres menor")
#if edad>12 and edad<17:
#    print("eres un adolecente")
#if edad>17:
#    print("eres un adulto")


#clavereal=1234
#print("ingrese una contraseña")
#claveusuario=int(input())
#while claveusuario!=clavereal:
#    print("contraseña incorrecta")
#    claveusuario=int(input())
#print("clave correcta")
#import random
#puntos=random.randint(1,30)
#if puntos>=20:
#    print("usted logro abrir la puerta")
#else:
#    print("aun no puede abrir la puerta")
import random
meta=30
turno=0
j1=0
j2=0
while j1!=30 and j2!=30:
	if turno % 2==0: 
		print("Turno de j1")
		dado=random.randint(1,6)
		print("Lanza el dado y saca ", dado)
		j1=j1+dado
		if j1>30:
			j1=j1-dado
		print("J1 va en a casilla ", j1)
	else:
		print("Turno de j2")
		dado=random.randint(1,6)
		print("Lanza el dado y saca ", dado)
		j2=j2+dado
		if j2>30:
			j2=j2-dado
		print("J2 va en a casilla ", j2)
	turno=turno+1
if j1>j2:
	print("Jugador 1 ha ganado la partida")
else:
	print("Jugador 2 ha ganado la partida")

Numero=7
Numero=5
