from __future__ import print_function
from random import randint
from board import Board


class Brick(Board):

    def __init__(self):
        pass

    def __addbrick(self, blk, initbrick):   # This method is private to Brick class
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
                        initbrick.append([i, j])
                blk.append(bx)
                break

    def __addbricks(self, blk, initbrick, i):
        while i:
            self.__addbrick(blk, initbrick)
            i = i - 1
