

while True:
    validador=True
    num= int(input("numero"))
    for num1 in range(2,num+1):
        for compro1 in range(2,num1+2):
            if num1%compro1==0:
                if num1!=2:
                    break
            if compro1==num1-1 or compro1==num1:
                for num2 in range(2,num1+1):
                    if num2*num1==num:
                        for compro2 in range(2,num2+2):
                            if num2%compro2==0:
                                if num2!=2:
                                    break
                            if compro2==num2-1 or compro2==num2:
                                print(num1,num2)
                                validador=False
                        
    if validador:
        print("no hay dos numeros primos cuyo producto sea igual a " + str(num))
