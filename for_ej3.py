

# Escribe un programa que muestre la tabla de multiplicar del número que indique el usuario y los múltiplo de 2.

numero_usu = int(input("Dime un numero para decir su tabla:\n"))


for a in range(1, 11):

    total = numero_usu * a
    print(f"{numero_usu} x {a} = {total}")

    if total % 2 == 0:
        print(f"{total} es múltiplo de 2")


