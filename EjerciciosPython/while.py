clave1=1234
inte=1
claveing=int(input("Ingrese clave:"))
#Mientras no se cumpla una condicion
# el programa no avanza a la siguiente linea de codigo
while inte<3:
   if claveing!=clave1:
    print("incorrecto lleva",inte)
    claveing=int(input("Ingrese clave:"))
    inte=inte+1
   else:
    break
if inte>=3:
  print("inCorrecto")
if clave1==claveing:
  print("correcto")