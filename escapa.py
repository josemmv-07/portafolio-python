import random

armadura = random.randint(1,100)
palo = False

titulo = "MAZMORRA: LA HUIDA DEL PRISIONERO"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("Despiertas en una celda oscura, con humedad en las paredes\n"
      "y cadenas oxidadas colgando del techo. De pronto,\n"
      " oyes un (clic) en la puerta...\n"
      "¡Está abierta!")

vez = input("¿ Ves un palo ? ¿Lo coge (S/N)? \n")
if vez == "S":
    palo = True

que_h = input("Qué haces?\n"
              "A - Salgo con cuidado por el pasillo\n"
              "B - Grito y pido ayuda\n")

if que_h == "A":
    print("Sales en silencio. El pasillo está oscuro, pero ves dos caminos:")
    a_donde = input("¿A dónde vas?\n"
                    "A - A la izquierda, donde hay antorchas encendidas\n"
                    "B - A la derecha, donde huele a humedad y podrido\n")
    if a_donde == "A":
        print("Llegas a una sala con una gran puerta custodiada por una armadura encantada.")
        ar = input("¿ Qué haces ?\n"
                   "A - Hablas con la armadura\n"
                   "B - Intentas correr hacia la puerta\n")
        if ar == "A":
            print(" La armadura te pregunta: dime un número del 1 al 100. " )
            usu = int(input("Di el número: \n"))
            if usu == armadura:
                print("Te mata y muere el número es: " + str(armadura))
            elif usu != armadura:
                print("Escapa eres libre el número es: " + str(armadura))
        elif ar == "B":
            print("La armadura te golpea con su espada.💀 Has muerto por impaciente.")
    elif a_donde == "B":
        print("Encuentras una vieja puerta de madera con un cartel que dice (Cuidado).\n")
        ab = input("¿Qué haces? \n"
                   "A - Abres la puerta\n"
                   "B - Das media vuelta\n")
        if ab == "A":
            print("Entras en una sala llena de ratas gigantes")
            if palo == True:
                print("Matas a todas las ratas y escapas. ¡Eres libre!")
            elif palo == False:
                print("💀 Te devoran. Has muerto.")
        elif ab == "B":
            print("Vuelves atrás y te pilla un guardia. 💀 Te mata.")
elif que_h == "B":
    print("Un guardia te escucha y entra furioso.")
    gr = input("¿Qué haces?\n"
               "A - Finges estar enfermo\n"
               "B - Le atacas por sorpresa\n")
    if gr == "A":
        print("El guardia se acerca y tú le robas las llaves.\n"
              "🔓 Escapas sigilosamente.🏆\n" 
              "¡Has escapado usando tu astucia!")
    else:
        print("El guardia reacciona rápido y te apuñala.💀 Muerto por valiente.")
        
            