print("Cuantos desean saber su promedio")
cant=int(input())
for i in range(cant):
    print("ingrese sus notas ")
    n1=float(input())
    n2=float(input())
    n3=float(input())
    total=(n1+n2+n3)/3
    if total>=4.0:
        print("pasaste bro", total)
    else:
        print("reprobaste por que tu promedio es ", total)