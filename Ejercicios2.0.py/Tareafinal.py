frutas={}
while True:
    try:
        opcion=int(input("""
1.-Ingresar fruta y precio
2.-Actualizar precio
3.-Borrar fruta y precio
4.-Mostrar las frutas y precios

    Ingrese una opcion : """))
        match opcion:
            case 1:
                Nombre=str(input("Ingrese el nombre de la fruta : ")).upper()
                while True:
                    try:
                        Valor=int(input("Ingrese el valor de la fruta : "))
                        frutas[Nombre]=Valor
                        break
                    except Exception:
                        print("Ingrese un monto valido")
            case 2:
                if len(frutas)==0:
                    print("Debe ingresar una fruta para actualizar su precio")
                else:
                    Nombre=input("Ingrese el nombre de la fruta a cambiar su valor : ").upper()
                    if Nombre in frutas:
                        while True:
                            try:
                                Valor=int(input("Ingrese el nuevo valor de su fruta : "))
                                frutas[Nombre]=Valor
                                break
                            except Exception:
                                print("Ingrese un monto valido")
                    else:
                        print("La fruta no existe")
                        break
            case 3 :
                while True:
                    name=str(input(" Ingrese el nombre de la fruta a eliminar :")).upper()
                    if name in frutas:
                        del frutas[name]
                        break
                    else:
                       print("La fruta no existe")
                       break
            case 4:
                if len(frutas)==0:
                    print("Ingrese una fruta antes de eliminar...no sea weon")
                else:
                    for key, value in frutas.items():
                        print(f"- {key} $ {value}")
            case 5:
                print("Saliendo")
                break
            case _ :
                print("Ingrese una opcion valida")
    except Exception:
        print("Ingrese un valor entero")