cont=0
total=0
numero=0
print("""Bienvenido a mi calculadora
Para usarla se le pedira ingresar un primer numero, luego el operador aritmetico
Y luego queda ingresar el numero que realizara la operacion,
Podra hacer calculos hasta que operador aritmetico sea = "salir""")
numero=float(input("Ingrese un numero : "))
total+=numero
while numero!="x":
   if cont>=1:
        print("                   \/")
        print("                   ", total)
   operadoraritmetico=(input("Ingrese operador  : "))
   if operadoraritmetico== "salir":
        break
   numero=float(input("Ingrese un numero : "))
   dicc={
    "+": total+numero,
    "-": total-numero,
    "*": total*numero,
    "/": total/numero
}
   total= dicc[operadoraritmetico]
   cont+=1

print("El total final es de : ", total)