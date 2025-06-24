""" El objetivo de este ejercicio final es crear un desafío Pokémon (o lo que más os guste/motive). 
Cada uno de los objetos será un entrenador pokémon, cuando nos situamos encima de una casilla que 
contiene un objeto, se lanzará un combate pokémon para luchar contra el entrenador rival. 
Tenemos que ganar el combate para que el entrenador desaparezca de nuestra lista e ir sucesivamente 
ganando a cada entrenador (objeto). Cuando hayamos vencido, se terminará el juego.
Nuestro pokémon será Pikachu y cada entrenador tendrá un solo pokémon a libre elección y con los
ataques que queráis."""


import os
import random
import readchar
from random import randint

titulo = "MINI-POKE"
print("\n" + titulo +"\n" + "-" * len(titulo) + "\n")

POS_X = 0
POS_Y = 1
NUM_DE_ENTREN_EN_MAP = 6

yo_entre = [0,1]
map_entre = []
entrenador_ganado = 0
entrenadores = []
fin_juego = False
vencido = False

obstaculo = """\
##########################
#######                  #
#######               ####
#####                 ####
#        #####           #
#        #####      ######
#        #####         ###
#                 ########
#                        #
####################   ###
#####                    #
########               ###
#                  #######
#####                 ####
##########################\
"""
# Creando obstáculo
obstaculo = [list(fila) for fila in obstaculo.split("\n")]

MAP_ANCHO = len(obstaculo[0])
MAP_ALTURA = len(obstaculo)

while not fin_juego:
    os.system("clear")
    # Generamos entrenadores random en el mapa
    while len(map_entre) < NUM_DE_ENTREN_EN_MAP:
        nuevo_yo_entre = [random.randint(0, MAP_ANCHO - 1), random.randint(0, MAP_ALTURA - 1)]

        if nuevo_yo_entre not in map_entre and nuevo_yo_entre != yo_entre and \
                obstaculo[nuevo_yo_entre[POS_Y]][nuevo_yo_entre[POS_X]] != "#":
            map_entre.append(nuevo_yo_entre)
    
    # MAPA
    print("+" + "-" * MAP_ANCHO * 4 + "+")

    for coordenada_y in range(MAP_ALTURA):
        print("|", end="")

        for coordenada_x in range(MAP_ANCHO):

            simbolo_que_mostrar = "  "
            objeto_en_la_celda = None
            entre_en_la_celda = None

            for map_entrenadores in map_entre:
                if map_entrenadores[POS_X] == coordenada_x and map_entrenadores[POS_Y] == coordenada_y:
                    simbolo_que_mostrar = " *"
                    objeto_en_la_celda = map_entrenadores

            for combate in entrenadores:
                if combate[POS_X] == coordenada_x and combate[POS_Y] == coordenada_y:
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