numero = int(input("pls enter a numer"))
aux = numero -1
contador=0
if numero <=1:
    print("no es primo")
while aux > 1:
        if numero % aux==0:
            contador +=1
        aux -=1

if contador == 0:
        print("es primo")
else:
        print("no es primo")
