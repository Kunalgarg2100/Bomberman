import time
import copy
from board import Matrix


class Bomb(object):

    def __init__(self, bombcord, explode_locations,
                 score, enemy_cord, enemy2_cord):
        self.created_time = time.time()
        self.curr_tick = 0

    def bomb_view(self, bombcord, n):
        for i in range(2):
            for j in range(1, 3):
                Matrix[bombcord[0] + i][bombcord[1] + j] = n
        Matrix[bombcord[0]][bombcord[1]] = "["
        Matrix[bombcord[0]][bombcord[1] + 3] = "]"
        Matrix[bombcord[0] + 1][bombcord[1]] = "["
        Matrix[bombcord[0] + 1][bombcord[1] + 3] = "]"

    def update(self, bombcord, explode_locations,
               score, enemy_cord, enemy2_cord):  # Upadates the state of bomb
        self.curr_tick = int(time.time() - self.created_time)
        if self.curr_tick >= 3:
            self.explode(bombcord, explode_locations,
                         score, enemy_cord, enemy2_cord)
        else:
            self.curr_tick += 1
        if self.curr_tick == 1:
            self.bomb_view(bombcord, 1)
        elif self.curr_tick == 2:
            self.bomb_view(bombcord, 0)

    def affected_area(self, x, y, score, explode_locations,
                      enemy_cord, enemy2_cord):
        if Matrix[x][y] != 'X':
            if Matrix[x][y] == '/':
                score[0] += 20
            elif Matrix[x][y] == 'E':
                score[0] += 100
                for p in enemy_cord:
                    kun = copy.deepcopy(p)
                    if [x, y] in kun:
                        enemy_cord.remove(p)
            elif Matrix[x][y] == 'F':
                score[0] += 130
                for p in enemy2_cord:
                    kun = copy.deepcopy(p)
                    if [x, y] in kun:
                        enemy2_cord.remove(p)

            for i in range(2):
                for j in range(4):
                    explode_locations.append([x + i, y + j])
            return
        else:
            return

    def explode(self, bombcord, explode_locations,
                score, enemy_cord, enemy2_cord):
        self.affected_area(bombcord[0] - 2, bombcord[1],
                           score, explode_locations, enemy_cord, enemy2_cord)
        self.affected_area(bombcord[0] + 2, bombcord[1],
                           score, explode_locations, enemy_cord, enemy2_cord)
        self.affected_area(bombcord[0], bombcord[1] - 4,
                           score, explode_locations, enemy_cord, enemy2_cord)
        self.affected_area(bombcord[0], bombcord[1] + 4,
                           score, explode_locations, enemy_cord, enemy2_cord)
        for p in explode_locations:
            Matrix[p[0]][p[1]] = 'e'
        bomb_location = []
        for i in range(2):
            for j in range(4):
                bomb_location.append([bombcord[0] + i, bombcord[1] + j])
        for p in bomb_location:  # Clean the bomb_location
            if((Matrix[p[0]][p[1]] is 0) or
               (Matrix[p[0]][p[1]] is '[') or
               (Matrix[p[0]][p[1]] is ']') or
               (Matrix[p[0]][p[1]] is 1)):
                Matrix[p[0]][p[1]] = ' '
        bombcord[0] = 0
        bombcord[1] = 0
