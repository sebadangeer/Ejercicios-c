import random
dinero=random.randint(1,5)
cafe=2
print("el coste de tu cafe es de", cafe, "dolares, el saldo de su tarjet es de ",dinero, "dolares")
if dinero<cafe:
    print("no tenemos fondos")
else:
    print("aqui tiene su cafe que tenga buen dia")
    