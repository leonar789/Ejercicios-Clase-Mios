num=int(input("numero"))
print(f"-convinaciones para {num}: ")
for i in range(num):
    for i2 in range(num):
        if i+i2 == num and i<=i2:
            print(f"    *{i}-{i2}")