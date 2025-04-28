capmax=50
total=0
print("desea ingresar cajas al camion ")
print("1-si")
print("2-no")
resp1=int(input())
if resp1==1:
   cajas=int(input("cuantas cajas desea ingresar:"))
   total=total+cajas
   while total<50:
     print("usted lleva ",total, "desea ingresar mas cajas al camion ")
     print("1-si")
     print("2-no")
     resp=int(input())
     if resp==1:
        print("usted lleva ", total,"cajas")
        cajas=int(input("cuantas cajas desea ingresar:"))
        total=total+cajas
     else:
        break
while total>50:
    print("Has excedido el limite de cajas en ",total-capmax)
    mncaj=int(input("Cuantas cajas desea quitar:"))
    total=total-mncaj
if total<=50 and total>1:
   print("llevas", total ,"cajas que tenga un buen viaje")
if resp1==2:
   print("usted no lleva cajas")
