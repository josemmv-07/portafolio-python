import string

# Dime un programa que me identifique la letra mayúscula.

texto_del_usuario = input("Introduzca un texto:\n")
letras_may = 0

for letra in texto_del_usuario:
    if letra in string.ascii_uppercase:
        letras_may += 1

print(f"En total de letra Mayúsculas = {letras_may} ")