# Escribe un programa en Python que me diga cuántos espacios, puntos y comas hay en un texto

texto_usuario = "Hola, me llamo Jose. ¿Tu como te llamas?"

puntos = "."
puntos_e = 0

comas = ","
comas_e = 0

espacios = " "
espacios_e = 0


for letra in texto_usuario:
    if letra in puntos:
        print(f"He encontrado un punto: {letra}")
        puntos_e += 1
    elif letra in comas:
        print(f"He encontrado una coma: {comas}")
        comas_e += 1
    elif letra in espacios:
        print(f"He encontrado un espacio: {espacios}")
        espacios_e += 1

print(f"Total de puntos = {puntos_e}\n"
      f"Total de comas = {comas_e}\n"
      f"Total de espacios = {espacios_e}")