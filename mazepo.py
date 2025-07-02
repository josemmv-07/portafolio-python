""" El objetivo de este ejercicio final es crear un desafío Pokémon (o lo que más os guste/motive). 
Cada uno de los objetos será un entrenador pokémon, cuando nos situamos encima de una casilla que 
contiene un objeto, se lanzará un combate pokémon para luchar contra el entrenador rival. 
Tenemos que ganar el combate para que el entrenador desaparezca de nuestra lista e ir sucesivamente 
ganando a cada entrenador (objeto). Cuando hayamos vencido, se terminará el juego.
Nuestro pokémon será Pikachu y cada entrenador tendrá un solo pokémon a libre elección y con los
ataques que queráis."""


import os
import readchar
import random

# Conf del mapa
POS_X = 0
POS_Y = 1
NUM_ENTRENADORES = 5 

# Obstáculos
mapa = """\
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
##########################"""

mi_posicion = [5,5]
entrenadores = []
fin_juego = False
victorias = 0

# Lista de enemigos
pokemon_enemigos = ["Squirtle", "Charmander", "Bulbasur", "Geodude", "Machop"]

mapa = [list(fila) for fila in mapa.split("\n")]
ANCHO = len(mapa[0])
ALTO = len(mapa)

print("Bienvenido al mundo Pokemon!!!")
print("Controles: w(arriba), s(abajo), a(izquierda), d(derecha), q(salir)")
print("Tu pokemon es (Pikachu)")
print("Derrota a todos los entrenadores (*)")
input("Dale a ENTER.....")

# Entrenadores en posiciones random 
while len(entrenadores) < NUM_ENTRENADORES:
    nueva_pos = [random.randint(0, ANCHO -1), random.randint(0, ALTO -1)]

    if (nueva_pos not in entrenadores and nueva_pos != mi_posicion and mapa[nueva_pos[POS_Y]]
        [nueva_pos[POS_X]] != "#"):
        entrenadores.append(nueva_pos)

# Bucle principal
while not fin_juego:
    os.system("clear")

    print(f"POKEMON - Victorias: {victorias}/{NUM_ENTRENADORES}")
    print("TU = @, Entrenadores = *")
    print()

    # Mapa
    for y in range(ALTO):
        for x in range(ANCHO):
            if mi_posicion[POS_X] == x and mi_posicion[POS_Y] == y:
                print("@", end="")
            elif [x, y] in entrenadores:
                print("*",end="")
            elif mapa[y][x] == "#":
                print("#", end="")
            else:
                print(" ", end="")
        print()
    
    print(f"\nEntrenadores restantes = {len(entrenadores)}")

    # Si gana
    if len(entrenadores) == 0:
        print("\n¡FELICIDADES!!!! ")
        break

    # Dirección del jugador 
    direccion = readchar.readchar().lower()
    nueva_posicion = None

    if direccion == "w":
        nueva_posicion = [mi_posicion[POS_X], (mi_posicion[POS_Y] - 1) % ALTO]
    elif direccion == "s":
        nueva_posicion = [mi_posicion[POS_X], (mi_posicion[POS_Y] + 1) % ALTO]
    elif direccion == "a":
        nueva_posicion = [(mi_posicion[POS_X] - 1) % ANCHO, mi_posicion[POS_Y]]
    elif direccion == "d":
        nueva_posicion = [(mi_posicion[POS_X] + 1) % ANCHO, mi_posicion[POS_Y]]
    elif direccion == "q":
        fin_juego = True
        print("Gracias por jugar !!!!")
        break

    if nueva_posicion:
        # Verificamos que no tenemos obstáculo
        if mapa[nueva_posicion[POS_Y]][nueva_posicion[POS_X]] != "#":
            mi_posicion = nueva_posicion

            # Verificamos si hay entrenadores 
            entrenador_encontrado = None
            for i, entrenador in enumerate(entrenadores):
                if entrenador[POS_X] == mi_posicion[POS_X] and entrenador[POS_Y] == mi_posicion[POS_Y]:
                    entrenador_encontrado = entrenador
                    pokemon_enemigo = pokemon_enemigos[i]
                    break

            # Batalla
            if entrenador_encontrado:
                os.system("clear")
                print("UN ENTRENADOR TE DESAFÍA!!!!!!")
                print(F"Tu Pikachu vs {pokemon_enemigo} enemigo")
                print()

                # Vida de los Pokemon
                vida_pikachu = 85
                if pokemon_enemigos == "Squirtle":
                    vida_enemigo = 90
                elif pokemon_enemigos == "Charmander":
                    vida_enemigo = 80
                elif pokemon_enemigos == "Bulbasaur":
                    vida_enemigo = 88
                elif pokemon_enemigos == "Geodude":
                    vida_enemigo = 95
                else: # Machop
                    vida_enemigo = 82
                
                vida_enemigo_max = vida_enemigo

                # Bucle de la batalla
                while vida_enemigo > 0 and vida_pikachu > 0:

                    # Turno de entrenadores
                    print(f"Turno de {pokemon_enemigo}:")
                    ataque = random.randint(1, 2)

                    if pokemon_enemigos == "Squirtle":
                        if ataque == 1:
                            print("Squirtle usa pistola agua !!!")
                            vida_pikachu -= 12
                        else:
                            print("Squirtle usa BURBUJA")
                            vida_pikachu -= 9
                    elif pokemon_enemigos == "Charmander":
                        if ataque == 1:
                            print("Charmander usa Ascuas!!!!")
                            vida_pikachu -= 11
                        else:
                            print("Charmander usa ARAÑAZO")
                            vida_pikachu -= 8
                    elif pokemon_enemigos == "Bulbasur":
                        if ataque == 1:
                            print("Bulbasaur usa Hoja afilada!!")
                            vida_pikachu -= 10
                        else:
                            print("Bulbasaur usa Placaje!!!!")
                            vida_pikachu -= 9
                    elif pokemon_enemigos == "Geodude":
                        if ataque == 1:
                            print("Geodude usa Lanzarrocas")
                            vida_pikachu -= 13
                        else:
                            print("Geudude usa PUÑOOOOO")
                            vida_pikachu -= 10
                    else: # Machap
                        if ataque == 1:
                            print("MACHOP USA GOLPE KARATE")
                            vida_pikachu -= 14
                        else:
                            print("Machop usa Patada baja!!!")
                            vida_pikachu -= 11
                    
                    vida_pikachu = max(0, vida_pikachu)
                    vida_enemigo = max(0, vida_enemigo)

                    print(f"{pokemon_enemigo}: {vida_enemigo}/{vida_enemigo_max}")
                    print(f"Pikachu: {vida_pikachu}/85")

                    if vida_pikachu <= 0:
                        print("\n Pikachu ha sido derrotado")
                        input("ENTER para continuar.....")
                        break

                    print("\nTu turno:")
                    print("[i]Impactrueno, [r]Rayo, [a]Ataque rápido")
                    ataque_jugador = readchar.readchar().lower()

                    if ataque_jugador == "i":
                        print("Pikachu usa IMPACTRUENO")
                        vida_enemigo -= 12
                    elif ataque_jugador == "r":
                        print("Pikachu usa RAYO")
                        vida_enemigo -= 15
                    elif ataque_jugador == "a":
                        print("Pikachu usa ataque rápido ")
                        vida_enemigo -= 10
                    
                    vida_pikachu = max(0, vida_pikachu)
                    vida_enemigo = max(0, vida_enemigo)

                    print(f"{pokemon_enemigo}: {vida_enemigo}/{vida_enemigo_max}")
                    print(f"Pikachu: {vida_pikachu}/85")
                    print()

                    if vida_enemigo <= 0:
                        print(f"{pokemon_enemigo} ha sido derrotado!!")
                        print("PIKACHU HA GANADO!!!!!")
                        entrenadores.remove(entrenador_encontrado)
                        victorias += 1
                        input("ENTER para continuar...")
                        break

print("\n FIN del Juego")