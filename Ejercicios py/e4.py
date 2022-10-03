from random import randrange
quierenjugar=True
puntajes=[0,0]

for i in range(7):
    if quierenjugar:
        for player in range(len(puntajes)):
            if input(f"Jugador {player+1}, es tu turno. Deseas probar suerte? \n -s \ -n") == "s":
                rdados=randrange(1,7)
                while True:
                    if rdados ==3:
                        print("Otro itento\n")
                        rdados=randrange(1,6)
                    if rdados == 1:
                        print("Ganaste 10 puntos\n")
                        puntajes[player]+=10
                        break
                    if rdados== 2:
                        print("Ganaste 20 puntos\n")
                        puntajes[player]+=20
                        break
                    if rdados==4:
                        print("¡Vamos! Duplicaste tus puntos\n")
                        puntajes[player]*=2
                        break
                    if rdados==5:
                        print("Ganaste 40 puntos\n")
                        puntajes[player]+=40
                        break
                    if rdados==6:
                        print("Perdiste la mitad de tus puntos\n")
                        puntajes[player]/=2
                        break
            else:
                quierenjugar=False
    else:
        break
    print("- jugador 1: " + str((int(puntajes[0]))) + "\n" + "- jugador 2: " + str((int(puntajes[1]))) + "\n")
if puntajes[0]>puntajes[1]:
    print("ha ganado el jugador 1")
else:
    print("ha ganado el jugador 2")
                



