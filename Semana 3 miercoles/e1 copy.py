dic_esp= {
}
dic_ing={

}
list= input("Introduce las palabras en ingles y español separadas por dos puntos, ejem: Casa:House")
lista_pares=list.split(",")
for par in lista_pares:
    par2=par.split(":")
    v1=par2[0]
    v2=par2[1]
    dic_esp[v1]= v2
    dic_ing[v2]= v1

texto= input("mete el texto en español")

traduccion=texto.split(" ")
tra_realizada=""
for palabra in traduccion:
    tra_realizada+=str(dic_esp.get(palabra,palabra)) + " "
    
print(tra_realizada)

