eleccion = input("Introduce la pizza que desees: \n1-Vegetariana \n2-No Vegetariana \n ->")
if float(eleccion) == 1:
    ingrediente = int(input("Introduce los ingredientes que desees: \n1-Tofu \n2-Pimiento \n ->"))
    if ingrediente == 1:
        ingrediente = "Tofu"
    else: 
        ingrediente= "Pimiento"
    print(f"Tu pizza es venegariana, tiene Mozarella, Tomate y {ingrediente}")
elif float(eleccion) == 2:

        ingrediente = int(input("Introduce los ingredientes que desees: \n1-Jamón \n2-Salmón \n3-Peperonni \n ->"))
        if ingrediente == 1:
            ingrediente = "Jamón"
        elif ingrediente ==2:
            ingrediente= "Salmón"
        else: 
            ingrediente= "Pimiento"
        print(f"Tu pizza es no venegariana, tiene Mozarella, Tomate y {ingrediente}")
else: 
    print("Elige algo del menú")