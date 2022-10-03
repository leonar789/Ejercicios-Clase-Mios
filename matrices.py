m1=[[1,2,3],[4,5,6]]
m2=[[-1,0],[0,1],[1,1]]
resultado=[]
contador=0
for i in range(len(m1)):
    contador=0
    for j in range(len(m1[i])):
        contador+=m1[i][j] * m2[j][i]
        print(contador)
    resultado.append(contador)


print(resultado)