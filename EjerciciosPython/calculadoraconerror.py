print("Bienvenido a mi calculadora")
print("Ingrese X cuando se le pida operador aritmetico para salir")
total=0
while True:
    try:
        n1=int(input("Ingrese un numero : "))
        operador=input("Ingrese un operador aritmetico : ")
        if operador=="x":
            break
        n2=int(input("Ingrese un numero : "))
        match operador:
            case "+":
                total+=n1+n2
            case "-":
                total+=n1-n2
            case "*":
                total+=n1*n2
            case "/":
                total+=n1/n2
        print(total)
    except Exception:
        print("Ingrese los valores de forma correcta")
print(total)