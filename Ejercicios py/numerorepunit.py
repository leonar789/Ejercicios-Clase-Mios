while True:
    n=0
    validador1=False
    validador2=False
    cuadrado=0
    acumulador=0
    while True:
        numero=input("Introduce un número")
        if not numero.isdigit():
            print("opcion no valida")
            continue
        break
    for i in range(1,len(numero)):
        if numero[i-1]== numero[i]:
            continue
        else:
            validador1= True
    for i in numero:
        acumulador+=int(i)
    if int(acumulador**(1/2))== acumulador**(1/2):
        validador2=True
    if not validador1:
        print("Es un numero puto \n")
    else:
        print("No es un primo de Fermat \n")
    if validador2:
        print("La suma de sus digitos es un cuadrado \n")
    else:
        print("La suma de sus digitos no es un cuadrado \n")


