numero = input("Elige un número")

if numero.isnumeric():
    numero=float(numero)
    if numero%2 == 0 and numero !=0:
        print(f"{numero} es par")
    elif numero == 0:
        print("Aun se discute si el 0 es par o no, aunque muchos lo consideran par")
    else:
        print(f"{numero} es impar")
else:
    print("Pls mete un número")