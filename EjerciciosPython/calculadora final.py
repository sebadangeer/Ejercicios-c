#def calcular (expresion):
#    try:
#        resultado=eval(expresion)
#        return resultado
#   except Exception as e:
#        return str(e)
#expresion=str(input("calculo"))
#resultado=calcular(expresion)
#print(resultado)
total=0
categoria=0
print("Bienvenido al supermercado de Sebita")
while categoria != 4:
    categoria=int(input("""Las categorias disponibles son :
1.-Zapatillas
2.-Poleras
3.-Gorras
4.-Ir al carrito de compras a pagar

Ingrese a la categoria que desea acceder : """))
    if categoria==1:
        print("""Has accedido a la categoria de Zapatillas
1.-Sneakers Mike Mcfly    $30000
2.-Zapatos CaballoTenista $60000
3.-Zapatos Montanbiki     $45000

              """)
        zapatillas=int(input("ingrese una opcion : "))
        if zapatillas==1:
            total+=30000
        elif zapatillas==2:
            total+=60000
        elif zapatillas==3:
            total+=45000
        else:
            print("ERROR AL INGRESAR PRODUCTO")
    elif categoria==2:
        print("""Has accedido a la categoria de Poleras
1.-Polera Jose 26   $15000
2.-Polera Ñaiki     $25000
3.-Polera gutsi     $10000

              """)
        poleras=int(input("ingrese una opcion : "))
        if poleras==1:
            total+=15000
        elif poleras==2:
            total+=25000
        elif poleras==3:
            total+=10000
        else:
            print("ERROR AL INGRESAR PRODUCTO")
    elif categoria==3:
        print("""Has accedido a la categoria de Gorras
1.-Sombrero psico  $30000
2.-Gorra Adios     $35000
3.-Gorra Luviton   $43000

              """)
        gorras=int(input("ingrese una opcion : "))
        if gorras==1:
            total+=30000
        elif gorras==2:
            total+=35000
        elif gorras==3:
            total+=43000
        else:
            print("ERROR AL INGRESAR PRODUCTO")
    elif categoria == 4:
        break
    else :
        print("La categoria seleccionada no existe, intentelo denuevo...")
    print("Usted lleva un total de $", total)
print("El total de su compra es de $",total)