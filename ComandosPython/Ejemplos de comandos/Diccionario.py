#el diccionario se abre con llaves las llaves se separan con comas
#se determina el valor con ":"
dicci={
    "seba" : "11",
    "pablo": "18",
    "juan" : "15"
}
print("de quien quieres saber edad")
print("seba")
print("pablo")
print("juan")
Persona=input()
Persona=Persona.lower()
duda=(dicci[Persona])
print(duda)
#Crear un diccionario con la funcion dict
diccionario=dict(nombre="seba",apellido="balladares",edad="15")
print("Que desea saber")
print("nombre")
print("apellido")
print("edad")
Quedesea=input()
Quedesea=Quedesea.lower()
print(diccionario[Quedesea])
