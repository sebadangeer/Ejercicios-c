
letra=(input("ingrese texto y las letras seran contadas:"))
totall=0
total=0
totalv=0
for x in letra:
    if x == " ":
        continue
    if x in "aeiou":
        totalv+=1
    else:
        total+=1
    totall+=1
    quedeseasaber=input("""que desea saber del texto
    1.-vocales
    2.-consonantes
    3.-letras tiene""")
    diccionario={
        1:totalv,
    2:total,
    3:totall
    }
    print(diccionario[quedeseasaber])