# Esta línea de abajo sirve para que el usuario introduzca su edad

edad = int(input("Dígame su edad "))
tipo_de_carnet = input("Dígame su tipo de carné (E para estudiante / P pensionista / F familia numerosa / N nada): ")

if (25 <= edad <= 35 and tipo_de_carnet == "E") or edad <= 10 or (edad >= 65 and tipo_de_carnet == "p") or (tipo_de_carnet == "F"):
    print("Se te aplica descuento")
else:
    print("No se te aplica descuento")
