from __future__ import print_function
from random import randint
from person import Person, Matrix


class Enemy(Person):

    def _moveright(self,  play):
        raise NotImplementedError("Subclass must implement abstract method")

    def _moveleft(self,  play):
        raise NotImplementedError("Subclass must implement abstract method")

    def _moveup(self,  play):
        raise NotImplementedError("Subclass must implement abstract method")

    def _movedown(self,  play):
        raise NotImplementedError("Subclass must implement abstract method")

    def __enemyMotion(self,  enem):
        for arr in enem:
            if((self.check_position(arr[0][0] + 2, arr[0][1]) == 0) and
               (self.check_position(arr[0][0] - 2, arr[0][1]) == 0) and
               (self.check_position(arr[0][0], arr[0][1] + 4) == 0) and
               (self.check_position(arr[0][0], arr[0][1] - 4) == 0)):
                continue
            else:
                step = 0
                while step == 0:
                    k = randint(1, 100)
                    if (k >= 1 and k <= 25):
                        if (self._moveright(arr)):
                            step += 1
                    elif (k > 25 and k <= 50):
                        if (self._movedown(arr)):
                            step += 1
                    elif (k > 50 and k <= 75):
                        if (self._moveleft(arr)):
                            step += 1
                    else:
                        if (self._moveup(arr)):
                            step += 1

    def __addenemy(self,  enem, initenemy):   # Private function
        while 1:
            x = randint(1, 17)
            x = x * 2 + 1
            if x % 4 == 1:
                y = randint(1, 9)
                y = y * 8 - 3
            elif x % 4 != 1:
                y = randint(1, 19)
                y = y * 4 + 1
            if(self.check_position(x, y) == 1):
                bx = []
                for i in range(x, x + 2):
                    for j in range(y, y + 4):
                        bx.append([i, j])
                        initenemy.append([i, j])
                enem.append(bx)
                break

    def __addenemies(self,  enemy_cord, initenemy, i):
        while i:
            self.__addenemy(enemy_cord, initenemy)
            i = i - 1


class Enemy1(Enemy):

    def _moveright(self,  new_cord):
        if(self._movergt(new_cord)):
            self._place_enemy(new_cord)
            return 1
        else:
            return 0

    def _moveleft(self,  new_cord):
        if(self._movelft(new_cord)):
            self._place_enemy(new_cord)
            return 1
        else:
            return 0

    def _moveup(self,  new_cord):
        if (self._moveupp(new_cord)):
            self._place_enemy(new_cord)
            return 1
        else:
            return 0

    def _movedown(self,  new_cord):
        if (self._movedwn(new_cord)):
            self._place_enemy(new_cord)
            return 1
        else:
            return 0


class Enemy2(Enemy):

    def _moveright(self,  new_cord):
        if(self._movergt(new_cord)):
            self._place_enemy2(new_cord)
            return 1
        else:
            return 0

    def _moveleft(self,  new_cord):
        if(self._movelft(new_cord)):
            self._place_enemy2(new_cord)
            return 1
        else:
            return 0

    def _moveup(self,  new_cord):
        if (self._moveupp(new_cord)):
            self._place_enemy2(new_cord)
            return 1
        else:
            return 0

    def _movedown(self,  new_cord):
        if (self._movedwn(new_cord)):
            self._place_enemy2(new_cord)
            return 1
        else:
            return 0
