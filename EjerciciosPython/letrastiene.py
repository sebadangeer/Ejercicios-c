palabra=input(("ingrese texto para saber cuantos caracteres tiene: "))
letras=0
vocales=0
cons=0
for i in palabra.lower():
    letras+=1
    if i in "aeiou":
        vocales+=1
    elif i==" ":
        print()
    else:
        cons+=1

print("su palabra tiene ",letras, "caracteres")
print(f"La cantidad de vocales es {vocales}")
print(f"La cantidad de consonantes es {cons}")


