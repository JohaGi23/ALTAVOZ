bandas=[]


#contstruyendo la interfaz 
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100

while(opcion!=5):
    print("1. Registrar Banda")
    print("2. Buscar informacion de una banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    
    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #creando los datos del diccionario
        banda["id"]=int(input("Digita el Id: "))
        banda["nombre"]=input("Nombre de la Banda: ")
        banda["genero"]=input("Genero: ")
        banda["Clasificacion"]=input("Clasificacion: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Digita el costo de la banda: $"))

        
        #agregando un diccionario a una lista
        bandas.append(banda)#palabra reservada para agregar

        pass
    elif opcion==2:
        bandaBuscada=input("Digita el nombre de la banda que estas buscando")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                #como lo encontre muestro los datos de bandaAuxiliar
                 print(f"id: {bandaAuxiliar["id"]}---nombre: {bandaAuxiliar["nombre"]}")
            else:
                print("parce siga buscando...")

        
    elif opcion==3:
        print(bandas)
        
    elif opcion==4:
        
        pass
    elif opcion==5:
        pass
    else:
        pass