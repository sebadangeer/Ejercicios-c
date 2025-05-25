
#Importas archivos dando la direccion de la carpeta y el nombre del archivo y con open lo importamos
#archivoabierto=open("Uso_De_TXT\\Archivo.txt")
archivo_sin_leer=open("Uso_De_TXT\\Archivo.txt",encoding="UTF-8")
#El archivo debe ser almacenado en una variable para poder ser usado y con la funcion read lo lee
linea1 = archivo_sin_leer.readlines()
#con la variable donde abrimos el archivo y la funcion readlines podemos ver el contenido del archivo y utilizarlo
archivo_sin_leer.close()
#Siempre que ocupemos un archivo debemos cerrarlo con esta funcion

print(linea1)

