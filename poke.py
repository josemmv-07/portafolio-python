from random import randint
import os
import time

vida_inicial_pika = 80
vida_inicial_squi = 90

tamanio_barra_vi = 20

vida_pika = vida_inicial_pika
vida_squi = vida_inicial_squi

while vida_pika > 0 and vida_squi > 0:
    
    # se devuelve los turnos de combate

    #Turno de Pikachu
    print("\nTurno de Pikachu\n")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikacho ataca con Bola voltio\n")
        vida_squi -= 10
    else:
        #Onda Trueno
        print("Pikachu ataca con Onda Trueno\n")
        vida_squi -= 11

    vida_pika = max(0,vida_pika)
    vida_squi = max(0, vida_squi)

    barras_de_vida_pika = int(vida_pika * tamanio_barra_vi / vida_inicial_pika)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pika, " " * (10 - barras_de_vida_pika),
                                              vida_pika, vida_inicial_pika))
    
    barras_de_vida_squi = int(vida_squi * tamanio_barra_vi / vida_inicial_squi)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squi, " " * (10 - barras_de_vida_squi),
                                              vida_squi, vida_inicial_squi))
    
    if vida_squi <= 0:
        print("¡Squirtle ha sido derrotado!\n")
        break
    
    input("\nEnter para continuar...\n\n")
    os.system('clear')

    # Turno de Squiertle
    print("\nTurno de Squiertle\n")

    ataque_squiertle = None
    while ataque_squiertle not in ["P", "A", "B", "N"]:
        ataque_squiertle = input("¿ que ataque deseas realizar? [P]Placaje, [A]Pistola agua, [B]Burbuja, [N]No hacer Nada:\n")

    if ataque_squiertle == "P":
        print("Squirtle ataca con Placaje\n")
        vida_pika -= 10
    elif ataque_squiertle == "A":
        print("Squirtle ataca con Pistola agua\n")
        vida_pika -= 12
    elif ataque_squiertle == "B":
        print("Squirtle ataca con Burbuja\n")
        vida_pika -= 9
    elif ataque_squiertle == "N":
        print("Squirtle no hace nada")
        vida_pika == 0

    vida_pika = max(0, vida_pika)
    vida_squi = max(0, vida_squi)

    barras_de_vida_pika = int(vida_pika * tamanio_barra_vi / vida_inicial_pika)
    print("Pikachu:   [{}{}]({}/{})".format("*" * barras_de_vida_pika, " " * (10 - barras_de_vida_pika),
                                            vida_pika, vida_inicial_pika))
    
    barras_de_vida_squi = int(vida_squi * tamanio_barra_vi / vida_inicial_squi)
    print("Squirtle:    [{}{}][{}/{}]".format("*" * barras_de_vida_squi, " " * (10 - barras_de_vida_squi),
                                              vida_squi, vida_inicial_pika))
    
    if vida_pika <= 0:
        print("¡Pikachu ha sido derrotado!\n")
        break
    
    input("Pulsa enter para continuar...\n")
   
    os.system('clear')
    
    
if vida_pika > vida_squi:
    print("Pikachu ¡GANA!!!!")
else:
    print("Squirtle ¡GANA!!!")