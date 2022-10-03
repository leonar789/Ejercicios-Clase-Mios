while True:
    n=0
    validador=False
    validadorprimo=False
    fermat=0
    while True:
        numero=input("Introduce un número")
        if not numero.isdigit():
            print("opcion no valida")
            continue
        break
    while fermat <= int(numero):
        fermat=(2**(2**n)) +1
        if fermat== int(numero):
            for i in range(1,int(numero)):
                if int(numero)%i==0 and i!=1:
                    break
                if i==int(numero)-1:
                    validador=True
            break
        n+=1
    if validador:
        print("Es un primo de Fermat \n")
    else:
        print("No es un primo de Fermat \n")
