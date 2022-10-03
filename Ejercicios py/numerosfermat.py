while True:
    n=2
    validador=False
    
    triangular=1
    while True:
        numero=input("Introduce un número")
        if not numero.isdigit():
            print("opcion no valida")
            continue
        break
    while triangular <= int(numero):
       
        if triangular== int(numero):
            if int(numero)%2==0:
                validador=True
                break
            break
        triangular= triangular + n
        n+=1
    if validador:
        print("Es un triangular \n")
    else:
        print("No es un triangular \n")
