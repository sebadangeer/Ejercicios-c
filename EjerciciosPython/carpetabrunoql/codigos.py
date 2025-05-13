
import random
contador=0
print("ingrese 2 numeros")
variable1=int(input())
variable2=int(input())
if  variable2<variable1:
    variable2=int(input())
variablerandom=random.randint(variable1,variable2)

print("*"*variablerandom)
