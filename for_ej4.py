"""Crea un programa donde el usuario nos dé una lista de números y el programa tiene que encontrar el
 número más pequeño y el más grande de la lista del usuario."""

numero_de_usuario = []

numero_int = int(input("Introduzca un número en la lista:\n"))
numero_de_usuario.append(numero_int)

while input("¿Desea introducir más numero? [S/N]") == "S":
    numero_int = int(input("Introduzca un número en la lista:\n"))
    numero_de_usuario.append(numero_int)

print(numero_de_usuario)

numeros_introducidos = input("introduzca los número separados por coma:\n") # 1,2,3....
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

numero_pe = numeros_de_usuario[0]
numero_gra = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pe > numero:
        numero_pe = numero

    if numero_gra < numero:
        numero_gra = numero

print(f"Numero grande: {numero_gra}, Numero pequeño: {numero_pe}")