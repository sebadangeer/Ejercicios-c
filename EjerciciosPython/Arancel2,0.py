arancel=200000
descuentoxcomunas={1:0.20,2:0.30,3:0.25,4:0.15}
lacomunaes={1:"la florida", 2:"la pintana", 3:"Puente Alto ", 4:"San Joaquin"}
descuentoporpersonas={1:0.02,2:0.03,3:0.04}
def descuento (comuna,grupofamiliar):
    descto=descuentoxcomunas[comuna]+descuentoporpersonas[grupofamiliar]
    desctoporcentual=descto*100
    totalapagar=arancel*(1-descto)
    print("su comuna es",lacomunaes[comuna] ,"el descuento es de ",round(desctoporcentual),"%")
    print("el total a pagar ese de ",totalapagar)
    return totalapagar
en_que_comunavive=int(input(f"""En que comuna vive
1.-La florida
2.-La pintana
3.-Puente Alto
4.-San Joaquin
Ingrese Opc : """))
con_cuantas_personas_vive=int(input(f"""Cuantas personas viven en su hogar?(Incluido el usuario) :
1.- 1 Persona
2.- 2 a 4 Personas 
3.- 5 o mas personas
Ingrese Opc : """))
arancel=descuento(en_que_comunavive,con_cuantas_personas_vive)