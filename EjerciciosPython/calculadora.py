print("bienvenido a la calculadora de sebita")

n1=float(input("ingrese un numero:"))
n2=float(input("ingrese un numero:"))
n3=float(input("ingrese un numero:"))
resp=int(input("""que desea hace con el numero
1-Suma
2-Restar
3-Multiplicar
4-Dividir
Ingrese Opcion: """))
dicc={
    1:n1+n2+n3,
    2:n1-n2-n3,
    3:n1*n2*n3,
    4:n1/n2/n3
}
print("el resultado es",dicc[resp])
