x="Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y="CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z="According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."
contx=0
conty=0
contz=0
print("x:")
print("\t Indices")
for indice, letra in enumerate(x):
    if letra == "a" or letra == "A":
        if x[indice+1] == "t":
            contx+=1
            print(f"\t\t- {indice}-{indice+1}")
print(f"\t at aparece {contx} veces\n")
print("y:")
print("\t Indices")
for indice, letra in enumerate(y):
    if letra == "o" or letra == "O":
        if y[indice+1] == "m":
            conty+=1
            print(f"\t\t- {indice}-{indice+1}")
print(f"\t om aparece {conty} veces\n")
print("z:")
print("\t Indices")
for indice, letra in enumerate(z):
    if letra == "i" or letra == "I":
        if z[indice+1] == "n":
            print(f"\t\t- {indice}-{indice+1}")
            contz+=1
print(f"\t in aparece {contz} veces\n")
