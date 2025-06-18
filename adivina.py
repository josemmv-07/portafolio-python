import random

print("Adivina qué número estoy pensando del 1 al 10")

a = int(input("¿Dime el número? "))
b = random.randint(1, 10)

if a == b:
    print("Bien, has acertado. Era el: " + str(b))
   
if a != b:
    print("¡Error! Era el " + str(b))
