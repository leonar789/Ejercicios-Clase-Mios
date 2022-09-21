dividendo= (input("Elige el dividendo"))
divisor = (input("elige el divisor"))

if dividendo.isnumeric() or divisor.isnumeric():
    divisor=float(divisor)
    dividendo=float(dividendo)
    if divisor == 0:
        print ("La división entre '0' no se encuentra definida")
    else:
        print(round(dividendo/divisor,10))

else:
    print("Debes escribir números, no palabras")
