print("Usted a ingresado a autoservice SEVIN")
producto=0
total=0
pf=1000
vn=1500
fosf=300
tmt=800
tal=1000
tno=700
carg=10000
while producto!="nada mas":
    print("")
    print("su total actual es de:",total)
    print("")
    print("/que desea llevar/")
    print("")
    print("papas fritas")
    print("vinagre")
    print("fosforos")
    print("salsa de tomate")
    print("Tallarines")
    print("toalla nova")
    print("cargador de celular")
    print("")
    print("para salir escriba exit en la terminal")
    print("")
    producto=(input("ingrese nombre de producto:"))
    if producto=="papas fritas":
        print("usted lleva papas fritas")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+pf*cantp
    if producto=="vinagre":
        print("usted lleva vinagre")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+vn*cantp
    if producto=="fosforos":
        print("usted lleva fosforos")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+fosf*cantp
    if producto=="salsa de tomate":
        print("usted lleva salsa de tomate")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+tmt*cantp
    if producto=="tallarines":
        print("usted lleva tallarines")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+tal*cantp
    if producto=="toalla nova":
        print("usted lleva toalla nova")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+tno*cantp
    if producto=="cargador de celular":
        print("usted lleva un cargador de celular")
        cantp=int(input("ingrese cantidad de producto: "))
        total=total+carg*cantp
    if producto=="exit":
        break
print("su total es de",total)

    


