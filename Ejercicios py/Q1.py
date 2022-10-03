infraccion={
    1:{"name":"Choque","cost":50},
    2:{"name":"Semáforo","cost":30},
    3:{"name":"Falta de documentos","cost":100}
}
oficial={
    1:{"name":"Luis","lastname": "Bello", "ci":13452224},
    2:{"name":"Jose","lastname": "Quevedo", "ci":44235611},
    3:{"name":"Antonio","lastname": "Guerra", "ci":12345678}
}
validador=True
multas={}
contador=1


while True:
    opcion=input("Bienvenido a nuestra base de datos. Elija una de las siguientes opciones \n 1- Agregar multa \n 2- Eliminar Multa \n 3- Mostrar multas \n 4- Busqueda de multas por fiscales  \n 5- Salir   \n-->")
    if opcion.isnumeric():
        if  int(opcion) not in range(1,6):
            print("opcion no valida")
            continue
    else:
        print("opcion no valida")
        continue
    if int(opcion)==1:
        print("A continuación ingrese los datos del infractor: ")
        nombrei=input("\t Nombre: ")
        apellidoi=input("\t Apellido: ")
        ci=input("\t Ci: ")
        while True:
            infraccionc=input("\t Infracción: \n \t \t 1- Choque \n \t \t 2- Semáforo \n \t \t 3- Falta de Documentos  \n-->")
            if infraccionc.isnumeric():
                if  int(infraccionc) not in range(1,4):
                    print("opcion no valida")
                    continue
            else:
                print("opcion no valida")
                continue
            if int(infraccionc) in infraccion:
                break
        while True:
            fiscal=input("\t Oficial: \n \t \t 1- Luis \n \t \t 2- José \n \t \t 3- Antonio \n-->")
            if fiscal.isnumeric():
                if  int(fiscal) not in range(1,4):
                    print("opcion no valida")
                    continue
            else:
                print("opcion no valida")
                continue
            if int(fiscal) in oficial:
                 break
        multas[contador]={
            "Nombre":nombrei,
            "Apellido":apellidoi,
            "Cedula":ci,
            "Infraccion":infraccion[int(infraccionc)]["name"],
            "Coste":infraccion[int(infraccionc)]["cost"],
            "Fiscal":oficial[int(fiscal)]
        }
        contador+=1
    if int(opcion) == 2:
        while True:
            print("Qué Multa desea borrar\n")
            for cosa, multa in multas.items():
                print(str(cosa) + "-->")
                for elemento,adicional in multa.items():
                    if elemento=="Fiscal":
                        print("\t Fiscal: ", end="\t ")
                        for info, dato in adicional.items():
                            print(dato, end=" ")
                    else:
                        print(f"\t {elemento}: \t {adicional}")
                print("\n")
            aborrar=input("Ingrese el número de la multa a eliminar o escriba '0' para finalizar: ")
            if aborrar=="0":
                break  
            if aborrar.isnumeric():
                if  int(aborrar) not in multas:
                    print("No hay multa en sistema con ese ID")
                    continue
            else:
                print("No hay multa en sistema con ese ID")
                continue
            if int(aborrar) in multas:
                multas.pop(int(aborrar))
                print("Multa eliminada")
            
            else: 
               print("Opccion no valida")

    if int(opcion)==3:
        print("A continuacion las multas en sistema: \n")
        for cosa, multa in multas.items():
            print(str(cosa) + "->")
            for elemento,adicional in multa.items():
                if elemento=="Fiscal":
                    print("\t Fiscal: ", end="\t ")
                    for info, dato in adicional.items():
                        print(dato, end=" ")
                    print("\n")
                else:
                    print(f"\t {elemento}: \t {adicional}")
    
    if int(opcion)== 4:
        while True:
           
            fiscal_escogido= input("Seleccione el fiscal que desea buscar: \n 1- Luis \n 2- Jose \n 3- Antonio \n 4- salir ")
            if int(fiscal_escogido)== 4:
                break
            if int(fiscal_escogido) in oficial:
                for cosa, multa in multas.items():
                    if multa["Fiscal"]["name"] == oficial[int(fiscal_escogido)]["name"]:
                        validador=False
                        print(str(cosa) + "->")
                        for elemento,adicional in multa.items():
                            if elemento=="Fiscal":
                                print("\t Fiscal: ", end="\t ")
                                for info, dato in adicional.items():
                                    print(dato, end=" ")
                                print("\n")            
                            else:
                                print(f"\t {elemento}: \t {adicional}")

                if validador:
                    print("El fiscal no ha hecho multas")
                else:
                    validador=True

    if int(opcion)== 5:
        print("Tenga un buen dia")
        break
        

