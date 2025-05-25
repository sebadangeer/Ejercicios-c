import time
def tiempo():
    time.sleep(1)
while True:
    promediocurso=0
    notasdelcurso=0
    aprobados=0
    reprobados=0
    listadealumnos=[]
    listadealumnosreprobados=[]
    listadealumnosaprobados=[]
    notasdealumnos=[]
    try:
        cantalumnos=int(input("Ingrese la cantidad de  alumnos del 003D : "))
        tiempo()
        for i in range(cantalumnos):
            total=0
            nombredelalumno=input("Ingrese su nombre : ")
            listadealumnos.append(nombredelalumno)
            tiempo()
            print(f"Bienvenido Alumno {nombredelalumno}")
            cantidad_de_notas=int(input("Ingrese su cantidad de notas : "))
            for x in range(cantidad_de_notas):
                promedioalumno=0
                notas=float(input(f"Ingrese la nota {x+1} : "))
                total+=notas
            promedioalumno=total/cantidad_de_notas
            notasdealumnos.append(promedioalumno)
            if promedioalumno>=4:
                tiempo()
                print("El alumno aprobo")
                print(f"Su promedio es de {promedioalumno} ")
                aprobados+=1
                listadealumnosaprobados.append(nombredelalumno)
            else:
                tiempo()
                print("El alumno reprobo")
                print(f"Su promedio es de {promedioalumno} ")
                reprobados+=1
                listadealumnosreprobados.append(nombredelalumno)
            notasdelcurso+=promedioalumno
            promediocurso=notasdelcurso/cantalumnos
        print(f"El promedio general del curso es de {round(promediocurso,1)}")
        totalaprobados=aprobados/cantalumnos
        totalreprobados=reprobados/cantalumnos
        while True:
            tiempo()
            opc=int(input("""
Profesor Robles que desea saber sobre sus alumnos : 
            1.-Lista de alumnos
            2.-Alumnos Aprobados
            3.-Alumnos reprobados
            4.-Salir
                          
Ingrese una opcion : """))
            variable=0
            variable1=0
            if opc==4:
                break
            match opc:
                case 1:
                    for i in (listadealumnos):
                        print(f"{variable+1}.-{i} ({notasdealumnos[variable1]})")
                        variable+=1
                        variable1+=1
                case 2:
                    if totalaprobados==0:
                        print("Lo sentimos Profesor pero nadie aprobo")
                    else:
                        totalaprobados=round(totalaprobados,3)
                        print(f"Los alumnos aprobados son {listadealumnosaprobados} estos equivalen al {totalaprobados*100}% del curso")
                case 3:
                    if totalreprobados==0:
                        print("Felicitaciones Profesor nadie reprobo")
                    else:
                        totalreprobados=round(totalreprobados,3)
                        print(f"Los alumnos reprobados son {listadealumnosreprobados} estos equivalen al {totalreprobados*100}% del curso")
    except Exception:
        print("Has ingresado un valor incorrecto")