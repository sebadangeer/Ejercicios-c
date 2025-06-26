# Crear gestion de vehiculos
# Crear programa para un parking de autos
# se debe ingresar
# Marca, año, patente, Tipo

# Marca: tipo string, se debe tipear la marca
# año: tipo int , solo de 4 digitos enteros
# patente: debe tener 4 letras minusculas y 2 digitos
# tipo: S= sedan, C= Camioneta, M= moto
# Se deve validar cada aspecto y tener un mantenedor para 
# todos los vehiculos motorizados
# 1.- Ingresar Vehiculo
# 2.- Mostrar Vehiculos
# 3.- Actualizar Vehiculo
# 4.- Borrar Vehiculo
# 5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
# 6.- Salir
Gestion_de_Vehiculos = {}
listadevehiculos=["Sedan","Camioneta","Moto"]
numerodevehiculo=1
def cero_autos(total):
    if len(total)==0:
        print("No existen vehiculos")   
def mostrarvehiculos():
    for key , value in Gestion_de_Vehiculos.items():
        print(key,value)
def funcionanal():
    while True :
        try:
            Año=int(input("Ingrese el año del vehiculo a registrar"))
            if len(str(Año))==4 :
                print("El año del vehiculo a sido ingresado con exito ")
                break
            else:
                print("El año no cumple con la normativa establecida")
        except Exception:
            print("Error intentelo nuevamente")
    return Año
def funcionpatentada():
    while True:
        try:
            Patentenueva=str(input("Ingrese la patente a registrar"))
            digitos=0
            minus=0
            for i in Patentenueva:
                if i.isdigit():
                    digitos+=1
                if i.islower():
                    minus+=1
            if digitos==2 and minus==4 and len(Patentenueva)==6 :
                print("Su patente a sido ingresada con exito")
                break
            else : 
                print("Error al ingresar la patente")
        except Exception:
            print("Error")
    return Patentenueva
def funcionvehicular():
    while True:
        try:
            Tipo_de_vehiculo=int(input("""
            1.-SEDAN
            2.-CAMIONETA
            3.-MOTO
                Ingrese el tipo de vehiculo a registrar : """))+1
            tipo=listadevehiculos[Tipo_de_vehiculo]
            break
        except Exception:
            print("Error ingrese un vehiculo valido")
    return tipo
while True:
    try:
        quedeseahacer=int(input("""
 1.- Ingresar Vehiculo
 2.- Mostrar Vehiculos
 3.- Actualizar Vehiculo
 4.- Borrar Vehiculo
 5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
 6.- Salir
        Ingrese una opcion : """))
        match quedeseahacer:
            case 1 :
                marcanueva=str(input("Ingrese la marca del vehiculo a registrar"))
                Año=funcionanal()
                Patentenueva=funcionpatentada()
                tipoaañadir=funcionvehicular()
                Gestion_de_Vehiculos[numerodevehiculo]={"Tipo":tipoaañadir,
                                                            "Año":Año,
                                                            "Patente":Patentenueva,
                                                            "Marca":marcanueva}
                numerodevehiculo+=1
            case 2 :
                if len(Gestion_de_Vehiculos)==0:
                    print("No hay vehiculos para mostrar")
                else:
                    mostrarvehiculos()
            case 3 :
                if len(Gestion_de_Vehiculos)==0:
                    print("No hay vehiculos para actualizar")
                else:
                    mostrarvehiculos()
                    while True:
                        try:
                            vehiculoaactualizar=int(input("Ingrese el numero del vehiculo a actualizar : "))
                            if vehiculoaactualizar in Gestion_de_Vehiculos:
                                while True:
                                    try:
                                        infoaactualizar=int(input("""
                1.-Tipo
                2.-Año
                3.-Patente
                4.-Marca
                    Ingrese una opcion : """))
                                        match infoaactualizar:
                                            case 1:
                                                tipoaañadir=funcionvehicular()
                                                Gestion_de_Vehiculos[vehiculoaactualizar]["Tipo"]=tipoaañadir
                                                break
                                            case 3:
                                                Patentenueva=funcionpatentada()
                                                Gestion_de_Vehiculos[vehiculoaactualizar]["Patente"]=Patentenueva
                                                break
                                            case 4:
                                                marcanueva=str(input("Ingrese la marca del vehiculo a registrar"))
                                                Gestion_de_Vehiculos[vehiculoaactualizar]["Marca"]=marcanueva
                                                break
                                            case 2:
                                                año=funcionanal()
                                                Gestion_de_Vehiculos[vehiculoaactualizar]["Año"]=año
                                                break
                                            case _:
                                                print("Ingrese una opcion valida")
                                    except Exception:
                                        print("Error intentelo nuevamente")
                            else:
                                print("El vehiculo no existe")
                            break
                        except Exception:
                            print("Ingrese un numero valido")
            case 4:
                if len(Gestion_de_Vehiculos)==0:
                    print("No hay vehiculos para eliminar")
                else:
                    while True:
                        try:
                            mostrarvehiculos()
                            vehiculoaborrar=int(input("Ingrese el numero de vehiculo a borrar"))
                            if vehiculoaborrar in Gestion_de_Vehiculos:
                                del Gestion_de_Vehiculos[vehiculoaborrar]
                                print("Vehiculo eliminado")
                                break
                            else:
                                print("ingrese un vehiculo para borrar")
                        except Exception:
                            print("Ingrese una opcion valida")
            case 5:
                if len(Gestion_de_Vehiculos)==0:
                    print("Aun no hay vehiculos")
                else:
                    print("El ultimo vehiculo ingresado es ", Gestion_de_Vehiculos[numerodevehiculo], " El total de vehiculos ingresados es de ",len(Gestion_de_Vehiculos))
            case 6:
                print("Saliendo")
                break
    except Exception:
        print("Ingrese una opcion valida")
