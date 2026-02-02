titulo = "Bienvenido al test del queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Qué haces cuando ves una tabla de queso?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo uno de los quesos\n"
               "C - No puedo evitar devorarla ")

if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion = puntuacion + 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones correctas son A, B o C")
    exit() 

opcion = input("Pregunta 2: ¿Te gusta el queso?\n"
               "A - No\n"
               "B - A veces\n"
               "C - Sí ")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Solo A, B o C")
    exit()

if puntuacion == 0:
    print("No te gusta el queso. Tu puntuación es 0.")
elif puntuacion <= 10:
    print("Más o menos eres fan. Tu puntuación es: " + str(puntuacion))
elif puntuacion >= 20:
    print("¡Felicidades! Eres fan del queso. Tu puntuación es: " + str(puntuacion))
else:
    print("Tu puntuación es: " + str(puntuacion))
