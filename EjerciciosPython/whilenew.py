opc=""
total=0
totalnum=0
totalsuma=0
while opc!="si":
    numero=int(input("ingrese el numero que desea sumar: "))
    total+=1
    totalsuma+=numero
    opc=input(f"su total es de {totalsuma} desea salir?: ")
    opc=opc.lower()
print(f"el total de su suma es de",totalsuma )
print(f"el total numeros sumados fue de",total)