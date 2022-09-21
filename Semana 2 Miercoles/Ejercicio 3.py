numero = int(input("pls enter a numer"))
aux = numero -1
acumulador=0

while aux >= 1:
        if numero % aux==0:
            acumulador += aux
        aux -=1

if acumulador > numero:
        print("es abundante")
else:
        print("no es abundante")
