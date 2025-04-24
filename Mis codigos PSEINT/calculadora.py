print("bienvenido a la calculadora de sebita")

n1=float(input("ingrese un numero:"))
n2=float(input("ingrese un numero:"))
n3=float(input("ingrese un numero:"))
print("que desea hace con el numero")
print("1-Suma")
print("2-Restar")
print("3-Multiplicar")
print("4-Dividir")
resp=int(input())
if resp==1:
    print("el resultado es ",n1+n2+n3)
if resp==2:
    print("el resultado es ",n1-n2-n3)
if resp==3:
    print("el resultado es ",n1*n2*n3)
if resp==4:
    print("el resultado es ",n1/n2/n3)

