while True:
    numero=int(input("numero"))
    validador= False
    for i in range(1,int(numero)):
        if i * (i+1)==int(numero):
            validador=True
            break
    if validador:
        print("oblongo")
    else:
        print("no oblongo")