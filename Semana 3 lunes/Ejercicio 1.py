num=int(input("Coge un número"))
for x in range(num+1):
    if x%2!=0:
        if x+2>num:
            print(x)
        else:
            print (x,end=",")