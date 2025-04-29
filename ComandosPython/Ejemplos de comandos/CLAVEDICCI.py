claveing=""
count=0
contador=0
nameuser=""
lista_de_usuarios={
    "seba" : "sebaxo12",
    "juan" : "juan11",
}
while count<=2 or claveing==lista_de_usuarios:
    count+=1
    nameuser= (input("Nombre de usuario: "))
    for key in lista_de_usuarios:
        if key[count] in lista_de_usuarios != nameuser:
            count+=1
        else:
            if key==nameuser:
                count=0
                contador=0
                while contador<=2 or claveing==key:
                    claveing=input((f"""Bienvenido {nameuser}                
Ingrese su clave: """))
                    if claveing!=key:
                        contador+=1
                        count+=1
                        if claveing == lista_de_usuarios[nameuser]:
                            print("Que tenga buen dia usuario: ", nameuser)
                            break
if count>=3:
    print("has excedido el numero de intentos diarios")
if claveing==lista_de_usuarios[nameuser]:
    print("Accediste a tus archivos secretos")