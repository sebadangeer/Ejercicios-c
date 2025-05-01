import random
numero_user=0
while numero_user<=50:
    multiplo=random.randint(2,8)
    numero_user=int(input("ingrese un numero: "))
    numero_user=numero_user*multiplo
    print("su multiplo al azar es de ",multiplo)
    print("Su total es de ", numero_user)
    if numero_user>50:
        print("Has llegado a la meta")
    else:
        print("no has llegado a la meta")