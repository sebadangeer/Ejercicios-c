cant=int(input("ingrese cantidad de notas"))
suma=0
for i in range(cant):
    print("ingrese sus notas ")
    notas=float(input())
    suma=suma+notas
prom=suma/cant
print("SU PROMEDIO ES ",prom)
if prom<=4:
    print("reprobaste")
else:
    print("aprobaste")
    