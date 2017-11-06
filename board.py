from __future__ import print_function
from termcolor import colored
Matrix = [[0 for x in range(85)] for y in range(41)]


class Board(object):

    @staticmethod
    def __initialise_board(wall, play, blk,
                         enemy_cord, enemy2_cord):
        for j in range(1, 40):
            for i in range(1, 85):
                if (wall[j][i] == 1):
                    Matrix[j][i] = 'X'
                elif ([j, i] not in play and [j, i] not in blk and
                      [j, i] not in enemy_cord and [j, i] not in enemy2_cord):
                    Matrix[j][i] = ' '
                elif ([j, i] in play):
                    Matrix[j][i] = 'B'
                elif ([j, i] in blk):
                    Matrix[j][i] = '/'
                elif ([j, i] in enemy_cord):
                    Matrix[j][i] = 'E'
                elif([j, i] in enemy2_cord):
                    Matrix[j][i] = 'F'
        return

    def check_position(self, x, y):
        if(x < 3 or x > 36 or y < 5 or y > 80):
            return 0
        if(Matrix[x][y] == ' '):
            return 1
        elif(Matrix[x][y] == 'B'):
            return 2
        elif(Matrix[x][y] == 'E'):
            return 3
        elif (Matrix[x][y] == 'F'):
            return 4
        else:
            return 0

    @staticmethod
    def __prboard(score, lives):
        for j in range(1, 39):
            for i in range(1, 85):
                if(Matrix[j][i] == 'B'):
                    print(colored(Matrix[j][i], 'yellow'), end="")
                elif(Matrix[j][i] == 'E'):
                    print(colored(Matrix[j][i], 'red'), end="")
                elif(Matrix[j][i] == 'X'):
                    print(colored(Matrix[j][i], 'white'), end="")
                elif (Matrix[j][i] == '/'):
                    print(colored(Matrix[j][i], 'green'), end="")
                elif (Matrix[j][i] == 'F'):
                    print(colored(Matrix[j][i], 'blue'), end="")
                else:
                    print(Matrix[j][i], end="")
            print(end="\n")
        print("Your Score is", score)
        print("Lives Left :", lives)
        return
