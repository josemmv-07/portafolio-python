import os 
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 11



my_position = [6,3]
map_objects = []

# Generate random objects on the map
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)





# Main Loop
while True:
    # DRAW Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)

            print(f" {char_to_draw} ", end="")
        print("|")
    
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where he wants to move

    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break

    os.system("clear")