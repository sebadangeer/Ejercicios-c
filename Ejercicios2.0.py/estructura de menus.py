while True:
    try:
        opcion=int(input("""opciones
                        opcion 1
                        opcion 2
                        opcion 3
                        opcion de salida"""))
        match opcion:
            case 1:
                print("lo que se hara en la opcion 1 ")
            case 2:
                print("Lo que se hara en la opcion 2 ")
            case 3:
                print("opcion 3 ")
            case 4:
                print("Saliendo")
                break
            case  _:
                print("Opcion invalida")
    except Exception: 
        print("Si pides enteros y escribes numeros ...")