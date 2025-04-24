cantn=int(input("ingrese cantidad de numeros:"))
total=0
for i in range(cantn):
    numero=int(input("INGRESE EL numero:"))
    print(("que desea hacer con el numero"))
    print("+")
    print("-")
    print("*")
    print("/")
    print("x para salir")
    operadoraritmetico=(input(""))
    if operadoraritmetico=="+":
        total=total+numero
        print("su total es ", total)
    if operadoraritmetico=="/":
        total=total/numero
        print("su total es ", total)
    if operadoraritmetico=="*":
        total=total*numero
        print("su total es ", total)
    if operadoraritmetico=="-":
        total=total-numero
        print("su total es ", total)
    if operadoraritmetico=="x":
        print("salir)")
        break