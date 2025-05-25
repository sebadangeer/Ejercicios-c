#Para graficar necesitamos pandas para crear el dataframe, matplot que es la encargada de graficar
#seaborn ordena lo valores para graficar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
def t():
    time.sleep(1)
while True:
    try:
        print("""Bienvenido a GRAFICADORA DE SEBASTIAN

Si desea salir del terminal Escriba SALIR en valor x
              """)
        nombredelgrafico=str(input("Ingrese el nombre de su Grafico : "))
        valorx=str(input("Ingrese el valor de x en su grafico : "))
        t()
        if valorx=="salir":
            break
        valory=str(input("Ingrese el valor de y en su grafico : "))
        t()
        dato = {valorx:[],valory:[]}
        t()
        cant=int(input(f"Ingrese la cantidad de {valorx} : "))
        t()
        for i in range(cant):
            t()
            variable1=str(input(f"Ingrese su {valorx} : "))
            t()
            variable2=float(input(f"Ingrese su {valory} : "))
            dato[valorx].append(variable1)
            dato[valory].append(variable2)
#Damos los parametros como en cualquier grafico y veemos que tipo de interfaz necesitamos,
#Las dominadas son line para graficos de  puntos y bar para graficos de barra
        df = pd.DataFrame(dato)
        t()
        print(df)
        opc=int(input("""En base a su informacion elija el grafico que mas le acomode 
                      1.-Grafico de barras
                      2.-Grafico de Puntos
                      
Ingrese su opcion : """))
        match opc:
            case 1:
                sns.barplot(x=valorx,y=valory,data=df)
                plt.title(nombredelgrafico)
                plt.show()
            case 2:
                sns.lineplot(x=valorx,y=valory,data=df)
                plt.title(nombredelgrafico)
                plt.show()
    except Exception:
        t()
        print("Porfavor, ingrese los valores que se le solicitan")
#Apuntes=Para graficar necesitamos columnas, para crear varias columnas estas se crean como diccionarios y su valor son listas
#para añadir elementos a nuestrascolumnas damos el valor de la llave o columna y con append añadimos elementos a nuestra columna
#es importante crear un data frame par que este pueda ser graficado_