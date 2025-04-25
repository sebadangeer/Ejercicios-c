import random
import time
turno=0
v1=50
v2=50
while v2>0 and v1>0:
    if turno % 2==0:
            print("turno de pikachu")
            print("pikachu ocupa impactrueno")
            ataque=random.randint(7,10)
            critico=random.randint(1,5)
            if critico==3:
                  v1=v1-ataque*2
                  print("has realizado un critico de", ataque*2,"daño" )
            else:
                  v1=v1-ataque
                  print("has realizado ataque de", ataque,"daño" )   
            print("a vergamo le queda",v1,"hp")
    else:
        print("turno de vergamo")
        print("vergamo ocupa megavergazo")
        ataque=random.randint(7,10)
        critico=random.randint(1,5)
        if critico==3:
                v2=v2-ataque*2
                print("has realizado un critico de", ataque*2,"daño" )
        else:
                v2=v2-ataque  
                print("has realizado ataque de", ataque,"daño" )       
        print("a pikachu le queda",v2,"hp")
    turno+=1
if v1<=0:
      print("ha ganado pikachu")
else:
      print("ha ganado vergamo")
                    