print("Vamos a calcular tu puntaje de credito")
credito=0
ingreso_mensuales=int(input("Ingrese sus ingresos mensuales : "))
if ingreso_mensuales>=500000 and ingreso_mensuales<=1000000:
    credito+=300000
elif ingreso_mensuales>=1000000 and ingreso_mensuales<=1500000:
    credito+=650000
elif ingreso_mensuales>=1500000:
    credito+=1000000
nivel_educacional=int(input("""Su nivel educacional es :
1.-Basico   : 1 %
2.-Media    : 1.3 %
3.-Superior : 1.5 %

Ingrese una opc : """))

if nivel_educacional== 1:
        print("Su nivel educacional es Basico")
elif nivel_educacional== 2:
        print("Su nivel educacional es Media")
        credito*=1.3
elif nivel_educacional==3:
        print("Su nivel educacional es Superior")
        credito*=1.5
nacionalidad=int(input("""
1.-Chileno
2.- Veneco
ingrese nacionalidad : """))

nacionalidad=nacionalidad.lower()
if nacionalidad==1:
    credito+=300000
    print("Su total de credito es : ", credito )
elif nacionalidad==2:
    print("Su total de credito es : ", credito )