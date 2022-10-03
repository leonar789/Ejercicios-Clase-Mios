#lista= [["nombre","leo"], ["nombre","leo"],["nombre","leo"]]
datos={
}

while True:
    v= input("Ingrese lo que desea agregar o salir para finalizar")
    if v == "salir":
        break
    v2= input("ingrese el contenido a agregar")
    datos [v] = v2
    for dato, dato2 in datos.items():
        print(f"Tu {dato} es {dato2}")
    