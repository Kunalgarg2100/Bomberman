from person import Person


class Player(Person):

    def __init__(self):
        self.currentBombs = 1
        self.maxBombs = 1
        self.__lives = 3

    def __update_move(self, arr, y):
        if (y == 2):  # Bomberman moved to blank area
            self._place_bomberman(arr)
        elif (y == 3):  # Bomberman moved to Enemy type 1 area
            self._place_enemy(arr)
        elif (y == 4):  # Bomberman moved to Enemy type 2 area
            self._place_enemy2(arr)
        else:
            return

    def moveright(self, arr):
        y = self._movergt(arr)
        self.__update_move(arr, y)

    def moveleft(self, arr):
        y = self._movelft(arr)
        self.__update_move(arr, y)

    def moveup(self, arr):
        y = self._moveupp(arr)
        self.__update_move(arr, y)

    def movedown(self, arr):
        y = self._movedwn(arr)
        self.__update_move(arr, y)
