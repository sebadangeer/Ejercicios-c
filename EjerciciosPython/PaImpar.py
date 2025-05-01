par=0
impar=0
cantn=int(input("ingrese la cant de numeros que desea saber: "))
for i in range(cantn):
    duda=int(input("ingrese un numero para saber si es par o impar: "))
    if duda%2==0:
        par+=1
        print("su numero es par")
    else:
        impar+=1
        print("su numero es impar")
print(f"""su total de pares es{par}
su total de impares es{impar}""")