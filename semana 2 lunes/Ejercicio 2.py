from asyncio.windows_events import NULL


nombre=input("Escribe tu nombre completo")
if nombre.isnumeric():
    print("Metiste un número")
else:
    print(nombre.title())
    print(nombre.lower())
    print(nombre.upper())

