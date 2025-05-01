print("Cuantos desean saber su promedio")
def promedio(nota1,nota2,nota3):
    total=nota1+nota2+nota3
    total=total/3
    total=round(total,1)
    return total
cant=int(input())
for i in range(cant):
    print("ingrese sus notas ")
    n1=float(input())
    n2=float(input())
    n3=float(input())
    notafinal=promedio(n1,n2,n3)
    if notafinal>=4.0:
        print("pasaste bro", notafinal)
    else:
        print("reprobaste por que tu promedio es ", notafinal)