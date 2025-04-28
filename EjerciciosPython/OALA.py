palabra=["LISTA","INSANO"]
letras=0
vocales=0
cons=0
for i in palabra:
    letras+=1
    if i in "aeiou":
        vocales+=1
    elif i==" ":
        print()
    else:
        cons+=1
print(i)
print("su palabra tiene ")