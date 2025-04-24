print("hola usuario ingrese sus notas")
n1=float(input("su primera nota es:"))
n2=float(input("su segunda nota es:"))
n3=float(input("su tercera nota es:"))
total=(n1+n2+n3)/3
if total>=4.0:
    print("pasaste bro", total)
else:
    print("reprobaste por que tu promedio es ", total)