usuario1=None
usuario2=None
usuario3=None
contraseña1=None
contraseña2=None
contraseña3=None
usuarioscreados=0
clave_de_acceso=2345
def crear_usuarios(usuario,contraseña):
    global usuarioscreados
    while True:
        try:
            print("""Ingresando a registro de un usuario........
    Presione x para salir y no crear usuario.""")
            usuario=str(input("""Ingrese el nombre del usuario : """))
            if usuario=="x":
                print("Volviendo al menú")
                usuario=None
                break
            contraseña=str(input("Ingrese la clave del usuario : "))
            while True:
                try:
                    confirmacion=int(input(f"""Su usuario sera {usuario} 
Su contraseña sera {contraseña}
        El usuario es correcto?
        1.-Si
        2.-No
        Ingrese una opcion : """))
                    break
                except Exception:
                    print("Ingrese una opcion valida")
            if confirmacion==1:
                print("Usuario creado correctamente")
                usuarioscreados+=1
                break
            if confirmacion==2:
                print("Volviendo a crear el usuario...")
        except Exception:
            print("Ingrese un valor valido")
    return usuario, contraseña
while True:
    try:
        opcion=int(input("""Bienvenido al menú de registro de usuarios")
    1.-Iniciar sesion
    2.-Registrar usuario
    3.-Ver usuarios creados
    4.-Salir
    Ingrese numero de opcion : """))
        match opcion:
            case 1:
                if usuarioscreados==0:
                    print("No hay usuarios creado...Volviendo al menú")
                else:
                    print("")
            case 2:
                if usuarioscreados<=3:
                    while True:
                        try:
                            print("""
        Desea crear un usuario?
        1.-Si
        2.-No""")    
                            creacion=int(input("Ingrese un valor numerico : "))
                            if creacion==1:
                                if usuarioscreados==0:
                                    usuario1, contraseña1=crear_usuarios(usuario1,contraseña1)
                                    break
                                if usuarioscreados==1:
                                    usuario2, contraseña2=crear_usuarios(usuario2,contraseña2)  
                                    break                  
                                if usuarioscreados==2:
                                    usuario3, contraseña3=crear_usuarios(usuario3,contraseña3)
                                    break
                            if creacion==2:
                                print("Volviendo al menú")
                                break
                            if creacion!=1 and creacion!=2:
                                print("INgrese una opcion valida")
                        except Exception:
                            print("ERROR....Ingrese lo que se le solicita")
                else:
                    print("Ya no puede seguir creando usuarios...")
            case 4 :
                print("Saliendo")
                break
            case 3 :
                print("Para esto necesita clave de acceso") 
                while True:
                    try:
                        claveuser=int(input("Ingrese la clave de acceso"))
                        break
                    except Exception:
                        print("Error en la clave")
                if claveuser==clave_de_acceso:
                    print(f"""
    Los usuarios creados son :
                          
    1.-{usuario1}
    2.-{usuario2}
    3.-{usuario3}
    """)
                else:
                    print("Solo Tiene un intento...volviendo al menú")
            case _ :
                print("Ingrese una opcion válida") 
    except Exception:
        print("Ingrese los valores que se le piden")
