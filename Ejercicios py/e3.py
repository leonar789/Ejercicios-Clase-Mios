limite=int(input("numero"))
contador1 = 0
contador2 = 1
fibo=1
fiboim= ["0"]
if limite==0:
    print(contador1)

if limite!=0:
    while contador2 <= limite:
        fiboim.append(str(fibo))
        fibo= contador1 + contador2
        contador1=contador2
        contador2=fibo
print(",".join(fiboim))
