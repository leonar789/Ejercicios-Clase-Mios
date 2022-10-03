lista=[]

tupla=()

while True:
    frase = input("introduce tu frase")
    busqueda=input("que buscas")
    for index, letra in enumerate(frase):
        lista.append((index,letra))
        contador=frase.count(busqueda)
    print(contador)
