pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300         
        },

        {
            "id": 2,
            "name": "Emphysema",
            "price": 500

        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],

    "Nervous system": [

        {
            "id": 4,
            "name": "Parkinson",
            "price": 800         
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],

    "Endocrine system": [

        {
            "id": 6,
            "name": "Diabetes",
            "price": 350         
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700

        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }

    ],  

}

sistemas=list(pathologies.keys())
enfermedades=list(pathologies.values())
enfermedades_separadas=[]
for enfermedad in enfermedades:
    for i in enfermedad:
        enfermedades_separadas.append(i)


contador2=1
lista={

}
while True:
    validador=True
    contador=1
    opcion=input("Bienvenido a nuestra base de datos. Elija una de las siguientes opciones \n 1- Introducir enfermo \n 2- buscar enfermedad \n 3- Salir   \n-->")
    if not opcion.isnumeric():
        print("opcion no valida")
        continue
    if int(opcion) not in range(1,4):
        print("opcion no valida")
        continue
    if int(opcion)==1:
        print("Ingresa los siguientes datos: \n")
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        cedula=input("C.I: ")
        while True:
            print("Indique el Id de la enfermedad:")
            for i in range(0,len(sistemas)):
                print(f'\t - {sistemas[i]}')
                for x in pathologies[sistemas[i]]:
                    for dato, info in x.items():
                        if dato=="name":
                            print(f"\t \t {contador}- {info}")
                            contador+=1
            id_enfermedad=input("-->")
            if id_enfermedad.isnumeric():
                if int(id_enfermedad) in range(1,contador+1):
                    id_enfermedad= int(id_enfermedad)-1
                    for sistema, datos in pathologies.items():
                        for enfermedades in datos:
                            if enfermedades["id"]== id_enfermedad +1:
                                sistemadic=sistema
                    print(id_enfermedad)
                    print(sistemadic)
                    break
                else:
                    print("Dato invalido")
            else:
                    print("Dato invalido")

        lista[contador2]={
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "Id Enf":id_enfermedad + 1,
            "Sistema":sistemadic,
            "Enfermedad":enfermedades_separadas[id_enfermedad]["name"],
            "coste":enfermedades_separadas[id_enfermedad]["price"],
        }
        
    if int(opcion) == 2:
        print("Indique el Id de la enfermedad:")
        for i in range(0,len(sistemas)):
            print(f'\t - {sistemas[i]}')
            for x in pathologies[sistemas[i]]:
                for dato, info in x.items():
                    if dato=="name":
                        print(f"\t \t {contador}- {info}")
                        contador+=1
        id_enfermedad=input("-->")
        if id_enfermedad.isnumeric():
            if int(id_enfermedad) in range(contador+1):
                id_enfermedad= int(id_enfermedad)
                print(id_enfermedad)
            else:
                print("Dato invalido")
        else:
            print("Dato invalido")

        for id, dato in lista.items():
            for elemento,adicional in dato.items():
                if id_enfermedad== adicional:
                    print(f"Paciente {id}: \n")
                    validador=False
                    for elemento, adicional in dato.items():
                        print(f"\t {elemento}: \t {adicional}")
        if validador:
            print("No hay pacientes con esa enfermedad")
        contador2+=1
    if int(opcion)==3:
        break
                