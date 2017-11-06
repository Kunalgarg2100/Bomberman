# This file makes the wall in the game
# Wall remains fixed in every level


class Wall(object):

    def __init__(self):
        pass

    @staticmethod
    # Construct Wall function, generates the wall layout
    # static method as it does n't need self parameter
    def __construct_wall(wall):
        for j in range(1, 40):
            if j < 3 or j > 36:  # Upper and Lower Wall
                for i in range(1, 85):
                    wall[j][i] = 1

            else:   # Walls in between the borders
                if j % 4 == 1 or j % 4 == 2:
                    for i in range(5, 81):
                        if i % 8 == 1 and i < 81:
                            for k in range(4):
                                wall[j][i + k] = 1

            for i in range(85):  # Left and Right Wall
                if i < 5 or i > 80:
                    wall[j][i] = 1
