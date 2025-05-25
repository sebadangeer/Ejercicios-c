#with open es para importar archivos, necesitamos leerlos y almacenarlos en una variable, como con def debemos llamar a la funcion 
#en el with debemos solicitar escritura con "w",y con "a" podemos añadir y no sobreescribir el archivo encoding utf-8 es para leer comas mayusculas etc
with open('Uso_De_datos\\Archivo.csv',"a",encoding="UTF-8") as archivo:
    #con archivo.write escribimos en el archivo lo que le demos
    i=0
    for i in range(20):
        archivo.write(f"{i+1} \n")
    #Esto sobreescribe el archivo
    #archivo.writelines(["con este comando podemos escribir\n","algo en el documento directamente"])
    
    #read es para leer el archivo
    # #ocupamos el \ para separar por lineas archivo.writelines(["con este comando podemos escribir\n","algo en el documento directamente"])

