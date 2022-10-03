products = {

    "mobiles": {

        "Apple": [

            {

                "id": 1,

                "name": "iPhone 7",

                "price": 300

            },

            {

                "id": 2,

                "name": "iPhone 8",

                "price": 350

            },

            {

                "id": 3,

                "name": "iPhone Xr",

                "price": 450

            },

            {

                "id": 4,

                "name": "iPhone Xs",

                "price": 460

            },

            {

                "id": 5,

                "name": "iPhone 11",

                "price": 900

            },

            {

                "id": 6,

                "name": "iPhone 12",

                "price": 1100

            },

            {

                "id": 7,

                "name": "iPhone 13",

                "price": 1300

            },

        ],

        "Samsung": [

            {

                "id": 8,

                "name": "Samsung Galaxy Beam",

                "price": 150

            },

            {

                "id": 9,

                "name": "Samsung Galaxy S6",

                "price": 200

            },

            {

                "id": 10,

                "name": "Samsung Galaxy S7",

                "price": 300

            },

        ],

        "Xiaomi": [

            {

                "id": 11,

                "name": "Xiaomi Redmi Note 8",

                "price": 250

            },

            {

                "id": 12,

                "name": "Xiaomi Redmi Note 8 Pro",

                "price": 300

            },

        ]

    },

    "laptops": {

        "DELL": [

            {

                "id": 13,

                "name": "Dell Inspiron 15",

                "price": 600

            },

            {

                "id": 14,

                "name": "Dell Latitude 14",

                "price": 650

            },

        ],

        "MAC": [

            {

                "id": 15,

                "name": "MacBook Pro 13",

                "price": 900

            },

            {

                "id": 16,

                "name": "MacBook M1",

                "price": 1500

            },

        ]

    },

}

dispositivos=list(products.keys())
marcas_list=[]
lista_id=[]
marcas_pc=[]
ventas={}
for dispositivos, marcas in products.items():
    for marca, equipos in marcas.items():
        marcas_list.append(marca)
        for equipo in equipos:
            lista_id.append(equipo)

contador=1
contador2=1
print(marcas_list)
print(lista_id)
while True:
    opcion=input("Bienvenido a nuestra base de datos. Elija una de las siguientes opciones \n 1- Comprar \n 2- Eliminar Multa \n 3- Mostrar multas \n 4- Busqueda de multas por fiscales  \n 5- Salir   \n-->")
    if opcion.isnumeric():
        if  int(opcion) not in range(1,4):
            print("opcion no valida")
            continue
    else:
        print("opcion no valida")
        continue
    if int(opcion)==1:
        print("A continuación ingrese los datos solicitados: ")
        nombrei=input("\t Nombre: ")
        apellidoi=input("\t Apellido: ")
        ci=input("\t Ci: ")
        while True:
            contador=1
            print("¿Elija el id del dispositivo que desea?: \n")
            for dispositivo, marcas in products.items():
                print(f"\n-{dispositivo}")
                for marca, equipos in marcas.items():
                    print(f"\t -{marca}")
                    for equipo in equipos:
                        for identidad, dato in equipo.items():
                            if identidad == "name":
                                print(f"\t \t {contador}- {dato}")
                                contador+=1
                print("\n")
            while True:
                id_compra=input("--> ")
            
                if not id_compra.isdigit():
                    print("opcion no valida")
                    continue
                if int(id_compra) not in range(1, contador):
                    print("opcion no valida")
                    continue
                break
            for dispositivo, marcas in products.items():
                for marca, equipos in marcas.items():
                    for equipo in equipos:
                        for identidad, dato in equipo.items():
                            if dato==int(id_compra):
                                 marca_compra=marca
                                 dispositivo_compra=dispositivo

            ventas[contador2]={
                "nombre": nombrei,
                "apellido": apellidoi,
                "cedula": ci,
                "Dispositivo": dispositivo_compra,
                "Marca": marca_compra,
                "Id producto": int(id_compra),
                "producto":lista_id[int(id_compra)-1]["name"],
                "coste":lista_id[int(id_compra)-1]["price"],
                }

            print("A continuación su factura \n")
            for identidad, dato in ventas[contador2].items():
                    print(f"\t {identidad}: \t {dato}")
            contador2+=1
            break



        