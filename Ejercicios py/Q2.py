from unicodedata import numeric


info = {

    "shirt_sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],

    "colors": {

        "plain": "white,black,blue,gray",

        "tie-dye": "rainbow,acid wash"

    },

    "print_sizes": [[(10, 10), 12.30], [(20, 15), 14.60]]

}

keys= list(info.keys())
values= list(info.values())

ventas={

}
contador=1
while True:
    opcion=input("Bienvenido a nuestra base de datos. Elija una de las siguientes opciones \n 1- Comprar \n 2- Ver compras \n 3- Salir   \n-->")
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
            print("Selecciona una talla:")
            for i in range(0,len(info["shirt_sizes"])):
                print(f'\t {i+1}- {info["shirt_sizes"][i]}')
            id_talla=input("-->")
            if id_talla.isnumeric():
                if int(id_talla) in range(1,len(values[0])+1):
                    talla= values[0][int( id_talla)-1]
                    print(talla)
                    break
                else:
                    print("Dato invalido")
            else:
                print("Dato invalido")


        while True:
            print("Selecciona un tipo de color:")
            for i in range(0,len(list(values[1].keys()))):
                print(f'\t {i+1}- {list(values[1].keys())[i]}')
            id_colortip=input("-->")
            if id_colortip.isnumeric():
                if int(id_colortip) in range(1,len(values[1])+1):
                    tipo_color= list(values[1].keys())[int(id_colortip)-1]
                    print(tipo_color)
                    break
                else:
                    print("Dato invalido")
            else:
                print("Dato invalido")

        while True:
            print("Selecciona un color:")
            for i in range(0,len(list(values[1].values())[int(id_colortip)-1].split(","))):
                print(f'\t {i+1}- {list(values[1].values())[int(id_colortip)-1].split(",")[i]}')
            id_color=input("-->")
            if id_color.isnumeric():
                if int(id_color) in range(1,len(list(values[1].values())[int(id_colortip)-1].split(","))+1):
                    color= list(values[1].values())[int(id_colortip)-1].split(",")[int(id_color)-1]
                    print(color)
                    break
                else:
                    print("Dato invalido")
            else:
                print("Dato invalido")

        while True:
            print("Selecciona un tamaño de impresion:")
            for i in range(0,len(values[2])):
                print(f'\t {i+1}- {values[2][i][0][0]} por {values[2][i][0][1]}')
            id_tamaño=input("-->")
            if id_tamaño.isnumeric():
                if int(id_tamaño) in range(1,len(values[2])+1):
                    tamaño= f"{values[2][int(id_tamaño)-1][0][0]} por {values[2][int(id_tamaño)-1][0][1]}"
                    print(tamaño)
                    break
                else:
                    print("Dato invalido")
            else:
                print("Dato invalido")
        
        ventas[contador]={
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "talla":talla,
            "color type":tipo_color,
            "color":color,
            "tamaño":tamaño,
            "coste": values[2][int(id_tamaño)-1][1]
        }
        contador+=1    
    if int(opcion) == 2:
        print("A continuacion las ventas realizadas: \n")
        for id, dato in ventas.items():
            print(str(id) + "->")
            for elemento,adicional in dato.items():
                    print(f"\t {elemento}: \t {adicional}")

    if int(opcion)==3:
        print("Tu te lo pierdes")
        break



        
