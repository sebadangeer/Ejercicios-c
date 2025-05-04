import random
dinero=[]
dineroaentregar=0
usuario1="215852385"
clave1=1234
clave2=7777
clave3=6666
dinerototal=0
usuario2="140220965"
usuario3="106460655"
cantidad_de_billetes_de_5=30
cantidad_de_billetes_de_10=30
cantidad_de_billetes_de_20=30
saldo_de_5=cantidad_de_billetes_de_5*5000
saldo_de_10=cantidad_de_billetes_de_10*10000
saldo_de_20=cantidad_de_billetes_de_20*20000
saldototaldelcajero=saldo_de_5+saldo_de_10+saldo_de_20
cash_need=str(input("Cuanto dinero desea sacar : "))
for i in str(cash_need):
    dinero+=i
if dinero[-1] in "123456789":
    print()
elif dinero[-2] in "123456789":
    print()
elif dinero[-3] in "123456789":
    print()
elif dinero[-4] in "12346789":
    print()
else:
    cash_need=int(cash_need)
    if cash_need<saldototaldelcajero:
        while cash_need!=dineroaentregar:
                billde20=random.randint(0,cantidad_de_billetes_de_20)
                billetesde20=billde20*20000
                billde10=random.randint(0,cantidad_de_billetes_de_10)
                billetesde10=billde10*10000
                billde5=random.randint(0,cantidad_de_billetes_de_5)
                billetesde5=billde5*5000
                dineroaentregar=billetesde5+billetesde10+billetesde20
if cash_need==dineroaentregar:
    print("Se le han dado", billde5,"billetes de 5, ",billde10,"billetes de 10","y ", billde20, "billetes de 20")
    print("que tenga buen dia")
else:
    print("el monto solicitado no esta disponible")
    print("usted no pudo sacar dinero")