print("Pd:Si no te sabes estos codigos eres un pendejo")
print("Bienvenido a la lista de comandos basicos de Sebita")
print("")
print("1.- Variables y Tipos de Datos")
print("2.- Operadores Aritmeticos")
print("3.- Encontrar numero min, max o redondear en variable")
print("4.- Bucles for,while , if, else")
print("5.- Listas y tuplas")
print("6.- Comandos acerca del texto (ejemplo: convertir a mayusculas)")
print("7.- Entrada y salida de texto")
print("8.- Importe de librerias")
Comando=int(input("Que tipo de comandos necesitas: "))
print("")

if Comando==1:
    print("""#1. variable = 5 : Asignar un valor numerico a una variable
#2. variable = "Hola" : Asignar texto a 2
#una variable
#3. variable = True o False : Asignar un valor booleano a una variable
#4. variable = [1, 2, 3] : Crear una lista
#5. variable = (1, 2, 3) : Crear una tupla""")

if Comando==2:
    print("""#1. variable 2 + variable : Suma
#2. variable - variable 2 : Resta
#3. variable * variable 2 : Multiplicación
#4. variable / variable 2 : División
#5. variable % variable 2 : Módulo (resto de la división)MOD PSEINT
#6. variable == variable 2 : igual a
#7. variable != variable 2 : Distinto a
#8. variable > variable 2 : Mayor que
#9. variable < variable 2 : Menor que""")

if Comando==3:
    print("""#1. variable=max(X,Y,Z) : Se queda solo con el numero mayor
#2. variable=min(X,Y,Z) : Se queda solo con el numero menor
#3. round(variable) : Se redondea los valores float
#4. variable = abs(-5)
#5. variable = 5 :   abs sirve para volver numros negativos a enteros """)

if Comando==4:
    print("""#1. if variable > 5: : Condicional if
#2. else: : Condicional else
#3. elif variable == 5: : Condicional elif
#4. for variable in range(5): : Bucle for
#5. while variable < 5: : Bucle while""")


if Comando==5:
    print("""#1. variable.append(y) : Agregar un elemento a una lista
#2. variable.insert(0, y) : Insertar un elemento en una posición específica de una lista
#3. variable.remove(y) : Eliminar un elemento de una lista
#. variable.index(y) : Obtener el índice de un elemento en una lista
#5. len(variable) : Obtener la longitud de una lista o tupla""")

if Comando==6:
    print("""#1. variable.upper() : Convertir a mayúsculas
#2. variable.lower() : Convertir a minúsculas
#3. variable.strip() : Eliminar espacios en blanco al principio y al final
#4. variable.split() : Dividir una cadena en una lista de palabras""")

if Comando==7:
    print("""#1. input() : Leer entrada del usuario
#2. print() : Imprimir texto de salida en la consola
#3. variable=int(input()) : Define la entrada del usuario como variable entero
#4. variable=float(input()) : Define la entrada del usuario como variable decimal""")


if Comando==8:
    print("""#1. import Namelibreria : se importa la libreria que necesites
#2. import random : Se libera el azar para variables aleatorias
          Ejemplo de como usar la libreria random
variable= random.randint(1,5) : se elije un numero al azar dentro del parentesis""")
#3. len(x) : Obtener la longitud de una secuencia
#4. type(x) : Obtener el tipo de dato de una variable""")
