from board import Board, Matrix


class Person(Board):

    @staticmethod
    # Updates the player co-ordinates on movement
    def __update_fun(player_cord, x, ch):
        # player_cord contains list of co-ordinates of player
        for i in range(len(player_cord)):
            Matrix[player_cord[i][0]][player_cord[i][1]] = ' '
        if x == 1:  # Move-Right
            for p in player_cord:
                p[1] += 4
        elif x == 2:  # Move-Left
            for p in player_cord:
                p[1] -= 4
        elif x == 3:  # Move-Up
            for p in player_cord:
                p[0] -= 2
        else:  # Move-Down
            for p in player_cord:
                p[0] += 2
        if ch == 8:  # If person moves to a blank position
            return 2
        elif ch == 24:  # If person moves to a Enemy position
            return 3
        elif ch == 32:  # If person moves to a Enemy2 position
            return 4
        elif ch == 16:  # If person moves to a Bomberman's position
            return 1

    def _movergt(self, player_cord):
        ch = 0
        for p in player_cord:
            ch += self.check_position(p[0], p[1] + 4)
        if ch:  # if person can move right
            x = self.__update_fun(player_cord, 1, ch)
            return x
        else:
            return 0

    def _movelft(self, player_cord):
        ch = 0
        for p in player_cord:
            # print(p)
            ch += self.check_position(p[0], p[1] - 4)
        if ch:  # if person can move left
            x = self.__update_fun(player_cord, 2, ch)
            return x
        else:
            return 0

    def _moveupp(self, player_cord):
        ch = 0
        for p in player_cord:
            ch += self.check_position(p[0] - 2, p[1])
        if ch:  # if person can move up
            x = self.__update_fun(player_cord, 3, ch)
            return x
        else:
            return 0

    def _movedwn(self, player_cord):
        ch = 0
        for p in player_cord:
            ch += self.check_position(p[0] + 2, p[1])
        if ch:  # if person can move down
            x = self.__update_fun(player_cord, 4, ch)
            return x
        else:
            return 0

    @staticmethod
    def _place_enemy(enemy_cord):
        for i in range(len(enemy_cord)):
            Matrix[enemy_cord[i][0]][enemy_cord[i][1]] = 'E'

    @staticmethod
    def _place_bomberman(player_cord):
        for i in range(len(player_cord)):
            Matrix[player_cord[i][0]][player_cord[i][1]] = 'B'

    @staticmethod
    def _place_enemy2(player_cord):
        for i in range(len(player_cord)):
            Matrix[player_cord[i][0]][player_cord[i][1]] = 'F'
