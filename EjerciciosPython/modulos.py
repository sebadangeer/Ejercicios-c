from funcsuper import totalfin
print("Usted a ingresado a autoservice SEVoN")
total=0
totalx=0
producto=0
while producto != 10:
    print(f"""
Su total actual es de:{total}

/Que desea llevar/

1.-Papas fritas
2.-Vinagre
3.-Fosforos
4.-Salsa de tomate
5.-Tallarines
6.-Toalla nova
7.-Cargador de celular

""")
    producto=int(input("ingrese numero de producto:"))
    if producto==10:
        break
    cantp=int(input("ingrese cantidad de producto: "))
    match (producto):
        case 1 :
            total+=totalfin(totalx,cantp,1000,producto)
        case 2 :
            total+=totalfin(totalx,cantp,1300,producto)
        case 3 :
            total+=totalfin(totalx,cantp,300,producto)
        case 4 :
            total+=totalfin(totalx,cantp,800,producto)
        case 5 :
            total+=totalfin(totalx,cantp,1100,producto)
        case 6 :
            total+=totalfin(totalx,cantp,1600,producto)
        case 7 :
            total+=totalfin(totalx,cantp,12000,producto)      
print("su total es de",total)