from __future__ import print_function
from timeout import *
from bomb import *
from board import *
from getchunix import *
from bomberman import *
from enemy import *
from wall import *
import signal
import copy
import sys
import time
import os
from level import *
import random
getch = GetchUnix()


player_cord = [[3, 5], [3, 6], [3, 7], [3, 8], [4, 5], [4, 6],
               [4, 7], [4, 8]]  # contains all the co-ordinates of player
initenemy = []  # contains all the co-ordinates of enemies of type 1
initbrick = []  # contains all the co-ordinates of bricks
initenemy2 = []  # contains all the co-ordinates of enemies of type 2
brick_cord = []  # contains only the top left co-ordinates of bricks
enemy_cord = []  # contains only the top left co-ordinates of enemies of type1
enemy2_cord = []  # contains only the top left co-ordinates of enemies of type2
bombcord = [0, 0]  # Bomb Cordinates
score = [0]  # Conatins the game score

# Wall is constructed from Wall object
wall = [[0 for x in range(85)] for y in range(41)]
wal = Wall()
wal._Wall__construct_wall(wall)

# This a 2D list which is our game board
board = Board()
board._Board__initialise_board(wall, player_cord, initbrick,
                               initenemy, initenemy2)  # Initailizes

player = Player()  # Player object
enemy = Enemy1()  # Enemy type 1 object
level = Level()  # Level object
enemy2 = Enemy2()  # Enemy type 2 object


@timeout(0.3)
def input_fxn():
    try:
        text = getch()
        return text
    except TimeoutError:
        pass
    return ''

levelno = 1 # Level Number
level._Level__level_design(levelno, enemy, enemy_cord, initenemy,
                           enemy2, enemy2_cord, initenemy2, brick_cord, initbrick)
# enemy is enemy object ,brick_cord coordinates of bricks
# enemy is enemy objec is brick object
board._Board__initialise_board(wall, player_cord,
                               initbrick, initenemy, initenemy2)
board._Board__prboard(score[0], player._Player__lives)

distroyable_region = []
current_time = time.time()
current2_time = time.time()

while(1):
    if(player._Player__lives == 0):  # Check if player is still alive
        sys.exit(0)
    c = input_fxn()  # Takes the input from keyboard
    if (c == 'q'):  # If 'q' is pressed, player exits from game
        print("Your score is", score[0])
        print("GAME OVER")
        sys.exit(0)
    elif (c == 'd'):  # If 'd' is pressed, player moves right
        player.moveright(player_cord)
    elif (c == 'a'):  # If 'a' is pressed, player moves left
        player.moveleft(player_cord)
    elif (c == 'w'):  # If 'w' is pressed, player moves up
        player.moveup(player_cord)
    elif(c == 's'):  # If 's' is pressed, player moves down
        player.movedown(player_cord)
    elif(c == 'b'):  # If 'b' is pressed, player drops bomb
        if player.currentBombs > 0:
            x = player_cord[0][0]
            y = player_cord[0][1]
            # location of bomb is same as that of player when he drops the bomb
            bombcord = [x, y]
            bomb_location = [x, y]
            # distroyable_region consists the regions to be distroyed when bomb
            # explodes
            distroyable_region = []
            bm = Bomb(bombcord, distroyable_region,
                      score[0], enemy_cord, enemy2_cord)  # Planting Bomb
            player.currentBombs -= 1

    if not distroyable_region:  # If distroyable region is empty,do nothing
        pass
    else:  # If not, then we check the position of the player

        # If player is in the distroyable region
        if player_cord[0] in distroyable_region:
            player._Player__lives -= 1  # subtract lives
            player_cord = [[3, 5], [3, 6], [3, 7], [3, 8],  # reset the co-ordinates of the player
                           [4, 5], [4, 6], [4, 7], [4, 8]]
            if(player._Player__lives != 0):
                for p in player_cord:
                    Matrix[p[0]][p[1]] = 'B'

        if bomb_location in player_cord:  # If player it at bomb loaction
            for l in player_cord:
                Matrix[l[0]][l[1]] = 'B'
        for p in distroyable_region:  # Remove all the distroyable regions
            Matrix[p[0]][p[1]] = ' '
        distroyable_region = []

    if bombcord[0] != 0:  # status of bomb is updated if bomb is planted
        bm.update(bombcord, distroyable_region,
                  score, enemy_cord, enemy2_cord)
    else:   # If bomb is not planted
        player.currentBombs = 1

    rem_time = time.time() - current_time
    rem_time2 = time.time() - current2_time

    if rem_time >= 0.8:  # enemy moves after every 0.8 secs
        enemy._Enemy__enemyMotion(enemy_cord)
        current_time = time.time()
    if rem_time2 >= 0.5:  # enemy2 moves after every 0.5 secs
        enemy2._Enemy__enemyMotion(enemy2_cord)
        current2_time = time.time()

    # If player and bomberman are at same co-ordinates
    if player_cord in enemy_cord or (player_cord in enemy2_cord):
        player._Player__lives -= 1
        player_cord = [[3, 5], [3, 6], [3, 7], [3, 8], [4, 5],
                       [4, 6], [4, 7], [4, 8]]  # reseting the bomberman
        if player._Player__lives != 0:
            for p in player_cord:
                Matrix[p[0]][p[1]] = 'B'

    if player._Player__lives > 0:
        if bombcord not in player_cord and \
                player_cord[0] not in distroyable_region:
            for p in player_cord:
                Matrix[p[0]][p[1]] = 'B'
        for p in enemy_cord:
            kun = copy.deepcopy(p)
            for l in kun:
                Matrix[l[0]][l[1]] = 'E'
        for p in enemy2_cord:
            kun = copy.deepcopy(p)
            for l in kun:
                Matrix[l[0]][l[1]] = 'F'
        os.system('tput reset')
        board._Board__prboard(score[0], player._Player__lives)
    else:
        player_cord = []
        os.system('tput reset')
        board._Board__prboard(score[0], player._Player__lives)

    if levelno == 1:
        if (not enemy_cord) and (not enemy2_cord):
            board._Board__prboard(score[0], player._Player__lives)
            print('Level 1 completed')
            levelno = 2
            initenemy = []
            initbrick = []
            initenemy2 = []
            brick_cord = []
            enemy_cord = []
            enemy2_cord = []
            bombcord = [0, 0]
            player_cord = [[3, 5], [3, 6], [3, 7], [3, 8],
                           [4, 5], [4, 6], [4, 7], [4, 8]]
            player._Player__lives = 3
            level._Level__level_design(levelno, enemy, enemy_cord,
                                       initenemy, enemy2, enemy2_cord, initenemy2,
                                       brick_cord, initbrick)
            # enemy is enemy object #blk is brick object
            board._Board__initialise_board(wall, player_cord,
                                           initbrick, initenemy, initenemy2)
            os.system('tput reset')
            board._Board__prboard(score[0], player._Player__lives)

    if levelno == 2:
        if (not enemy_cord) and (not enemy2_cord):
            board._Board__prboard(score[0], player._Player__lives)
            print('Level 1 completed')
            levelno = 3
            initenemy = []
            initbrick = []
            initenemy2 = []
            brick_cord = []
            enemy_cord = []
            enemy2_cord = []
            bombcord = [0, 0]
            player_cord = [[3, 5], [3, 6], [3, 7], [3, 8],
                           [4, 5], [4, 6], [4, 7], [4, 8]]
            player._Player__lives = 4
            level._Level__level_design(levelno, enemy, enemy_cord,
                                       initenemy, enemy2, enemy2_cord, initenemy2,
                                       brick_cord, initbrick)
            # enemy is enemy object #blk is brick object
            board._Board__initialise_board(wall, player_cord,
                                           initbrick, initenemy, initenemy2)
            os.system('tput reset')
            board._Board__prboard(score[0], player._Player__lives)
    if player._Player__lives == 1:
        print('Last Live')
