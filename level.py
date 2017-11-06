from brick import *
brick = Brick()


class Level(object):

    def __level_design(self, level, enemy, enemy_cord, initenemy,
                       enemy2, enemy2_cord, initenemy2, brick_cord, initbrick):

        if(level == 1):
            enemy._Enemy__addenemies(enemy_cord, initenemy, 4)
            brick._Brick__addbricks(brick_cord, initbrick, 50)

        if(level == 2):
            enemy._Enemy__addenemies(enemy_cord, initenemy, 4)
            brick._Brick__addbricks(brick_cord, initbrick, 40)
            enemy2._Enemy__addenemies(enemy2_cord, initenemy2, 2)

        if(level == 3):
            enemy._Enemy__addenemies(enemy_cord, initenemy, 3)
            brick._Brick__addbricks(brick_cord, initbrick, 34)
            enemy2._Enemy__addenemies(enemy2_cord, initenemy2, 4)
