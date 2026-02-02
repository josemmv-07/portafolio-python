respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("¿Qué opción prefieres [A, B, C]? ")
    print("Di A, B o C")

if respuesta == "A":
    print("Has elegido bien")
elif respuesta == "B":
    print("Más o menos bien")
elif respuesta == "C":
    print("Has elegido mal")
    exit()

numero = 12

while numero > 1:
    numero += 1
    print(f"Mi número es {numero}")
    if numero == 1000:
        break
