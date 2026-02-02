import os
import random
import time

# Configuración del mapa
POS_X = 0
POS_Y = 1
NUM_ENTRENADORES = 5  # Número de entrenadores Pokemon en el mapa

# Definición del mapa (obstáculos)
definicion_obstaculos = """\
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

# Variables del jugador
mi_posicion = [5, 5]
entrenadores_pokemon = []  # Lista de entrenadores (objetos) en el mapa
fin_juego = False
victorias = 0  # Contador de victorias

# Crear la matriz de obstáculos
definicion_obstaculos = [list(fila) for fila in definicion_obstaculos.split("\n")]
ANCHO_MAPA = len(definicion_obstaculos[0])
ALTO_MAPA = len(definicion_obstaculos)

print("¡Bienvenido al mundo Pokemon!")
print("Controles: W(arriba), S(abajo), A(izquierda), D(derecha), Q(salir)")
print("Objetivo: Encuentra y derrota a todos los entrenadores Pokemon (*)")
input("Presiona Enter para comenzar...")

# Generar entrenadores Pokemon en posiciones aleatorias
while len(entrenadores_pokemon) < NUM_ENTRENADORES:
    nueva_posicion = [random.randint(0, ANCHO_MAPA - 1), random.randint(0, ALTO_MAPA - 1)]
    
    # Verificar que la posición no esté ocupada y no sea un obstáculo
    if (nueva_posicion not in entrenadores_pokemon and 
        nueva_posicion != mi_posicion and 
        definicion_obstaculos[nueva_posicion[POS_Y]][nueva_posicion[POS_X]] != "#"):
        entrenadores_pokemon.append(nueva_posicion)

def obtener_tecla():
    """Función para obtener una tecla presionada"""
    try:
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    except ImportError:
        # Para sistemas Unix/Linux
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.cbreak(fd)
            tecla = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return tecla.lower()

def batalla_pokemon():
    """Función que maneja la batalla Pokemon"""
    print("\n" + "="*50)
    print("    ¡UN ENTRENADOR POKEMON TE DESAFIA!")
    print("="*50)
    
    # Estadísticas iniciales de los Pokemon
    vida_inicial_pikachu = 80
    vida_inicial_squirtle = 90
    tamaño_barra_vida = 20
    
    vida_pikachu = vida_inicial_pikachu
    vida_squirtle = vida_inicial_squirtle
    
    print("\n¡Comienza la batalla!")
    print("Tu Pokemon: Squirtle")
    print("Pokemon enemigo: Pikachu")
    
    # Bucle de batalla
    while vida_pikachu > 0 and vida_squirtle > 0:
        
        # Turno de Pikachu (enemigo)
        print("\n" + "-"*40)
        print("TURNO DE PIKACHU (ENEMIGO)")
        print("-"*40)
        
        ataque_pikachu = random.randint(1, 2)
        if ataque_pikachu == 1:
            print("¡Pikachu ataca con Bola Voltio!")
            vida_squirtle -= 10
        else:
            print("¡Pikachu ataca con Onda Trueno!")
            vida_squirtle -= 11
        
        # Asegurar que la vida no sea negativa
        vida_pikachu = max(0, vida_pikachu)
        vida_squirtle = max(0, vida_squirtle)
        
        # Mostrar barras de vida
        barras_vida_pikachu = int(vida_pikachu * tamaño_barra_vida / vida_inicial_pikachu)
        barras_vida_squirtle = int(vida_squirtle * tamaño_barra_vida / vida_inicial_squirtle)
        
        print(f"\nPikachu (Enemigo):  [{'*' * barras_vida_pikachu}{' ' * (tamaño_barra_vida - barras_vida_pikachu)}] ({vida_pikachu}/{vida_inicial_pikachu})")
        print(f"Squirtle (Tu):      [{'*' * barras_vida_squirtle}{' ' * (tamaño_barra_vida - barras_vida_squirtle)}] ({vida_squirtle}/{vida_inicial_squirtle})")
        
        # Verificar si Squirtle fue derrotado
        if vida_squirtle <= 0:
            print("\n¡Tu Squirtle ha sido derrotado!")
            print("¡Has perdido la batalla!")
            return False
        
        input("\nPresiona Enter para tu turno...")
        
        # Turno de Squirtle (jugador)
        print("\n" + "-"*40)
        print("TU TURNO - SQUIRTLE")
        print("-"*40)
        
        ataque_elegido = None
        while ataque_elegido not in ["P", "A", "B", "N"]:
            print("\n¿Qué ataque deseas usar?")
            print("[P] Placaje (daño: 10)")
            print("[A] Pistola Agua (daño: 12)")
            print("[B] Burbuja (daño: 9)")
            print("[N] No hacer nada")
            ataque_elegido = input("Elige tu ataque: ").upper()
            
            if ataque_elegido not in ["P", "A", "B", "N"]:
                print("¡Opción inválida! Usa P, A, B o N")
        
        if ataque_elegido == "P":
            print("\n¡Squirtle ataca con Placaje!")
            vida_pikachu -= 10
        elif ataque_elegido == "A":
            print("\n¡Squirtle ataca con Pistola Agua!")
            vida_pikachu -= 12
        elif ataque_elegido == "B":
            print("\n¡Squirtle ataca con Burbuja!")
            vida_pikachu -= 9
        elif ataque_elegido == "N":
            print("\n¡Squirtle decide no hacer nada!")
        
        # Asegurar que la vida no sea negativa
        vida_pikachu = max(0, vida_pikachu)
        vida_squirtle = max(0, vida_squirtle)
        
        # Mostrar barras de vida actualizadas
        barras_vida_pikachu = int(vida_pikachu * tamaño_barra_vida / vida_inicial_pikachu)
        barras_vida_squirtle = int(vida_squirtle * tamaño_barra_vida / vida_inicial_squirtle)
        
        print(f"\nPikachu (Enemigo):  [{'*' * barras_vida_pikachu}{' ' * (tamaño_barra_vida - barras_vida_pikachu)}] ({vida_pikachu}/{vida_inicial_pikachu})")
        print(f"Squirtle (Tu):      [{'*' * barras_vida_squirtle}{' ' * (tamaño_barra_vida - barras_vida_squirtle)}] ({vida_squirtle}/{vida_inicial_squirtle})")
        
        # Verificar si Pikachu fue derrotado
        if vida_pikachu <= 0:
            print("\n¡Pikachu enemigo ha sido derrotado!")
            print("¡HAS GANADO LA BATALLA!")
            return True
        
        input("\nPresiona Enter para continuar...")
        os.system('clear' if os.name == 'posix' else 'cls')

def dibujar_mapa():
    """Función para dibujar el mapa actual"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print("="*60)
    print(f"    MUNDO POKEMON - Entrenadores derrotados: {victorias}/{NUM_ENTRENADORES}")
    print("="*60)
    print("Leyenda: @ = Tu, * = Entrenador Pokemon, # = Obstáculo")
    print("Controles: W(arriba), S(abajo), A(izquierda), D(derecha), Q(salir)")
    print("="*60)
    
    # Dibujar el borde superior
    print("+" + "-" * (ANCHO_MAPA * 2) + "+")
    
    # Dibujar cada fila del mapa
    for coordenada_y in range(ALTO_MAPA):
        print("|", end="")
        
        for coordenada_x in range(ANCHO_MAPA):
            caracter_a_dibujar = "  "
            
            # Verificar si hay un entrenador en esta posición
            for entrenador in entrenadores_pokemon:
                if entrenador[POS_X] == coordenada_x and entrenador[POS_Y] == coordenada_y:
                    caracter_a_dibujar = " *"
            
            # Verificar si el jugador está en esta posición
            if mi_posicion[POS_X] == coordenada_x and mi_posicion[POS_Y] == coordenada_y:
                caracter_a_dibujar = " @"
            
            # Verificar si hay un obstáculo
            if definicion_obstaculos[coordenada_y][coordenada_x] == "#":
                caracter_a_dibujar = "##"
            
            print(caracter_a_dibujar, end="")
        
        print("|")
    
    # Dibujar el borde inferior
    print("+" + "-" * (ANCHO_MAPA * 2) + "+")

# Bucle principal del juego
while not fin_juego:
    dibujar_mapa()
    
    # Verificar si ganó el juego
    if len(entrenadores_pokemon) == 0:
        print("\n" + "="*50)
        print("    ¡FELICITACIONES!")
        print("  ¡HAS DERROTADO A TODOS LOS ENTRENADORES!")
        print(f"    Victorias totales: {victorias}")
        print("="*50)
        break
    
    print(f"\nEntrenadores restantes: {len(entrenadores_pokemon)}")
    print("Ingresa tu movimiento:")
    
    # Obtener la dirección del jugador
    try:
        direccion = input("Dirección (w/a/s/d/q): ").lower()
    except KeyboardInterrupt:
        print("\n¡Juego interrumpido!")
        break
    
    nueva_posicion = None
    
    if direccion == "w":  # Arriba
        nueva_posicion = [mi_posicion[POS_X], (mi_posicion[POS_Y] - 1) % ALTO_MAPA]
    elif direccion == "s":  # Abajo
        nueva_posicion = [mi_posicion[POS_X], (mi_posicion[POS_Y] + 1) % ALTO_MAPA]
    elif direccion == "a":  # Izquierda
        nueva_posicion = [(mi_posicion[POS_X] - 1) % ANCHO_MAPA, mi_posicion[POS_Y]]
    elif direccion == "d":  # Derecha
        nueva_posicion = [(mi_posicion[POS_X] + 1) % ANCHO_MAPA, mi_posicion[POS_Y]]
    elif direccion == "q":  # Salir
        fin_juego = True
        print("¡Gracias por jugar!")
        break
    else:
        print("¡Movimiento inválido! Usa W, A, S, D o Q")
        input("Presiona Enter para continuar...")
        continue
    
    if nueva_posicion:
        # Verificar si la nueva posición no es un obstáculo
        if definicion_obstaculos[nueva_posicion[POS_Y]][nueva_posicion[POS_X]] != "#":
            mi_posicion = nueva_posicion
            
            # Verificar si hay un entrenador en la nueva posición
            entrenador_encontrado = None
            for entrenador in entrenadores_pokemon:
                if entrenador[POS_X] == mi_posicion[POS_X] and entrenador[POS_Y] == mi_posicion[POS_Y]:
                    entrenador_encontrado = entrenador
                    break
            
            # Si encontramos un entrenador, iniciar batalla
            if entrenador_encontrado:
                if batalla_pokemon():
                    # Si ganamos la batalla, eliminar el entrenador
                    entrenadores_pokemon.remove(entrenador_encontrado)
                    victorias += 1
                    print(f"\n¡Entrenador derrotado! Victorias: {victorias}")
                else:
                    # Si perdemos, el juego continúa pero no eliminamos al entrenador
                    print("\n¡Perdiste la batalla! El entrenador sigue en el mapa.")
                
                input("Presiona Enter para continuar...")
        else:
            print("¡No puedes moverte ahí! Hay un obstáculo.")
            input("Presiona Enter para continuar...")

print("\n¡Fin del juego!")