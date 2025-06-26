Alumno={"Seba":[],"Diego":[]}
#Tarea
##Crear programa de manejo de notas

# 1.-Ingresar Nota
# 2.-Borrar nota
# 3.-Motrar notas
# 4.-Sacar promedio, nota mayor a menor
# 5.-Limpiar notas
# 6.-Salir
while True:
    Que_alumno_desea_ver=str(input("""Ingrese el nombre del alumno : """))
    if Que_alumno_desea_ver in (Alumno):
        while True:
                quedeseahacer=int(input("""
 1.-Ingresar Nota
 2.-Borrar nota
 3.-Motrar notas
 4.-Sacar promedio, nota mayor a menor
 5.-Limpiar notas
 6.-Salir
"""))
                match quedeseahacer:
                    case 1:
                        while True:
                            try:
                                nota=float(input("Ingrese la nota a añadir : "))
                                if nota>=1 and nota<=7:
                                    Alumno[Que_alumno_desea_ver].append(nota)
                                    print(Alumno[Que_alumno_desea_ver])
                                    break
                                else:
                                    print("Ingrese una nota valida")
                            except Exception:
                                print("Su nota a sido mal ingresada")
                    case 2:
                        var=0
                        for i in (Alumno[Que_alumno_desea_ver]):
                            print(f"{var+1}.- {Alumno[Que_alumno_desea_ver][var]}")
                            var+=1
                        notaaborrar=int(input("Ingrese la nota a borrar : "))-1
                        print("La nota a sido eliminada con exito")
                    case 3 :
                        if len(Alumno[Que_alumno_desea_ver]) <0:
                            var=0
                            for i in (Alumno[Que_alumno_desea_ver]):
                                print(Alumno[Que_alumno_desea_ver][var])
                                var+=1
                        else:
                            print("El alumno no tiene notas registradas")
                    case 4 :
                        promedio=0
                        for i in (Alumno[Que_alumno_desea_ver]):
                            promedio+=i
                        promedio=promedio/len(Alumno[Que_alumno_desea_ver])
                        print(f"El promedio del Alumno {Que_alumno_desea_ver} es {promedio}")
                        print(min(Alumno[Que_alumno_desea_ver]))
                        print(max(Alumno[Que_alumno_desea_ver]))
                    case 5:
                        Alumno[Que_alumno_desea_ver]=[]
                    case 6:
                        print("Saliendo")    
                        break            

    else:
        print("El alumno no forma parte de sus registros")
